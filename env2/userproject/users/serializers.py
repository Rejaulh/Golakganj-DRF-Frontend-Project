from rest_framework import serializers
from .models import UserProfile, Sector, Worker
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     email = serializers.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already Exist")
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Login Serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user': self.user.username})
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            refresh_token = RefreshToken(self.token)
            refresh_token.blacklist()
        except Exception as e:
            self.fail('invalid_token', detail=str(e))




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'location']
        # read_only_fields = ['user']

class SectorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sector
        fields = ["id", "sector_name"]

class WorkerSerializer(serializers.ModelSerializer):
    sector = SectorSerializer()
    class Meta:
        model = Worker
        fields = "__all__"

    def validate_AWC_Code(self, value):
        """
        Check if the AWC_Code is unique and is exactly 11 digits long.
        """
        # Check if AWC_Code is exactly 11 digits
        if len(str(value)) != 11:
            raise serializers.ValidationError("AWC_Code must be exactly 11 digits long.")
        
        # Check for uniqueness when creating a new Worker
        # if self.instance is None and Worker.objects.filter(AWC_Code=value).exists():
        #     raise serializers.ValidationError("This AWC_Code already exists.")

        # Check for uniqueness when updating a Worker
        if self.instance is not None and self.instance.AWC_Code != value and Worker.objects.filter(AWC_Code=value).exists():
            raise serializers.ValidationError("This AWC_Code already exists.")

        return value

    def create(self, validated_data):
        awc_code = validated_data.get('AWC_Code')
        if Worker.objects.filter(AWC_Code = awc_code).exists():
            raise serializers.ValidationError({"AWC_Code":"This AWC Code has already Exist."})
        sector_data = validated_data.pop('sector')
        # sector, created = Sector.objects.get_or_create(**sector_data)
        try:
            sector = Sector.objects.get(**sector_data)
        except Sector.MultipleObjectsReturned:
            sector = Sector.objects.filter(**sector_data).first()  # Handle multiple sectors
        except Sector.DoesNotExist:
            sector = Sector.objects.create(**sector_data)

        worker = Worker.objects.create(sector=sector, **validated_data)
        return worker
    
    
    def update(self, instance, validated_data):
        sector_data = validated_data.pop('sector', None)
        sector = instance.sector

        instance.AWC_Code = validated_data.get('AWC_Code', instance.AWC_Code)
        instance.AWC_Name = validated_data.get('AWC_Name', instance.AWC_Name)
        instance.AWW_Name = validated_data.get('AWW_Name', instance.AWW_Name)
        instance.AWW_Phone = validated_data.get('AWW_Phone', instance.AWW_Phone)
        instance.AWH_Name = validated_data.get('AWH_Name', instance.AWH_Name)
        instance.AWH_Phone = validated_data.get('AWH_Phone', instance.AWH_Phone)
        instance.AWC_Address = validated_data.get('AWC_Address', instance.AWC_Address)
        instance.AWC_Image = validated_data.get('AWC_Image', instance.AWC_Image)
        instance.Drinking_Water_Facility = validated_data.get('Drinking_Water_Facility', instance.Drinking_Water_Facility)
        instance.Toilet_Facility = validated_data.get('Toilet_Facility', instance.Toilet_Facility)
        instance.Electricity_Avaiable = validated_data.get('Electricity_Avaiable', instance.Electricity_Avaiable)
        instance.Kitchen_Garden_Available = validated_data.get('Kitchen_Garden_Available', instance.Kitchen_Garden_Available)
        instance.save()

        if sector_data is not None:
            sector.sector_name = sector_data.get('sector_name', sector.sector_name)
            sector.save()

        return instance