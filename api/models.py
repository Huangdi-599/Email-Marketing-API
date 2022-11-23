from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL ##Authenticated User

# Create your models here.
class Lists (models.Model):
    user = models.ForeignKey(User,  default = 1 ,null = True,  on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)

class EmailContact(models.Model):
    user = models.ForeignKey(User,  default = 1 ,null = True,  on_delete=models.SET_NULL)
    email= models.EmailField(max_length=254)
    lists = models.ManyToManyField(Lists)
    reg_date = models.DateTimeField(auto_now_add=True)


