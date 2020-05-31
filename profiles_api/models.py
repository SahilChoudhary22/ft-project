import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager 

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user Profile"""
        if not email:
            raise ValueError("Users must have an email address")

        # Data manipulation and setting
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
    
        # saving
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with the given details"""
        user = self.create_user(email, name, password)

        # giving superuser privileges
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Implementing custom user model.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Inheriting AbstractBaseUser to restate our minimum requirements"""
    email = models.EmailField(max_length=255, unique=True) ## email field
    name = models.CharField(max_length=255) ## name field
    is_activate = models.BooleanField(default=True) # is activated (used for acc deletion etc.)
    is_staff = models.BooleanField(default=False) # if the user is admin, give access to special locations
    tz = models.CharField(max_length=50) # kept it as CharField to supply dummy data easily in the given time limit

    objects = UserProfileManager() # user profile manager for django CLI

    USERNAME_FIELD = 'email' # Overriding the django username auth with email auth
    REQUIRED_FIELDS = ['name'] # make name mandatory

    # dunder method to customize model representation in the admin panel
    def __str__(self):
        return self.name


class ActivityPeriod(models.Model):
    """Activity Period model to track user's activity"""
    #receiving user object, related_name to link the nested serializer
    user = models.ForeignKey(UserProfile, related_name = "activity_periods", on_delete=models.CASCADE)
    # start_time and end_time
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.user.name + "'s Activity Period"