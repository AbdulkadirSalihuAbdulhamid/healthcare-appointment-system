from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class PatientRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and has the patient role."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if request.user.role != "patient":
            messages.error(request, "This page is only for patient accounts.")
            if request.user.is_superuser:
                return redirect("admin-dashboard")
            if request.user.role == "doctor":
                return redirect("doctors:dashboard")
            return redirect("core:home")
        return super().dispatch(request, *args, **kwargs)


class DoctorRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and has the doctor role."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if request.user.role != "doctor":
            messages.error(request, "This page is only for doctor accounts.")
            if request.user.is_superuser:
                return redirect("admin-dashboard")
            if request.user.role == "patient":
                return redirect("patients:dashboard")
            return redirect("core:home")
        return super().dispatch(request, *args, **kwargs)
