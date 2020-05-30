import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 


# Implementing custom user model.
class User(AbstractUser):
    # Overriding the inbuilt id to match the pattern of given JSON
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # real_name = first_name + " " + last_name
    # todo - use timezone field
    tz = models.CharField(max_length=50)
    # dunder method to customize model representation in the admin panel
    def __str__(self):
        if self.first_name:
            return self.first_name + " " + self.last_name
        else:
            return self.username

    # To access from API to get full name
    def real_name(self):
        return self.first_name + " " + self.last_name

# Activity Period model to track user activity
class ActivityPeriod(models.Model):
    #receiving user object
    user = models.ForeignKey(User, related_name = "members" ,on_delete=models.CASCADE)
    # start_time and end_time
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # synchronizing IDs of both the models
    # def id(self):
    #     return user.id
    
    # def tz(self):
    #     return user.tz
    
    



## TODO - fix timezone
## Make API
## Create script to populate the DB