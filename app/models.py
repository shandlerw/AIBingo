from django.db import models
from django.db import models
import re
from datetime import datetime
import bcrypt
from django.db.models.fields import EmailField, IntegerField, related

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
