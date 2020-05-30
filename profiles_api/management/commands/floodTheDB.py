import datetime
import random
from faker import Faker
from django.core.management.base import BaseCommand

from profiles_api.models import UserProfile, ActivityPeriod



class Command(BaseCommand):
    help = "Save randomly generated values to the model fields."

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete-existing',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Delete existing stock records before generating new ones',
        )
    # def get_date(self):
    #     # Naively generating a random date
    #     day = random.randint(1, 28)
    #     month = random.randint(1, 12)
    #     year = random.randint(2014, 2017)
    #     return datetime.date(year, month, day)

    def handle(self, *args, **options):
        fake = Faker()
        records = []
        activities = []
        for _ in range(20):
            kwargs = {
                'id': fake.random_int(),
                'name': fake.name(),
                'email': fake.email(),
                'tz': fake.word()
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
            record = UserProfile(**kwargs)
            actRecord = ActivityPeriod(**kwargsact)
            actRecord2 = ActivityPeriod(**kwargsact)
            records.append(record)            
            activities.append(actRecord)
            activities.append(actRecord2)
        if options["delete_existing"]:
            UserProfile.objects.all().delete()
            ActivityPeriod.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing User Profiles and Activity records deleted.'))
        UserProfile.objects.bulk_create(records)
        ActivityPeriod.objects.bulk_create(activities)
        self.stdout.write(self.style.SUCCESS('User Profiles saved successfully.'))
        self.stdout.write(self.style.SUCCESS('Random Activity record added.'))