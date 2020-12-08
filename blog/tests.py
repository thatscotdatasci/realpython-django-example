import datetime
from typing import Union, List

from django.test import TestCase
from django.urls import reverse

from .models import Post, Category, Comment

# Create your tests here.


def create_category(name: str = "Category") -> Category:
    category = Category(name=name)
    category.save()
    return category


def create_post(title: str = "Post Title", body="Post Body", categories: Union[None, List] = None) -> Post:
    if categories is None:
        categories = [create_category()]

    post = Post(title=title, body=body)
    post.save()
    post.categories.set(categories)
    return post


def create_comment(author: str = "J Bloggs", body:str = "Comment body", post: Post = create_post()) -> Comment:
    comment = Comment(author=author, body=body, post=post)
    comment.save()
    return comment


class BlogIndexViewTests(TestCase):

    def test_posts_list(self):
        for _ in range(2):
            create_post()
        p = create_post()
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context.get("category"))
        self.assertQuerysetEqual(response.context["post_list"], [p.title]*3, transform=str)

    def test_post_ordering(self):
        p_old = create_post(title="Old Post")
        p_old.created_on -= datetime.timedelta(days=1)
        p_old.save()

        p_new = create_post(title="New Post")

        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context.get("category"))
        self.assertQuerysetEqual(response.context["post_list"], [p_new.title, p_old.title], transform=str)
        self.assertTrue(response.context["post_list"][0].created_on > response.context["post_list"][1].created_on)
        self.assertAlmostEqual(
            (response.context["post_list"][0].created_on - datetime.timedelta(days=1)).timestamp(),
            response.context["post_list"][1].created_on.timestamp(),
            delta=10
        )


class BlobCategoryViewTests(TestCase):

    def test_posts_list(self):
        cat_1 = create_category("cat_1")
        cat_2 = create_category("cat_2")
        for cat in (cat_1, cat_2):
            for _ in range(3):
                create_post(title=cat.name, categories=[cat])
        response = self.client.get(reverse("blog:category", args=(cat_1.name,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category"], cat_1.name)
        self.assertQuerysetEqual(response.context["post_list"], [cat_1.name]*3, transform=str)

    def test_post_ordering(self):
        cat_1 = create_category("cat_1")
        cat_2 = create_category("cat_2")

        create_post(categories=[cat_2])

        p_old = create_post(title="Old Post", categories=[cat_1])
        p_old.created_on -= datetime.timedelta(days=1)
        p_old.save()

        p_new = create_post(title="New Post", categories=[cat_1])

        response = self.client.get(reverse("blog:category", args=(cat_1.name,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category"], cat_1.name)
        self.assertQuerysetEqual(response.context["post_list"], [p_new.title, p_old.title], transform=str)
        self.assertTrue(response.context["post_list"][0].created_on > response.context["post_list"][1].created_on)
        self.assertAlmostEqual(
            (response.context["post_list"][0].created_on - datetime.timedelta(days=1)).timestamp(),
            response.context["post_list"][1].created_on.timestamp(),
            delta=10
        )


class BlogDetailViewTest(TestCase):

    def test_content(self):
        post = create_post(title="Post Title", body="This is my post content")
        response = self.client.get(reverse("blog:detail", args=(post.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["post"].title, post.title)
        self.assertEqual(response.context["post"].body, post.body)

    def test_no_comments(self):
        post = create_post()
        response = self.client.get(reverse("blog:detail", args=(post.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No comments yet!")
        self.assertQuerysetEqual(response.context["comments"], [])

    def test_retrieve_comment(self):
        post = create_post()
        comment = create_comment(author="J Bloggs", body="Comment body", post=post)
        response = self.client.get(reverse("blog:detail", args=(post.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["comments"], [f"{comment.post} - {comment.author} - {comment.created_on}"],
            transform=str
        )

    def test_post_comment(self):
        post = create_post()

        comment_author = "J Blogs"
        comment_body = "This is the body"
        new_comment = {"author": comment_author, "body": comment_body}

        response = self.client.post(reverse("blog:detail", args=(post.pk,)), data=new_comment)
        self.assertEqual(response.status_code, 302)

        comments = Post.objects.get(pk=post.pk).comments.all()
        self.assertEqual(len(comments), 1)

        comment = comments[0]
        self.assertEqual(comment.author, comment_author)
        self.assertEqual(comment.body, comment_body)
        self.assertAlmostEqual(comment.created_on.timestamp(), datetime.datetime.now().timestamp(), delta=100)
