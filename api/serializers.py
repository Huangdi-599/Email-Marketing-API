from rest_framework import serializers


from .models import EmailContact, Lists
from .user_serializers import UserDataSerializer



class ListsSerial(serializers.ModelSerializer):
    user = UserDataSerializer(read_only = True)
    class Meta:
        model = Lists
        fields = [
            'user',
            'id',
            'name',
        ]
    def validate_name(self, value):
        request =  self.context.get('request')
        q = Lists.objects.filter(user=request.user)
        query = q.filter(name__iexact = value)
        if query.exists():
            raise serializers.ValidationError("This name already exist")
        return value


class EmailContactSerial(serializers.ModelSerializer):
    lists = ListsSerial(many = True, read_only=True)
    user = UserDataSerializer(read_only = True)
    class Meta:
        model = EmailContact
        fields = [
            'user',
            'id',
            'email',
            'lists',
            'reg_date'
        ]
        
    def validate_email(self, value):
        request =  self.context.get('request')
        q = EmailContact.objects.filter(user=request.user)
        query = q.filter(email__iexact = value)
        if query.exists():
            raise serializers.ValidationError("This email address already exist")
        return value
    
    

