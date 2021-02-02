from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    experience_name = models.CharField(max_length=100)
    playlist = models.TextField()
    color_scheme = models.TextField()
    description = models.TextField()


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    color_scheme = models.TextField()
    #color_list = models.ListTextField()
    color_count = models.IntegerField()


