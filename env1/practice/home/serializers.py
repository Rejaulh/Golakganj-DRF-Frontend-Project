from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# # created token some users by manualy
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
    def create(self, validated_data):
        user = User.objects.create(username = validated_data["username"])
        user.set_password(validated_data["username"])
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Student
        fields = "__all__"
        # fields = ["name", "age"]
        # exclude = ["id"]
        
        def validate(self,data):

            if data["age"] < 18:
                raise serializers.ValidationError({"error":"age can't be less than 18"})
            if data["name"]:
                for n in data["name"]:
                    if n.isdigit():
                        raise serializers.validationError({"error": "Name canot be numeric"})
            return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = "__all__"

# Admition Model Serializer
class AdmitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admition
        fields = "__all__"
        # exclude = ["id"]