from django.db import models
from django.db import models
import re
from datetime import datetime
import bcrypt
from django.db.models.fields import EmailField, IntegerField, related

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Character(models.Model):
    name = models.CharField
    affiliation = models.CharField
    char_pic = models.ImageField
    char_desc = models.CharField
    char_quotes = models.CharField
    
