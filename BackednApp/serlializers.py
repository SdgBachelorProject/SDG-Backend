from django.db.models import fields
from rest_framework import serializers
from .models import *
import json




class UserSerializer(serializers.ModelSerializer):

    friends = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('uid', 'email', 'username', 'friends', 'league')

class FriendsSerializer(UserSerializer):
    def to_representation(self, value):
        user_data = super().to_representation(value)
        user_json = json.dumps(user_data)
        user_dict = json.loads(user_json)
        friends = user_dict['friends']
        friends_json = json.dumps(friends)
        friends_list = json.loads(friends_json)
        user_dict['friends'] = friends_list
        return user_dict

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('friends',)



class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectrictyConsumption
        fields = '__all__'

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