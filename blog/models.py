from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


NEWS_CATEGORY = (
    ('Fashion', 'Fashion'),
    ('Gadgets', 'Gadgets'),
    ('Lifestyle', 'Lifestyle'),
)

STATUS_CATEGORY = (
    ('home', 'home'),
    ('blog', 'blog'),
)

POSITION_CATEGORY = (
    ("dm", "don't miss"),
    ("wt", "what's tranding"),
)

FUTURE_EVENTS = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=2, choices=POSITION_CATEGORY)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.name}-{self.name}'


class BlogNews(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    tag = models.ManyToManyField(Tag)
    category = models.CharField(
        max_length=10, choices=NEWS_CATEGORY, default='Fashion')
    events = models.CharField(
        max_length=10, choices=FUTURE_EVENTS, default="No")
    status = models.CharField(
        max_length=20, choices=STATUS_CATEGORY, default='blog')
    position = models.CharField(
        max_length=2, choices=POSITION_CATEGORY, default='dm')
    body = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = "Blog New"
        verbose_name_plural = "Blog News"

    def __str__(self):
        return self.name

    def imageUrl(self):
        try:
            image = self.image.url
        except:
            image = ""
        return image


class Advertising(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    link = models.URLField()
    perc = models.IntegerField()

    def imageUrl(self):
        try:
            image = self.image.url
        except:
            image = ""
        return image


class BlogVideo(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    view = models.IntegerField(default=1)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField()
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    comments = GenericRelation(Comment)

    def imageUrl(self):
        try:
            image = self.image.url
        except:
            image = ""
        return image

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
