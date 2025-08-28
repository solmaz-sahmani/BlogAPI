from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'solmaz',
            email = 'solmaz.sahmani@gmail.com',
            password = 'secret'
        )
        
        cls.post = Post.objects.create(
            author = cls.user,
            title = 'this is a title',
            bocy = 'body content'
        )    
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'solmaz')
        self.assertEqual(self.post.title,'this is a title')
        self.assertEqual(self.post.body, 'body content')
        self.assertEqual(str(self.post), 'this is a title')
        