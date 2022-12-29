from rest_framework import serializers


""""
SETTING A USER DATA SERIALIZER AS A FOREIGN KEY TO OTHER MODELS
"""
class UserDataSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
