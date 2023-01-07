from rest_framework import serializers

from userpanel.models import *


class CustomDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDocumentUploadModel
        fields = "__all__"
        read_only_fields = ['user',]
        
        
class ProfileDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileDocumentModel
        fields = "__all__"
        
class SubmitFileQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SubmitFileQuestion
        fields = "__all__"
class SubmitPreVerifiedQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SubmitPreVerifiedQuestion
        fields = "__all__"
class SubmitTextQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SubmitTextQuestion
        fields = "__all__"
        
class JobSubmitFileQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= JobSubmitFileQuestion
        fields = "__all__"
class JobSubmitPreVerifiedQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= JobSubmitPreVerifiedQuestion
        fields = "__all__"
class JobSubmitTextQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= JobSubmitTextQuestion
        fields = "__all__"