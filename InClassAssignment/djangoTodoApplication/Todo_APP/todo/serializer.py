from rest_framework import serializers
from .models import TodoModel

class todoSerializer(serializers.HyperlinkedModelSerializer):   
    id= serializers.ReadOnlyField()
    class Meta:
        model= TodoModel
        fields= "__all__"
