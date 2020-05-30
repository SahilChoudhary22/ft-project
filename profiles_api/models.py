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

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)


        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with the given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Implementing custom user model.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    #TODO - Overriding the inbuilt id to match the pattern of given JSON
    email = models.EmailField(max_length=255, unique=True) ## email field
    name = models.CharField(max_length=255) ## name field
    is_activate = models.BooleanField(default=True) ## is activated (used for acc deletion etc.)
    is_staff = models.BooleanField(default=False) # if the user is admin, give access to special locations
    # todo - use timezone field
    tz = models.CharField(max_length=50)

    objects = UserProfileManager() # we'll create a manager for django CLI ease

    USERNAME_FIELD = 'email' ## Overriding the django username auth with email auth
    REQUIRED_FIELDS = ['name'] ## username is automatically mandatory, this makes name mandatory too

    # dunder method to customize model representation in the admin panel
    def __str__(self):
        return self.name

# Activity Period model to track user activity
class ActivityPeriod(models.Model):
    #receiving user object
    user = models.ForeignKey(UserProfile, related_name = "members" ,on_delete=models.CASCADE)
    # start_time and end_time
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # synchronizing IDs of both the models
    



## TODO - fix timezone
## Make API
## Create script to populate the DB