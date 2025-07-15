from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())
    def test_form_is_invalid(self):
        comment_form = CommentForm({'boy': 'good post'})
        self.assertFalse(comment_form.is_valid(), msg= "Form should be invalid due to missing 'body' field")
