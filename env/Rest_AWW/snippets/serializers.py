from .models import *
# from snippets.serializers import SnippetSerializer
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        # fields = ["__all__"]
        fields = ['id', 'title', 'code', 'linenose', 'language', 'style', 'owner','highlighted']


from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all(), many=True)
    class Meta:
        model = User
        fields = ["id", "username", "snippets"]