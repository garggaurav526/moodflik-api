from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from .models import CustomUser, Bio
from django.db.models import Q
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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

    def validate_date_of_birth(self, value):
        if value == None:
            raise serializers.ValidationError("please select date.")
        return value

    def validate_terms_confirmed(self, value):
        if value == 0:
            raise serializers.ValidationError("please agree on terms.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user       

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
        
        # def validate(self, data):
    #     email = data.get('email')
    #     password = data.get('password')

    #     if email and password:
    #         user = authenticate(email=email, password=password)
    #         print("835472465754:",user)
    #         if not user:
    #             msg = 'Unable to log in with provided credentials.'
    #             raise serializers.ValidationError(msg, code='authorization')
    #     else:
    #         msg = 'Must include "email" and "password".'
    #         raise serializers.ValidationError(msg, code='authorization')

    #     data['user'] = user
    #     return data



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         print("token:::",token)
#         # Add custom claims
#         token['username'] = user.username
#         return token


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['user', 'phone_number', 'country', 'city', 'website', 'me', 'like', 'dislike', 'photo_url']

    def update(self, instance, validated_data):
        instance.user = validated_data['user']
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