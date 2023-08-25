from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('El usuario debe de contener un correo electronico')
        user = self.model(
            email = self.normalize_email(email=email),
            username = username
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username = username,
            password=password,
        )

        user.user_admin = True
        user.save()
        return user



class MyUser(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', max_length=50, unique=True)
    email = models.EmailField('Correo electronico', max_length=50, unique=True)
    name = models.CharField('Nombre', max_length=50, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    image = models.ImageField('Imagen de perfil', upload_to='media/', blank=True, null=True)

    user_active = models.BooleanField(default=True)
    user_admin = models.BooleanField(default=False)
    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username}"
    
    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    def is_staff(self):
        return self.user_admin
    