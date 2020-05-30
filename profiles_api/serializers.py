from rest_framework import serializers
from profiles_api.models import UserProfile, ActivityPeriod
from profiles_api.constants import DATE_FORMAT

class GetActivityPeriods(serializers.ModelSerializer):
    """ Serializer that serializes the activity periods"""
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')
    
    def get_start_time(self, obj):
        return obj.start_time.strftime(DATE_FORMAT)
    
    def get_end_time(self, obj):
        return obj.end_time.strftime(DATE_FORMAT)


class GetUserActivitySerializer(serializers.ModelSerializer):
    real_name = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ('id', 'real_name', 'tz', 'activity_periods')
    
    def get_real_name(self, obj):
        return obj.name
    
    def get_activity_periods(self, obj):
        activities = ActivityPeriod.objects.filter(user=obj).all().order_by('start_time')
        return GetActivityPeriods(activities, many=True).data

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