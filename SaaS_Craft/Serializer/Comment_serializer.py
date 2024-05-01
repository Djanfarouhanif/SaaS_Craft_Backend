from rest_framework import serializers
from Post.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = "__all__"