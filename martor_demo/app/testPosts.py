# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="New Title", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "New Title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post Body")
