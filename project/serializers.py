from rest_framework import serializers
from .models import Service, Project, Program

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('id', 'name','icon')


class ProjectSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'image', 'slug', 'category', 'description', 'created_at', 'program')


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'name','icon', 'slug', 'description', 'created_at')