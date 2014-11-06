from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model
import requests
from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .models import Company, Contact
from .serializers import CompanySerializer, ContactSerializer, UserSerializer
from tender.models import Branch



class CompanyDetailApi(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a company.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ContactDetailApi(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contact
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user


class UserViewSet(viewsets.ModelViewSet):
    """
    Get an overview of the users
    """
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete  user
    """
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)