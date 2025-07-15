from django.test import TestCase
from .forms import CollaborateForm
from .models import AboutSection, CollaborateRequest
from django.urls import reverse



class TestAboutView(TestCase):

    def setUp(self):
        self.about_section = AboutSection.objects.create(
            title="Test Section",
            profile_image="test_image.jpg",
            content="This is a test content."
        )
        self.about_section.save()
        

    def test_about_section_and_collaborate_form_valid(self):
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.about_section.title)
        self.assertContains(response, self.about_section.content)
        self.assertIsInstance(response.context['form'], CollaborateForm)

    def test_successful_collaborate_submission(self):
        post_data = {
            'name': 'Test User',
            'email': 'andrew@yahoo.com',
            'message': 'This is a test collaborate.'
        }
        response = self.client.post(reverse(
            'about:about'), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Your collaboration request has been submitted!",
            response.content
        )