from django.db.models import fields
from rest_framework import serializers
from django.contrib.postgres import PostgresUpsertMixin
from .models import *
  
class UserSerializer(PostgresUpsertMixin,serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'email', 'username']

    on_conflict_do_nothing = True

class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectrictyConsumption
        fields = ['hoursOfPhoneUsage', 'hoursOfComputerUsage', 'hoursOfTVUsage', 'user']

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterConsumption
        fields = '__all__'

class HeatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatingConsumption
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_question
        fields = '__all__'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_question
        fields = '__all__'

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_answer
        fields = '__all__'

class TakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Take
        fields = '__all__'

class TakeAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Take_answer
        fields = '__all__'