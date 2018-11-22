from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.user.save()
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ras, Profile))

    def test_save(self):
        self.ras.create_user_profile(self.user, True)
        self.ras.save_user_profile(self.user)
        users = Profile.objects.all()
        self.assertTrue(len(users) > 0)


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User(username='Keller Njoroge', email='keller@kell.com', password='passwadd')
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.gram = Project(projectname='Keller_Insta', overview='A clone of Instagram',
                            profile=self.user, url='Keller_insta.com')

    def tearDown(self):
        Profile.objects.all().delete()
        self.gram.delete()

    def test_save(self):
        self.gram.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 1)


class VoteTest(TestCase):
    def setUp(self):
        self.user = User(username='Keller Njoroge', email='keller@kell.com', password='passwadd')
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.gram = Project(projectname='Keller_Insta', overview='A clone of Instagram',
                            profile=self.user, url='Keller_insta.com')
        self.vetting = Vote(designvote=1, usabilityvote=6, creativityvote=7,
                            contentvote=8, voter=self.user, project=self.gram)

    def tearDown(self):
        Profile.objects.all().delete()
        self.vetting.delete()
        self.gram.delete()

    def test_save_vote(self):
        self.vetting.save_vote()
        votes = Vote.objects.all()
        self.assertTrue(len(votes) == 1)
