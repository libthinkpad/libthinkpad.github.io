from unittest import TestCase

from render_page import BlogPostFetcher


class TestBlogPostFetcher(TestCase):

    def setUp(self):
        self.fetcher = BlogPostFetcher("tests/posts/")

    def test_get_posts(self):
        posts = self.fetcher.get_posts()

        self.assertEqual(2, len(posts))