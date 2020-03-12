from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(default="")
    books = models.ManyToManyField(Book, related_name="authors")
