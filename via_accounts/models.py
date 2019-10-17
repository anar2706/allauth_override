from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Countries = {

    ('TR','Turkey'),
    ('AZE','Azerbaijan'),
    ('IRA','Iran'),
    ('USA','USA')




}




class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=70,choices=Countries)
    created  = models.DateTimeField(auto_now_add=True)
    phone    = models.CharField(verbose_name='Phone Number',max_length=255)


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-created']