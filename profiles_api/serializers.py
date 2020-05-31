from rest_framework import serializers, fields
from profiles_api.models import UserProfile, ActivityPeriod
import json
from django.contrib.auth.validators import UnicodeUsernameValidator

class ActivityPeriodSerializer(serializers.ModelSerializer):
    """ Serializer that serializes the activity periods"""
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class GetUserActivitySerializer(serializers.ModelSerializer):
    """ 
    The serializer which aggregates every requirement of the test
    viz. users and their activities. Basically nests the ActivityPeriodSerializer
    """
    activity_periods = ActivityPeriodSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'tz', 'activity_periods')
        extra_kwargs = {
            'name': {
                'validators': [UnicodeUsernameValidator()],
            },
        }
        depth = 1


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
        } ## made password write only, so it doesnt get returned on GET request
    
    def create(self, validated_data):
        """Create and return a new user"""
        ## overriding default create

        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password=validated_data['password']
        )

        return user