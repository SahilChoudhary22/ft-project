from rest_framework import serializers, fields
from profiles_api.models import UserProfile, ActivityPeriod
import json


class GetActivityPeriods(serializers.ModelSerializer):
    """ Serializer that serializes the activity periods"""
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')
    
    def get_start_time(self, obj):
        """Had to use this way of conversion because of strftime and strptime issues in windows OS."""
        stime = json.dumps(obj.start_time, indent=2, sort_keys=True, default=str)[1:20]
        return stime
    
    def get_end_time(self, obj):
        return json.dumps(obj.end_time, indent=4, sort_keys=True, default=str)


class GetUserActivitySerializer(serializers.ModelSerializer):
    """ 
    The serializer which aggregates every requirement of the test
    viz. users and their activities.
    """
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
    
    # retrieves value for SerialMethodField
    def get_real_name(self, obj):
        return obj.name
    
    def get_activity_periods(self, obj):
        activities = ActivityPeriod.objects.filter(user=obj).all().order_by('start_time')
        return GetActivityPeriods(activities, many=True).data


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