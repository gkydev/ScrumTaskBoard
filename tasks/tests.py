from django.test import TestCase
from .models import Status, TechExpert
from django.test import Client
# Create your tests here.

# Model Tests

class StatusTest(TestCase):

    def create_status(self, status_title="test title"):
        return Status.objects.create(status_title=status_title)

    def test_create_status(self):
        s = self.create_status()
        self.assertTrue(isinstance(s, Status))
        self.assertEqual(s.__unicode__(), s.status_title)

class TechExpertTest(TestCase):

    def create_expert(self, expert_name="test name"):
        return TechExpert.objects.create(expert_name=expert_name)

    def test_create_expert(self):
        e = self.create_expert()
        self.assertTrue(isinstance(e, TechExpert))
        self.assertEqual(e.__unicode__(), e.expert_name)

class RedirectTest(TestCase):
    def redirect_test(self):
        c = Client()
        res = c.get('/home')
        # Login değilse yönlendiriyo demektir
        self.assertEqual(res.status_code, 302)