from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser, Bio, PrivacySettings
from django.db.models import Q
from django.conf import settings
import datetime

class UserSerializer(serializers.ModelSerializer):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer not to say'),
    )
    gender = serializers.ChoiceField(
        required=True,
        label="Gender",
        choices=GENDER
    )
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'date_of_birth', 'gender', 'terms_confirmed')

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    # def validate_date_of_birth(self, value):
        # if value == None:
            # raise serializers.ValidationError("please select date.")
        # return value

    def validate_date_of_birth(self, value):
        if value:
            dob = value
            print("dob:::", dob, datetime.datetime.now())
            age = (datetime.date.today() - dob) // datetime.timedelta(days=365.2425)
            print("age:::", age)
            if age <= 13:
                raise serializers.ValidationError('Must be greater than 13 years old to register')
            return dob
        else:
            raise serializers.ValidationError("please select date.")
        

    def validate_terms_confirmed(self, value):
        if value == 0:
            raise serializers.ValidationError("please agree on terms.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user       

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.password = validated_data['password']
        instance.date_of_birth = validated_data['date_of_birth']
        instance.gender = validated_data['gender']
        instance.save()

        return instance

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def validate(self, data):
        user_obj=None
        email = data.get('email', None)
        password = data.get('password', None)
        if not email and not username:
            print("getting nothing:::")
            raise serializers.ValidationError({"error":"Need to be filled"})

        # if CustomUser.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            # raise serializers.ValidationError(u'Username is not available')

        user = CustomUser.objects.filter(
                Q(email=email)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError({"email":"Not valid"})
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError({"password":"Incorrect credentials please try again"})
        new_data = user_obj
        print("new_data:::",new_data)
        return new_data
        
class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['user', 'phone_number', 'country', 'city', 'website', 'me', 'like', 'dislike', 'photo_url']

    def update(self, instance, validated_data):
        instance.phone_number = validated_data['phone_number']
        instance.country = validated_data['country']
        instance.city = validated_data['city']
        instance.website = validated_data['website']
        instance.me = validated_data['me']
        instance.like = validated_data['like']
        instance.dislike = validated_data['dislike']
        instance.photo_url = validated_data['photo_url']
        instance.save()

        return instance

class PrivacySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacySettings
        fields = ['user', 'privacy_settings']

# class BlockUsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Block
#         fields = ['user', 'blocked_user']
