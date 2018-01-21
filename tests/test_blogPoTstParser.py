from unittest import TestCase

from render_page import BlogPostParser


class TestBlogPosttParser(TestCase):

    def setUp(self):
        f = open("tests/posts/a-post.md", "r")
        d = f.read()
        f.close()

        self.postParser = BlogPostParser(d, "a-post.md")

    def test_get_author(self):
        self.assertEqual("Jane Doe", self.postParser.get_author())

    def test_get_date(self):
        self.assertEqual("1th January 2018", self.postParser.get_date())

    def test_get_title(self):
        self.assertEqual("Post 1", self.postParser.get_title())

    def test_get_description(self):
        self.assertEqual("This is a test post", self.postParser.get_description())

    def test_get_image(self):
        self.assertEqual("/test/image.png", self.postParser.get_image())

    def test_get_content(self):
        self.assertEqual("Post text 1\nPost text 1\nPost text 1\n",
                          self.postParser.get_content())