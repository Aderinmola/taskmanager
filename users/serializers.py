from rest_framework import serializers
from users.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ('email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        # fields = '__all__'
        fields = ['id', 'name', 'email', 'start_date']
        # extra_kwargs = {'password': {'write_only': True}}

    
