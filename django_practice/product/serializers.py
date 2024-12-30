from rest_framework import serializers
from .models import Product
from django.contrib.auth.hashers import make_password

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", 'name', 'description', 'price', 'stock', 'supplier', 'created_at', 'updated_at']

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "password"]

#     def create(self, validated_data):
#         user = User(
#             username=validated_data['username'],
#             password=make_password(validated_data['password'])  # Ensure the password is hashed
#         )
#         user.save()
#         return user
    

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['isAdmin'] = user.is_staff
        

        return token