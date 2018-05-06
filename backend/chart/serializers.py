from rest_framework import serializers


class PostSnapshotSerializer(serializers.Serializer):
    time = serializers.IntegerField()
    likes = serializers.IntegerField()
    reposts = serializers.IntegerField()
    comments = serializers.IntegerField()
