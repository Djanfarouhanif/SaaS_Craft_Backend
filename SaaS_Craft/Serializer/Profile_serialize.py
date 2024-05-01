from rest_framework import serializers
from Post.models import Profile

class ProfileSerialiser(serializers.ModelSerializer):
    class Meta:
        models = Profile
        fields = "__all__"