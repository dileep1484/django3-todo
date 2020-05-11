from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer
    # todos = serializers.StringRelatedField(many=True)
    # todos = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only=True,
    #     view_name='user-detail',
    # )

    class Meta:
        model = Todo
        fields = ('id','title','memo','created','datecompleted','important','user')
        # fields = ['username', 'todos']