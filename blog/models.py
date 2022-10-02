from pickle import TRUE
from random import choices
from tabnanny import verbose
from tkinter import ACTIVE
from turtle import title
from unicodedata import category
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
        
    
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS =(
        (ACTIVE, 'Active'),
        (DRAFT, 'DRAFT')
    )
    category = models.ForeignKey(Category, related_name ='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100, choices = CHOICES_STATUS, default = ACTIVE)
    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name