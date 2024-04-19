from django.shortcuts import render,redirect
from rest_framework import viewsets
from myapp.models import Contactform
from myapp.serializers import ContactformSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
class ContactformviewSet(viewsets.ModelViewSet):
    queryset=Contactform.objects.all()
    serializer_class = ContactformSerializer

from .models import ResumeSubmission
from .serializers import ResumeSubmissionSerializer

class ResumeSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ResumeSubmission.objects.all()
    serializer_class = ResumeSubmissionSerializer

@api_view(['POST'])
def save_contact_form(request):
    if request.method == 'POST':
        serializer = ContactformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import ResumeSubmission
from myapp.serializers import ResumeSubmissionSerializer

@api_view(['POST'])
def upload_resume(request):
    serializer = ResumeSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)