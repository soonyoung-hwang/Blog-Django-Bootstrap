from django.test import TestCase, Client
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from blog.models import Post


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_trump = User.objects.create_user(
            username="Trump", password="somepassword"
        )

    def test_landing(self):
        # create posts
        post_001 = Post.objects.create(
            title="첫 번째 포스트입니다.",
            content="Hello World. We are the one. Thanks",
            author=self.user_trump,
        )
        post_002 = Post.objects.create(
            title="두 번째 포스트입니다.",
            content="결과야 빨리 나와라... 시험아 겹치지 마라...",
            author=self.user_trump,
        )
        post_003 = Post.objects.create(
            title="세 번째 포스트입니다.",
            content="벌써 세번째 포스트네요.",
            author=self.user_trump,
        )
        post_004 = Post.objects.create(
            title="네 번째 포스트입니다.",
            content="네 번째 포스트입니다.",
            author=self.user_trump,
        )
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, "html.parser")

        body = soup.body
        self.assertNotIn(post_001.title, body.text)
        self.assertIn(post_002.title, body.text)
        self.assertIn(post_003.title, body.text)
        self.assertIn(post_004.title, body.text)
