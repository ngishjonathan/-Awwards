from django.test import TestCase

from django.test import TestCase

from .models import User,Profile,Project,Review
import datetime as dt

class ProfileTest(TestCase):
    """class for testing the class Profile."""
    def setUp(self):
        self.emma = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')

    def test_instance(self):
        self.assertTrue(isinstance(self.emma,Profile))

    def test_save(self):
        self.emma.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) >0 )

# Create your tests here.
