""" Imports for blog models """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    """ Model for Posts """
    project_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    project_description = models.TextField()
    deployed_link = models.URLField(max_length=200)
    code_repository = models.URLField(max_length=200, blank=True)
    other_relevant_information = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """ To display the posts by created on in desending order """
        ordering = ['-date_posted']

    def __str__(self):
        """ To return the individual title objects as a string """
        return self.project_title

    def get_absolute_url(self):
        """Find url after user posts to the forum"""
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_title)
        return super().save(*args, **kwargs)

    def number_of_likes(self):
        """ To return the number of likes """
        return self.likes.count()


class Comment(models.Model):
    """ Model for Comments """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    your_comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ordering comments by first created """
        ordering = ["date_posted"]

    def __str__(self):
        return f"Comment {self.your_comment} by {self.name}"
