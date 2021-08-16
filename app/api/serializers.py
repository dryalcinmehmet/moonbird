from datetime import datetime

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from service.models import Questions, Answers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


class LoginUserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class LogoutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    question = serializers.CharField(required=True)
    date = serializers.DateField(required=False, default=datetime.now())

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs

    def validate_title(self, attrs):
        title = attrs
        if 'duman' in title:
            raise ValidationError({"msg": "Title 'duman' olamaz!"})
        return attrs

    def list(self):
        """
        List and return a new `Question` instance, given the validated data.
        """
        return Questions.objects.all()

    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Questions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """

        instance.title = validated_data.get('title', instance.title)
        instance.question = validated_data.get('question', instance.question)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
