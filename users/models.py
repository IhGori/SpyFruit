from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.html import escape, mark_safe
from django.conf import settings
import uuid
# Create your models here.

class User(AbstractUser):

    
    profile_pic = models.ImageField(upload_to="profile_pictures/", null=True, blank=True, default='profile_pictures/avatardefault.png')

    usuario_id = models.UUIDField(
        default= uuid.uuid4        
    )

    is_admin = models.BooleanField('Administrador', default = False)
    is_dados = models.BooleanField('Dados', default = False)

    

  
    

