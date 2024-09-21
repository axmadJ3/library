from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import AccountSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    

