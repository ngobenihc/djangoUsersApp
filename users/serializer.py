from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password =serializers.CharField(write_only=True,required=False)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user



    def update(self, instance, validated_data):
        try:
            user = instance
            password = validated_data.pop("password")
            odl_password = validated_data.pop("odl_password")
            if user.check_password(odl_password):
                user.set_password(password)
            else:
                raise Exception("odl_password doesn't match")
            user.save()
        except Exception as err:
            raise serializers.ValidationError(err)
        return super(UserSerializer,self).update(instance, validated_data)

    class Meta:
        model = User
        fields=['url','id','username','email','first_name','last_name','password','odl_password']