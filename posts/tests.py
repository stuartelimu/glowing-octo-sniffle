from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):

    def setUp(self):
        Post.objects.create(text='Hello, world!')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Hello, world!')

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, world!')
        self.assertTemplateUsed(response, 'post_list.html')
