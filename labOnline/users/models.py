from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Usuário', max_length=30, unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail')
    #is_staff = models.BooleanField('Equipe', default=False)
    #is_active = models.BooleanField('Ativo', default=True)
    #is_student = models.BooleanField(default=False)
    #is_teacher = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
  
		
    def __str__(self):
	    return self.name or self.username

    def get_absolute_url(self):
	    return reverse('core:index')

    class Meta:
	    verbose_name = 'Usuário'
	    verbose_name_plural = 'Usuários'
	    ordering = ['id']