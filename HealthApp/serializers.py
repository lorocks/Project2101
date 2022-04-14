from rest_framework import serializers
from .models import testingAPI, FirebaseData, Alert

class testingAPISerializer(serializers.ModelSerializer):
    data = serializers.FloatField()
    string = serializers.CharField(max_length=200)

    class Meta:
        model = testingAPI
        fields = ('__all__')

class FirebaseDataSerializer(serializers.ModelSerializer):
    Temp = serializers.FloatField()
    IR = serializers.IntegerField()
    username = serializers.CharField(max_length = 4)

    class Meta:
        model = FirebaseData
        fields = ('__all__')

class AlertSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=4)

    class Meta:
        model = Alert
        fields = ('__all__')