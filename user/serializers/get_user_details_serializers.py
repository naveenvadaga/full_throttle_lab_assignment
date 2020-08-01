from rest_framework import serializers


class UserActivityPeriodSerializer(
        serializers.Serializer):
    start_time = serializers.CharField(
        max_length=100)
    end_time = serializers.CharField(
        max_length=100)


class UserDetailsSerializer(
        serializers.Serializer):
    id = serializers.CharField(max_length=100)
    real_name = serializers.CharField(
        max_length=150)
    tz = serializers.CharField(max_length=200)
    activity_periods = UserActivityPeriodSerializer(
        many=True)
