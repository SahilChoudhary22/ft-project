from rest_framework import serializers, fields
from profiles_api.models import UserProfile, ActivityPeriod
from profiles_api.constants import DATE_FORMAT
import json

class GetActivityPeriods(serializers.ModelSerializer):
    """ Serializer that serializes the activity periods"""
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')
    
    def get_start_time(self, obj):
        #pro = obj.start_time.strftime(DATE_FORMAT)
        return json.dumps(obj.start_time, indent=2, sort_keys=True, default=str)
    
    def get_end_time(self, obj):
        #con = obj.end_time.strftime(DATE_FORMAT)
        return json.dumps(obj.end_time, indent=4, sort_keys=True, default=str)


class GetUserActivitySerializer(serializers.ModelSerializer):
    real_name = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('id', 'real_name', 'tz', 'activity_periods')
        extra_kwargs = { 
            'tz': {
                'read_only': True,
            }
        }
    def get_real_name(self, obj):
        return obj.name
    
    def get_activity_periods(self, obj):
        activities = ActivityPeriod.objects.filter(user=obj).all().order_by('start_time')
        return GetActivityPeriods(activities, many=True).data
    
    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('activity_periods')
        activity = ActivityPeriod.objects.create(**user_data)
        user = UserProfile.objects.create(activity=activity, **validated_data)
        return user

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'tz')


class CreateActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time', 'user')


class GetUserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'tz')


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta: # define our serializer
        model = UserProfile # the model to serialize
        fields = ('id', 'email', 'name', 'tz', 'password') # the fields we want to make accessible
        extra_kwargs = { 
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        } ## made password write only, so it doesnt get returned on get request
    
    def create(self, validated_data):
        """Create and return a new user"""
        ## overriding default create

        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password=validated_data['password']
        )

        return user