from rest_framework import serializers
from Post.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        models = Article
        fields = "__all__"