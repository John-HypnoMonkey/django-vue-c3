from rest_framework import serializers


class PostSnapshotSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    likes = serializers.IntegerField()
    reposts = serializers.IntegerField()
    comments = serializers.IntegerField()
