from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.





class Product(models.Model):


    STATUS_CHOICES = [
        ('draft','Draft'),
        ('published','Published')

    ]



    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title  = models.CharField(max_length=255)
    slug  = models.SlugField(blank=True)
    image = models.ImageField()
    count = models.IntegerField(default=0)
    description  = models.TextField()
    price  = models.DecimalField(max_digits=9,decimal_places=2)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')



    class Meta:
        ordering = ['-created']
        verbose_name_plural  = "Posts"



    def get_absolute_url(self):
        return reverse('shop:detail',kwargs={'slug':self.slug})



    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product,self).save(*args,**kwargs)



    
class Comment (models.Model):
    product = models.ForeignKey(Product,related_name='comments',on_delete=models.CASCADE,null=True)
    name    = models.CharField(max_length=255,blank=True)
    email   = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-created']



    def __str__(self):
        return f'Comment by {self.name} on {self.product}'


    