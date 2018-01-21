#
# Copyright (c) 2017 Ognjen Galić
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE

import codecs
import os
import shutil

from typing import List
from jinja2 import Environment, FileSystemLoader
from markdown import markdown


class BlogPostParser:
    """
    This class represents a blog post
    """

    class BlogPostParserException(Exception):
        pass

    def __init__(self, post: str, file):
        self.file = file
        self.post = post
        self.lines = post.split("\n")

    def get_author(self):
        """
        Get the author of the post
        :return: the author
        """
        return self.__return_filter("Written-by:")

    def get_date(self):
        """
        Get the date of the post
        :return: the date of the post
        """
        return self.__return_filter("Posted-on:")

    def get_title(self):
        """
        Get the title of the post
        :return: the title of the post
        """
        if len(self.lines) < 1:
            raise BlogPostParser.BlogPostParserException("Failed to get title!")
        return self.lines[0].replace("#", "").strip()

    def get_content(self):
        """
        Get the content of the post
        :return: the post content
        """
        split = self.post.split("---")
        if len(split) < 1:
            raise BlogPostParser.BlogPostParserException("Malformed post!")
        split = split[0].split("\n")
        if len(split) < 1:
            raise BlogPostParser.BlogPostParserException("Post content has no lines!")
        ret = ""
        for line in split[1:]:
            if line == "":
                continue
            ret += line + "\n"
        return ret

    def get_description(self):
        """
        Get the post description
        :return: the description of the post
        """
        return self.__return_filter("Short-description:")

    def __return_filter(self, needle: str):
        """
        Filter the post text and find needle, strip it and return
        :param needle: the needle to find
        :return: the stripped text
        """
        for line in self.lines:
            if needle in line:
                return line.replace(needle, "").strip()
        raise BlogPostParser.BlogPostParserException("Needle not found: " + needle)

    def get_image(self):
        """
        Get the image of the post
        :return: the image URL or none if no image
        """
        try:
            return self.__return_filter("Image:")
        except BlogPostParser.BlogPostParserException:
            return None

    def get_file(self):
        """
        Get the source file of the post
        :return: the source file
        """
        return self.file.replace(".md", "")

    def get_content_html(self):
        return markdown(self.get_content(), extensions=["markdown.extensions.nl2br"])

class BlogPostFetcher:
    """
    This class fetches all posts from some path
    """

    def __init__(self, path: str):
        """
        Initialize the fetcher to feth from path
        :param path: the path to fetch from
        """
        if not os.path.exists(path):
            raise FileNotFoundError("{}: not found".format(path))
        self.path = path

    def get_posts(self) -> List[BlogPostParser]:
        """
        Fetch all posts from the path
        :return: a list of posts
        """
        ret = []
        for file in os.listdir(self.path):
            if not file.endswith(".md"):
                continue
            with codecs.open(self.path + file, mode="r", encoding="utf-8") as text:
                data = text.read()
                post = BlogPostParser(data, file)
                ret.append(post)
        return ret


class Renderer:
    """
    This defines a generic HTML renderer
    """

    def __init__(self, env: Environment):
        self.env = env

    def render(self):
        pass


class SingleBlogPostRenderer(Renderer):
    """
    This renders a single post
    """

    def __init__(self, env: Environment, post: BlogPostParser):
        super().__init__(env)
        self.template = env.get_template("post.html")
        self.post = post

    def render(self):
        return self.template.render(post=self.post)


class BlogIndexRenderer(Renderer):
    """
    This renders the blog index
    """

    def __init__(self, env: Environment, posts: List[BlogPostParser]):
        self.posts = posts
        self.template = env.get_template("post_index.html")
        super().__init__(env)

    def render(self):
        return self.template.render(posts=self.posts)

class MarkdownRenderer(Renderer):
    """
    This renders a markdown file into HTML
    """

    def __init__(self, env: Environment, file: str, title: str):
        super().__init__(env)
        self.env = env
        self.file = file
        self.title = title
        self.template = env.get_template("md.html")

    def render(self):
        with codecs.open("model/{}".format(self.file), mode="r", encoding="utf-8") as file:
            data = file.read()
            text =  markdown(data, extensions=["markdown.extensions.nl2br"])
            return self.template.render(text=text, title=self.title)

class ProjectsPageGenerator(Renderer):
    """
    This renders a individual project page
    """

    def __init__(self, env: Environment, project: str):
        super().__init__(env)
        self.md = MarkdownRenderer(env, file="projects/{}.md".format(project),
                                   title="{} Documentation - ThinkPads.org".format(project))

    def render(self):
        return self.md.render()

class FRUPageRenderer(Renderer):
    """
    This renders the FRU page
    """

    def __init__(self, env: Environment):
        super().__init__(env)
        self.template = env.get_template("fru.html")

    def render(self):
        return self.template.render()


class PageGenerator:
    """
    This is the main runtime generator
    """

    def __init__(self, env: Environment):
        print("Regenerating ThinkPads.org\n")
        self.env = env
        
    def start(self):
        self.clear()
        self.generate_blog_posts()
        self.generate_blog_index()
        self.generate_index()
        self.generate_repositories()
        self.generate_about()
        self.generate_projects()
        self.generate_projects_index()
        self.generate_fru()

    def generate_blog_posts(self):
        """
        This generates all the posts in blog/posts
        :return: None
        """
        print("Generating posts")
        fetcher = BlogPostFetcher("model/posts/")
        posts = fetcher.get_posts()
        for post in posts:
            print("Generating {}".format(post.get_file()))
            os.mkdir("blog/{}".format(post.get_file()))
            renderer = SingleBlogPostRenderer(self.env, post)
            with codecs.open("blog/{}/index.html".format(post.get_file()),
                             mode="w", encoding="utf-8") as file:
                file.write(renderer.render())
        print()

    def generate_blog_index(self):
        """
        This generates the blog index
        :return: None
        """
        print("Generating index")
        fetcher = BlogPostFetcher("model/posts/")
        posts = fetcher.get_posts()
        with open("blog/index.html", "w") as file:
            renderer = BlogIndexRenderer(self.env, fetcher.get_posts())
            file.write(renderer.render())

    def generate_index(self):
        """
        This generates the main index
        :return: None
        """
        print("Generating home page")
        renderer = MarkdownRenderer(self.env, "news.md", "Home - ThinkPads.org")
        with codecs.open("index.html", mode="w", encoding="utf-8") as file:
            file.write(renderer.render())

    def clear(self):
        """
        This clears all the generated data
        :return: None
        """
        try:
            print("Clearing posts")
            shutil.rmtree("blog/")
            os.mkdir("blog/")
            print("Clearing homepage")
            os.remove("index.html")
            print("Clearing projects")
            shutil.rmtree("projects/")
            print("Clearing repositories")
            os.remove("repositories/index.html")
            print("Clearing about")
            os.remove("about/index.html")
            print("Clearing FRU")
            os.remove("fru/index.html")
        except FileNotFoundError as e:
            print("*** WARN: {}".format(str(e)))
        print()

    def generate_repositories(self):
        """
        This generates the main index
        :return: None
        """
        print("Generating repository page")
        renderer = MarkdownRenderer(self.env, "repositories.md",
                                    "Software Repositories - ThinkPads.org")
        with codecs.open("repositories/index.html", mode="w", encoding="utf-8") as file:
            file.write(renderer.render())

    def generate_about(self):
        """
        This generates the "About" page
        :return:
        """
        print("Generating about")
        renderer = MarkdownRenderer(self.env, "about.md",
                                    "About us - ThinkPads.org")
        with codecs.open("about/index.html", mode="w",
                         encoding="utf-8") as file:
            file.write(renderer.render())

    def generate_projects(self):
        """
        This generates the project child pages
        :return: None
        """
        print()
        os.mkdir("projects")
        print("Generating projects")
        for project in os.listdir("model/projects/"):
            project = project.replace(".md", "")
            print("Generating " + project)
            generator = ProjectsPageGenerator(self.env, project)
            os.mkdir("projects/{}".format(project))
            with codecs.open("projects/{}/index.html".format(project), "w") as file:
                file.write(generator.render())
        print()

    def generate_projects_index(self):
        """
        This generates the project index
        :return:
        """
        print("Generating project index")
        renderer = MarkdownRenderer(self.env, "projects.md", "Projects - ThinkPads.org")
        with codecs.open("projects/index.html", mode="w", encoding="utf-8") as file:
            file.write(renderer.render())

    def generate_fru(self):
        """
        This generates the FRU page
        :return:
        """
        print("Generating FRU page")
        renderer = FRUPageRenderer(self.env)
        with codecs.open("fru/index.html", mode="w", encoding="utf-8") as file:
            file.write(renderer.render())


def main():

    env = Environment(
        loader=FileSystemLoader("templates", followlinks=True),
    )

    generator = PageGenerator(env)
    generator.start()

if __name__=="__main__":
    main()