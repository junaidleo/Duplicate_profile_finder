from model import Profile
from service import find_duplicates

profile = Profile()

profile.add_profile("profile 1", {'id': 1, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhai', 'last_name': 'Shah', 'class_year': None, 'date_of_birth': '1990-10-11'})
profile.add_profile("profile 2", {'id': 2, 'email': 'knowkanhai@gmail.com', 'first_name': 'Kanhail', 'last_name': 'Shah', 'class_year': '2012', 'date_of_birth': '1990-10-11'})

find_duplicates(["profile 1", "profile 2"], ['email', 'first_name', 'last_name', 'class_year', 'date_of_birth'], profile)