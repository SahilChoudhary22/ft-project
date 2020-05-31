import datetime
import random
from faker import Faker
from django.core.management.base import BaseCommand
import uuid
from profiles_api.models import UserProfile, ActivityPeriod


class Command(BaseCommand):
    help = "Save randomly generated values to the model fields."

    

    def add_arguments(self, parser):
        """ CLI commands for amazing UX"""
        parser.add_argument(
            '--delete-existing',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Delete existing stock records before generating new ones',
        )

    def handle(self, *args, **options):
        """function that populates the database"""
        timezones = ['Asia/Kolkata', 'US/Texas', 'Australia', 'Russia', 'China', 'SEA', 'JPR']
        fake = Faker()
        records = []
        activities = []
        for _ in range(20):
            kwargs = {
                'id': random.randint(1, 99999),
                'name': fake.name(),
                'email': fake.email(),
                'tz': fake.word(ext_word_list=timezones)
            }
            name_to_fill = kwargs['id']
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
            
            record = UserProfile(**kwargs)
            actRecord = ActivityPeriod(**kwargsact)
            actRecord2 = ActivityPeriod(**kwargsact2)
            actRecord3 = ActivityPeriod(**kwargsact3)


            records.append(record)            
            activities.append(actRecord)
            activities.append(actRecord2)
            activities.append(actRecord3)
        
        if options["delete_existing"]:
            UserProfile.objects.all().delete()
            ActivityPeriod.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing User Profiles and Activity records deleted.'))
        UserProfile.objects.bulk_create(records)
        ActivityPeriod.objects.bulk_create(activities)
        self.stdout.write(self.style.SUCCESS('User Profiles saved successfully.'))
        self.stdout.write(self.style.SUCCESS('Random Activity record added.'))