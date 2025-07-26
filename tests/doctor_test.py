import unittest
from datetime import datetime, timedelta
from personnel import Doctor
from utilities.specialisations import Specialisation


class DoctorTestCase(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("tom", "jones", "01/01/1980", "Doctor")
        Doctor._Doctor__id_count = 0

    def test_that_a_doctor_can_be_created(self):
        expected = f"""
Medical ID: DTR-001
Name: Tom Jones
Date of Birth: 01/01/1980
Specialisation: Doctor
Contact Email: No emails
Contact Number: No phone numbers"""
        self.assertMultiLineEqual(self.doctor.__str__(), expected)

    def test_that_a_doctors_details_can_be_edited(self):
        self.doctor.first_name = "mary-jane"
        self.doctor.last_name = "mahomes"
        self.doctor.date_of_birth = "01/01/1988"
        self.doctor.specialisation = "Nurse"
        self.doctor.add_email("something@something.something")
        self.doctor.add_number("123456789")

        expected = f"""
Medical ID: DTR-001
Name: Mary-Jane Mahomes
Date of Birth: 01/01/1988
Specialisation: Nurse
Contact Email: something@something.something
Contact Number: 123456789"""
        self.assertMultiLineEqual(self.doctor.__str__(), expected)


    def test_that_names_cannot_be_empty(self):
        with self.assertRaises(ValueError): self.doctor.first_name = ""
        with self.assertRaises(ValueError): self.doctor.last_name = None

    def test_that_names_cannot_be_one_character(self):
        with self.assertRaises(ValueError): self.doctor.first_name = "a"
        with self.assertRaises(ValueError): self.doctor.last_name = "j"

    def test_that_names_cannot_be_non_alphabetical(self):
        with self.assertRaises(ValueError): self.doctor.first_name = "9tom"
        with self.assertRaises(ValueError): self.doctor.last_name = "jon£$"

    def test_that_names_are_case_insensitive(self):
        self.doctor.first_name = "tHomAs"
        self.doctor.last_name = "jOhaNnEs"
        self.assertEqual(self.doctor.first_name, "Thomas")
        self.assertEqual(self.doctor.last_name, "Johannes")

    def test_that_names_can_contain_hyphen_and_apostrophe(self):
        self.doctor.first_name = "mary-jane"
        self.doctor.last_name = "taylor-britt"
        self.assertEqual(self.doctor.first_name, "Mary-Jane")
        self.assertEqual(self.doctor.last_name, "Taylor-Britt")

    def test_that_date_of_birth_can_only_be_in_DMYYYY_format(self):
        with self.assertRaises(ValueError): self.doctor.date_of_birth = "33/1/1980"
        with self.assertRaises(ValueError): self.doctor.date_of_birth = "7/14/1975"
        with self.assertRaises(ValueError): self.doctor.date_of_birth = "31/12/90"

    def test_that_date_of_birth_cannot_be_in_the_future(self):
        with self.assertRaises(ValueError): self.doctor.date_of_birth = "3/01/2055"
        with self.assertRaises(ValueError): self.doctor.date_of_birth = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")

    def test_that_email_can_be_added(self):
        self.doctor.add_email("tom_jones123@gmail.com")
        self.assertEqual(self.doctor.emails, "tom_jones123@gmail.com")

        self.doctor.add_email("tjWatt@yahoo.co.uk")
        self.assertEqual(self.doctor.emails, "tom_jones123@gmail.com, tjWatt@yahoo.co.uk")

    def test_that_email_can_be_removed(self):
        self.doctor.add_email("tom_jones123@gmail.com")
        self.assertEqual(self.doctor.emails, "tom_jones123@gmail.com")

        self.doctor.delete_email("tom_jones123@gmail.com")
        self.assertEqual(self.doctor.emails, "No emails")

    def test_that_emails_can_be_edited(self):
        self.doctor.add_email("tom_jones123@gmail.com")
        self.assertEqual(self.doctor.emails, "tom_jones123@gmail.com")

        self.doctor.edit_email("tom_jones123@gmail.com", "tjWatt@yahoo.co.uk")
        self.assertEqual(self.doctor.emails, "tjWatt@yahoo.co.uk")

    def test_that_number_can_be_added(self):
        self.doctor.add_number("87")
        self.assertEqual(self.doctor.numbers, "87")

        self.doctor.add_number("123")
        self.assertEqual(self.doctor.numbers, "87, 123")

    def test_that_number_can_be_removed(self):
        self.doctor.add_number("87")
        self.assertEqual(self.doctor.numbers, "87")

        self.doctor.delete_number("87")
        self.assertEqual(self.doctor.numbers, "No phone numbers")

    def test_that_number_can_be_edited(self):
        self.doctor.add_number("87")
        self.assertEqual(self.doctor.numbers, "87")

        self.doctor.edit_number("87", "123")
        self.assertEqual(self.doctor.numbers, "123")

    def test_that_specialisation_can_be_edited(self):
        self.assertEqual(self.doctor.specialisation, Specialisation.DOCTOR)
        self.doctor.specialisation = "Nurse"
        self.assertEqual(self.doctor.specialisation, Specialisation.NURSE)

    def test_that_specialisation_is_case_insensitive(self):
        self.doctor.specialisation = "nuRsE"
        self.assertEqual(self.doctor.specialisation, Specialisation.NURSE)

    def test_specialisation_raises_error_if_unavailable(self):
        with self.assertRaises(ValueError): self.doctor.specialisation = "Farmer"

if __name__ == '__main__':
    unittest.main()