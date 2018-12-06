from django.test import TestCase
from issues.views import *
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import resolve
from django.core.urlresolvers import reverse
from issues.models import Bug, BugComment, Feature
from django.utils import timezone


class BugsTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test")

    def test_all_bugs_access(self):
        response = self.c.get(reverse('get_all_bugs'))
        self.assertEqual(response.status_code, 302)

    def test_bug_create(self):
        response = self.c.get(reverse('new_bug'))
        self.assertEqual(response.status_code, 302)

        self.c.login(username='test', password='test')
        response = self.c.get(reverse('new_bug'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_bug_create(self):
        self.c.login(username='test', password='test')
        data = {'title': '', 'details': 'Test details'}
        response = self.c.post(reverse('new_bug'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "title",
                             "This field is required.")

    def test_valid_bug_create(self):
        self.c.login(username='test', password='test')
        data = {'details': 'Test details', 'title': 'Test title'}
        data['author'] = self.user.id
        self.assertEqual(Bug.objects.count(), 0)
        response = self.c.post(reverse('new_bug'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bug.objects.count(), 1)


class FeaturesTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test")

    def test_all_features_access(self):
        response = self.c.get(reverse('get_all_features'))
        self.assertEqual(response.status_code, 302)

    def test_feature_create(self):
        response = self.c.get(reverse('new_feature'))
        self.assertEqual(response.status_code, 302)

        self.c.login(username='test', password='test')
        response = self.c.get(reverse('new_feature'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_feature_create(self):
        self.c.login(username='test', password='test')
        data = {'title': '', 'details': 'Test details'}
        response = self.c.post(reverse('new_feature'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "title",
                             "This field is required.")
