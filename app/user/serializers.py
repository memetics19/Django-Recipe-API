from django.contrib.auth import get_user_model, authenticate 
from rest_framework import serializers 
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email','password','name')
        extra_kwargs ={'password':
        {'write_only':True, 
        'min_length':8
        }
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and rerun it"""
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user       

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object """

    email = serializers.CharField(max_length = None)
    password = serializers.CharField(
        style = {'input_type':'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        """Validate and authenticate the user here """
        email = attrs.get('email')
        password = attrs.get('password')


        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user: 
            msg = ('User is not valid')
            raise serializers.ValidationError(msg,code='authentication')

        attrs['user'] = user
        return attrs 
