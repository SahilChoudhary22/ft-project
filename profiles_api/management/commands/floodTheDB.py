import datetime
import random
from faker import Faker
from django.core.management.base import BaseCommand
import uuid
from profiles_api.models import UserProfile, ActivityPeriod


class Command(BaseCommand):
    help = "Create dummy users and their activity periods."

    def add_arguments(self, parser):
        """ CLI commands for amazing UX"""
        parser.add_argument(
            '--delete-existing',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Delete Users and their activities before generating new ones',
        )

    def handle(self, *args, **options):
        """function that populates the database"""
        
        timezones = ['Asia/Kolkata', 'US/Texas', 'Australia', 'Russia', 'China', 'SEA', 'JPR']
        fake = Faker() # Faker module
        records = [] # to handle users
        activities = [] # to handle activity_periods
        
        # generate users
        for _ in range(20):
            kwargs = {
                'id': random.randint(1, 99999),
                'name': fake.name(),
                'email': fake.email(),
                'tz': fake.word(ext_word_list=timezones)
            }
            name_to_fill = kwargs['id']
            # generate start time and end time for the generated user
            for _ in range(3):
                kwargsact = {
                    'user': UserProfile(name_to_fill),
                    'start_time': fake.date_time_this_decade(),
                    'end_time': fake.date_time_this_decade()
                }
                kwargsact2 = {
                    'user': UserProfile(name_to_fill),
                    'start_time': fake.date_time_this_decade(),
                    'end_time': fake.date_time_this_decade()
                }
                kwargsact3 = {
                    'user': UserProfile(name_to_fill),
                    'start_time': fake.date_time_this_decade(),
                    'end_time': fake.date_time_this_decade()
                }
            
            # Instantiator
            record = UserProfile(**kwargs)
            actRecord = ActivityPeriod(**kwargsact)
            actRecord2 = ActivityPeriod(**kwargsact2)
            actRecord3 = ActivityPeriod(**kwargsact3)

            # Appending the new objects
            records.append(record)            
            activities.append(actRecord)
            activities.append(actRecord2)
            activities.append(actRecord3)
        
        # if the user enters optional arguement '--delete-existing' 
        if options["delete_existing"]:
            UserProfile.objects.all().delete()
            ActivityPeriod.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing User Profiles and Activity records deleted.'))
        
        # Bulk creation of objects
        UserProfile.objects.bulk_create(records)
        ActivityPeriod.objects.bulk_create(activities)
        # Output on successful operation
        self.stdout.write(self.style.SUCCESS('User Profiles saved successfully.'))
        self.stdout.write(self.style.SUCCESS('Random Activity record added.'))