from django.contrib import admin
from profiles_api import models

# Registering both the models of the app
class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tz')


admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.ActivityPeriod, ActivityPeriodAdmin)

# Modify Admin Panel Header
admin.site.site_header = "FT Labs Admin Panel"