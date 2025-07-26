import unittest
from datetime import datetime, timedelta
from personnel import Patient


class PatientTestCase(unittest.TestCase):
    def setUp(self):
        self.patient = Patient("tom", "jones", "01/01/1980", "regular check-up", "Doctor")
        Patient._Patient__id_count = 0

    def test_that_a_patient_can_be_created(self):
        expected = f"""
Patient ID: PTT-001
Name: Tom Jones
Date of Birth: 01/01/1980
Contact Email: No emails
Contact Number: No phone numbers"""
        self.assertMultiLineEqual(self.patient.__str__(), expected)


    def test_that_a_patients_details_can_be_edited(self):
        self.patient.first_name = "mary"
        self.patient.last_name = "taylor-britt"
        self.patient.date_of_birth = "01/01/1988"
        self.patient.add_email("something@something.something")
        self.patient.add_number("123456789")

        expected = f"""
Patient ID: PTT-001
Name: Mary Taylor-Britt
Date of Birth: 01/01/1988
Contact Email: something@something.something
Contact Number: 123456789"""
        self.assertMultiLineEqual(self.patient.__str__(), expected)


    def test_that_names_cannot_be_empty(self):
        with self.assertRaises(ValueError): self.patient.first_name = ""
        with self.assertRaises(ValueError): self.patient.last_name = None

    def test_that_names_cannot_be_one_character(self):
        with self.assertRaises(ValueError): self.patient.first_name = "a"
        with self.assertRaises(ValueError): self.patient.last_name = "j"

    def test_that_names_cannot_be_non_alphabetical(self):
        with self.assertRaises(ValueError): self.patient.first_name = "9tom"
        with self.assertRaises(ValueError): self.patient.last_name = "jon£$"

    def test_that_names_are_case_insensitive(self):
        self.patient.first_name = "tHomAs"
        self.patient.last_name = "jOhaNnEs"
        self.assertEqual(self.patient.first_name, "Thomas")
        self.assertEqual(self.patient.last_name, "Johannes")

    def test_that_names_can_contain_hyphen_and_apostrophe(self):
        self.patient.first_name = "mary-jane"
        self.patient.last_name = "taylor-britt"
        self.assertEqual(self.patient.first_name, "Mary-Jane")
        self.assertEqual(self.patient.last_name, "Taylor-Britt")

    def test_that_date_of_birth_can_only_be_in_DMYYYY_format(self):
        with self.assertRaises(ValueError): self.patient.date_of_birth = "33/1/1980"
        with self.assertRaises(ValueError): self.patient.date_of_birth = "7/14/1975"
        with self.assertRaises(ValueError): self.patient.date_of_birth = "31/12/90"

    def test_that_date_of_birth_cannot_be_in_the_future(self):
        with self.assertRaises(ValueError): self.patient.date_of_birth = "3/01/2055"
        with self.assertRaises(ValueError): self.patient.date_of_birth = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")

    def test_that_email_can_be_added(self):
        self.patient.add_email("tom_jones123@gmail.com")
        self.assertEqual(self.patient.emails, "tom_jones123@gmail.com")

        self.patient.add_email("tjWatt@yahoo.co.uk")
        self.assertEqual(self.patient.emails, "tom_jones123@gmail.com, tjWatt@yahoo.co.uk")

    def test_that_email_can_be_removed(self):
        self.patient.add_email("tom_jones123@gmail.com")
        self.assertEqual(self.patient.emails, "tom_jones123@gmail.com")

        self.patient.delete_email("tom_jones123@gmail.com")
        self.assertEqual(self.patient.emails, "No emails")

    def test_that_emails_can_be_edited(self):
        self.patient.add_email("tom_jones123@gmail.com")
        self.assertEqual(self.patient.emails, "tom_jones123@gmail.com")

        self.patient.edit_email("tom_jones123@gmail.com", "tjWatt@yahoo.co.uk")
        self.assertEqual(self.patient.emails, "tjWatt@yahoo.co.uk")

    def test_that_number_can_be_added(self):
        self.patient.add_number("87")
        self.assertEqual(self.patient.numbers, "87")

        self.patient.add_number("123")
        self.assertEqual(self.patient.numbers, "87, 123")

    def test_that_number_can_be_removed(self):
        self.patient.add_number("87")
        self.assertEqual(self.patient.numbers, "87")

        self.patient.delete_number("87")
        self.assertEqual(self.patient.numbers, "No phone numbers")

    def test_that_number_can_be_edited(self):
        self.patient.add_number("87")
        self.assertEqual(self.patient.numbers, "87")

        self.patient.edit_number("87", "123")
        self.assertEqual(self.patient.numbers, "123")

    def test_that_reason_can_be_edited(self):
        self.assertEqual(self.patient.reason, "regular check-up")
        self.patient.reason = "asthma attack"
        self.assertEqual(self.patient.reason, "asthma attack")

    def test_that_specialty_needed_can_be_edited(self):
        self.assertEqual(self.patient.specialty_needed, "Doctor")
        self.patient.reason = "Nurse"
        self.assertEqual(self.patient.reason, "Nurse")

        
if __name__ == '__main__':
    unittest.main()