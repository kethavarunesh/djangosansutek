from rest_framework import serializers
from myapp.models import Contactform

class ContactformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contactform
        fields=['name','email','phone','message']


from myapp.models import ResumeSubmission

class ResumeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeSubmission
        fields = '__all__'