from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','password','first_name','phone')
        extra_kwargs = {
            'password': {'write_only': True, 'required':False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance