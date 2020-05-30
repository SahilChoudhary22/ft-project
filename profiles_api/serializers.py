from rest_framework import serializers
from profiles_api.models import User, ActivityPeriod



class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a user object"""
    #activity_periods = ActivityPeriodSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
    

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes activity object"""
    members = UserSerializer(many=True, read_only=True)
    # activityList = ActivityPeriod.objects.get(user__iexact='user')
    class Meta:
        model = ActivityPeriod
        fields = '__all__'
        depth = 1

# class RepliesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Replies
#         fields = ('id', 'content', 'parent_id', 'likes')
#     parent_id = serializers.Field(source='comment.parent_id')

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'parent_id', 'content', 'likes', 'replies')
#     replies = RepliesSerializer(many=True)