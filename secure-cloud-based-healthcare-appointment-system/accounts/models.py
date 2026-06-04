from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.db.models import Avg

from accounts.managers import CustomUserManager
from utils.file_utils import (
    profile_photo_directory_path,
)


class User(AbstractUser):
    """
    Custom user model with extra fields
    """

    class RoleChoices(models.TextChoices):
        DOCTOR = "doctor", "Doctor"
        PATIENT = "patient", "Patient"

    username = models.CharField(max_length=30, unique=True)
    role = models.CharField(
        choices=RoleChoices.choices,
        max_length=20,
        default="patient",
        error_messages={"required": "Role must be provided"},
    )
    email = models.EmailField(
        blank=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    registration_number = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip() or self.username

    def get_doctor_profile(self):
        """
        Return doctor profile URL
        """
        return reverse(
            "doctors:doctor-profile", kwargs={"username": self.username}
        )

    @property
    def rating(self):
        """Star rating for templates (0–5); uses review average when present."""
        avg = self.average_rating
        return int(round(avg)) if avg else 0

    @property
    def average_rating(self):
        return (
            self.reviews_received.aggregate(Avg("rating"))["rating__avg"] or 0
        )

    @property
    def rating_count(self):
        return self.reviews_received.count()

    @property
    def rating_distribution(self):
        distribution = {i: 0 for i in range(1, 6)}
        for rating in self.reviews_received.values_list("rating", flat=True):
            distribution[rating] += 1
        return distribution


class Profile(models.Model):
    """
    User profile
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    avatar = models.ImageField(
        default="defaults/user.png", upload_to=profile_photo_directory_path
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        blank=True,
    )
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    price_per_consultation = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    is_available = models.BooleanField(default=True)
    blood_group = models.CharField(
        max_length=5,
        choices=[
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("O+", "O+"),
            ("O-", "O-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
        ],
        blank=True,
        null=True,
    )
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Profile of {}".format(self.user.username)

    def _static_avatar_relative_path(self):
        """Bundled doctor photo shipped under static/assets/img/doctors/."""
        from django.contrib.staticfiles import finders

        if self.user.role != User.RoleChoices.DOCTOR:
            return None
        username = self.user.username
        for ext in ("jpg", "jpeg", "png", "webp"):
            rel = f"assets/img/doctors/{username}.{ext}"
            if finders.find(rel):
                return rel
        return None

    @property
    def has_stored_avatar(self):
        """True when a real photo is available (uploaded media or bundled static file)."""
        if self._static_avatar_relative_path():
            return True
        name = (self.avatar.name or "").strip()
        if not name or name == "defaults/user.png":
            return False
        try:
            return self.avatar.storage.exists(name)
        except Exception:
            return False

    @property
    def image(self):
        """URL for templates; static doctor photo, then media, then default SVG."""
        from django.templatetags.static import static

        rel = self._static_avatar_relative_path()
        if rel:
            return static(rel)
        if self.has_stored_avatar:
            return self.avatar.url
        return static("assets/img/default-avatar.svg")
