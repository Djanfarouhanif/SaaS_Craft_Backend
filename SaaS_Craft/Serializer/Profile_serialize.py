from rest_framework import serialisers
from .models import Profile

class ProfileSerialiser(serialisers.ModelSerialiser):
    class Meta:
        models = Profile
        fields = "__all__"