import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 


# Implementing custom user model.
class User(AbstractUser):
    # Overriding the inbuilt id to match the pattern of given JSON
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # todo - use timezone field
    tz = models.CharField(max_length=50)

    # dunder method to customize model representation in the admin panel
    def __str__(self):
        return self.first_name + " " + self.last_name

    # To access from API to get full name
    def real_name(self):
        return first_name + " " + last_name

# Activity Period model to track user activity
class ActivityPeriod(models.Model):
    #receiving user object
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # start_time and end_time
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # synchronizing IDs of both the models
    def id(self):
        return user.id



## TODO - fix timezone
## Make API
## Create script to populate the DB