from rest_framework import serializers
from .models import Login,Registration

class loginSerilaizer(serializers.HyperlinkedModelSerializer):   
    id= serializers.ReadOnlyField()
    class Meta:
        model= Login
        fields= "__all__"

class RegisterSerilaizer(serializers.HyperlinkedModelSerializer):   
    id= serializers.ReadOnlyField()
    class Meta:
        model= Registration
        fields= "__all__"
