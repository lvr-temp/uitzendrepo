from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Company, Contact
from tender.models import Tenderbase

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',
                  'password',
                  'userrole',
                  'is_active',
                  'is_staff',
                  'is_admin'
                )


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.id')

    class Meta:
        model = Contact
        fields = ('gender',
                  'firstname',
                  'prefix',
                  'lastname',
                  'phonenumber',
                  'user'
        )


class CompanySerializer(serializers.ModelSerializer):
    commissioner_user_company = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Company
        fields = ('name',
                  'description',
                  'website',
                  'commissioner_user_company'
        )




