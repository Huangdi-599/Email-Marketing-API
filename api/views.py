from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework import generics,permissions,serializers
from rest_framework. views import APIView
from rest_framework.response import Response


from .models import Lists, EmailContact
from .serializers import ListsSerial, EmailContactSerial
from .auth_serializers import SignupSerializer



class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    
    
class UserLogout(APIView):  
   pass 
            
           
class CreateLists(generics.ListCreateAPIView):
    queryset = Lists.objects.all()
    serializer_class = ListsSerial
    def get_queryset(self, *args , **kwargs):
        qs = super().get_queryset(*args , **kwargs)
        request  = self.request
        user = request.user
        if user.is_authenticated:
            return qs.filter(user = request.user)   
    def perform_create(self , serializer):
        request  = self.request
        serializer.save(user = request.user) 
        
        
class UpdateLists(generics.UpdateAPIView):
    queryset = Lists.objects.all()
    serializer_class = ListsSerial
    lookup_field = 'pk'
    def perform_update(self, serializer):
        serializer.save()

class DeleteLists(generics.DestroyAPIView):
    queryset = Lists.objects.all()
    serializer_class = ListsSerial
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        