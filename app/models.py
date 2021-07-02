from django.db import models
from django.db import models
import re
from datetime import datetime
import bcrypt
from django.db.models.fields import EmailField, IntegerField, related

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Character(models.Model):
    name = models.CharField(max_length=15)
    affiliation = models.CharField(max_length=15)
    char_pic = models.CharField (max_length=50)
    char_desc = models.CharField (max_length=250)
    char_quotes = models.CharField (max_length= 125)
    
#git test
