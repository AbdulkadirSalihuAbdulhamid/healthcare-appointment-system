import json
import random


def generate_fixtures():
    # Default password for all users: aaa
    fixtures = []
    user_id = 1
    profile_id = 1

    # Nigerian names
    male_first_names = [
        "Adebayo",
        "Chukwuemeka",
        "Ibrahim",
        "Olumide",
        "Emeka",
        "Adeyemi",
        "Musa",
        "Oluwaseun",
        "Tunde",
        "Femi",
        "Kolawole",
        "Segun",
        "Babatunde",
        "Adeolu",
        "Ifeanyi",
    ]

    male_last_names = [
        "Adebayo",
        "Okafor",
        "Ibrahim",
        "Oluwaseun",
        "Chukwu",
        "Adeyemi",
        "Musa",
        "Okafor",
        "Adeleke",
        "Obi",
        "Okoro",
        "Adekunle",
        "Babatunde",
        "Ogunleye",
        "Nwankwo",
    ]

    female_first_names = [
        "Amina",
        "Chioma",
        "Folake",
        "Ngozi",
        "Aisha",
        "Bukola",
        "Fatima",
        "Adunni",
        "Ifeoma",
        "Zainab",
        "Temitope",
        "Blessing",
        "Adeola",
        "Halima",
        "Funke",
    ]

    female_last_names = [
        "Adebayo",
        "Okafor",
        "Ibrahim",
        "Oluwaseun",
        "Chukwu",
        "Adeyemi",
        "Musa",
        "Okafor",
        "Adeleke",
        "Obi",
        "Okoro",
        "Adekunle",
        "Babatunde",
        "Ogunleye",
        "Nwankwo",
    ]

    specializations = [
        "Cardiologist",
        "Dermatologist",
        "Neurologist",
        "Pediatrician",
        "Orthopedic Surgeon",
        "Psychiatrist",
        "Gynecologist",
        "Dentist",
        "Ophthalmologist",
        "ENT Specialist",
    ]

    cities = [
        "Lagos",
        "Abuja",
        "Kano",
        "Ibadan",
        "Port Harcourt",
        "Benin City",
        "Kaduna",
        "Aba",
        "Maiduguri",
        "Ilorin",
        "Warri",
        "Onitsha",
    ]

    states = [
        "Lagos",
        "Abuja",
        "Kano",
        "Oyo",
        "Rivers",
        "Edo",
        "Kaduna",
        "Abia",
        "Borno",
        "Kwara",
        "Delta",
        "Anambra",
    ]

    # Doctor images mapping - ensure unique assignment
    # List of available images
    available_images = [
        "profiles/dr_aisha_adeleke.jpg.jpg",
        "profiles/dr_amina_ademeyi.jpg.jpg",
        "profiles/dr_babatunde_adeyemi.jpg.jpg",
        "profiles/dr_bukola_obi.jpg.jpg",
        "profiles/dr_fatima_musa.jpg",
        "profiles/dr_femi.jpg",
        "profiles/dr_funke_okafor.jpg.png",
        "profiles/dr_halima_musa.jpg.jpg",
        "profiles/dr_ibrahim_nwankwo.jpg.jpg",
        "profiles/dr_ifeoma_adeyemi.jpg.jpg",
        "profiles/dr_segun_ibrahim.jpg.jpg",
    ]
    
    # Shuffle images to randomize assignment
    random.shuffle(available_images)
    image_index = 0

    # Generate 15 doctors
    for i in range(1, 16):
        # Randomly choose gender for doctor
        gender = random.choice(["male", "female"])
        if gender == "male":
            first_name = random.choice(male_first_names)
            last_name = random.choice(male_last_names)
        else:
            first_name = random.choice(female_first_names)
            last_name = random.choice(female_last_names)

        doctor_username = f"doctor{i}"

        # Assign doctor image - cycle through available images
        if image_index < len(available_images):
            doctor_image = available_images[image_index]
            image_index += 1
        else:
            # If we run out of images, use default
            doctor_image = "defaults/user.png"

        doctor = {
            "model": "accounts.user",
            "fields": {
                "password": "pbkdf2_sha256$720000$OcHcETvxtfm6vrCHNV3C26$XuDrKX1V0pYUyxhCFekQ4QZtJ+17u7B/sjd/y7zuGC8=",  # "aaa"
                "username": doctor_username,
                "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
                "first_name": first_name,
                "last_name": last_name,
                "role": "doctor",
                "is_active": True,
                "date_joined": "2023-01-01T00:00:00Z",
            },
        }
        fixtures.append(doctor)

        # Doctor Profile
        doctor_profile = {
            "model": "accounts.profile",
            "pk": profile_id,
            "fields": {
                "user": user_id,
                "avatar": doctor_image,
                "phone": f"+234{random.randint(700, 999)}{random.randint(1000000, 9999999)}",
                "dob": f"{random.randint(1960, 1990)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "about": f"MBBS from {random.choice(['University of Lagos College of Medicine', 'University of Ibadan College of Medicine', 'Ahmadu Bello University', 'University of Nigeria Nsukka'])}. {random.randint(5, 20)} years of experience in {random.choice(specializations)}.",
                "specialization": random.choice(specializations),
                "gender": gender,
                "address": f"{random.randint(1, 99)} {random.choice(['Victoria Island', 'Ikoyi', 'Lekki', 'Surulere', 'Yaba'])} Street",
                "city": random.choice(cities),
                "state": random.choice(states),
                "postal_code": f"{random.randint(100001, 999999)}",
                "country": "Nigeria",
                "price_per_consultation": random.randint(5000, 20000),
                "is_available": True,
            },
        }
        fixtures.append(doctor_profile)
        user_id += 1
        profile_id += 1

    # Generate 15 patients
    for i in range(1, 16):
        # Randomly choose gender for patient
        gender = random.choice(["male", "female"])
        if gender == "male":
            first_name = random.choice(male_first_names)
            last_name = random.choice(male_last_names)
        else:
            first_name = random.choice(female_first_names)
            last_name = random.choice(female_last_names)

        patient_username = f"patient{i}"
        patient = {
            "model": "accounts.user",
            "pk": user_id,
            "fields": {
                "password": "pbkdf2_sha256$720000$OcHcETvxtfm6vrCHNV3C26$XuDrKX1V0pYUyxhCFekQ4QZtJ+17u7B/sjd/y7zuGC8=",  # "aaa"
                "username": patient_username,
                "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
                "first_name": first_name,
                "last_name": last_name,
                "role": "patient",
                "is_active": True,
                "date_joined": "2023-01-01T00:00:00Z",
            },
        }
        fixtures.append(patient)

        # Patient Profile
        blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        areas = [
            "Victoria Island",
            "Ikoyi",
            "Lekki",
            "Surulere",
            "Yaba",
            "Ikeja",
            "Gbagada",
            "Maryland",
        ]

        patient_profile = {
            "model": "accounts.profile",
            "pk": profile_id,
            "fields": {
                "user": user_id,
                "phone": f"+234{random.randint(700, 999)}{random.randint(1000000, 9999999)}",
                "dob": f"{random.randint(1970, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "gender": gender,
                "address": f"Flat {random.randint(1,20)}A, {random.randint(1, 99)} {random.choice(areas)} Street",
                "city": random.choice(cities),
                "state": random.choice(states),
                "postal_code": f"{random.randint(100001, 999999)}",
                "country": "Nigeria",
                "blood_group": random.choice(blood_groups),
                "allergies": random.choice(
                    ["None", "Dust Allergy", "Food Allergy", "Drug Allergy"]
                ),
                "medical_conditions": random.choice(
                    ["None", "High Blood Pressure", "Diabetes", "Asthma"]
                ),
            },
        }
        fixtures.append(patient_profile)
        user_id += 1
        profile_id += 1

    # Write fixtures to file
    with open("fixtures/initial_data.json", "w") as f:
        json.dump(fixtures, f, indent=2)


if __name__ == "__main__":
    generate_fixtures()
