import json
from django.http.response import Http404, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect
from rest_framework import serializers, status, generics, permissions
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import mandrill

from django.core.mail import send_mail



from . import serializers as s
from . import models as m


class SubmitApplication(APIView):
    def post(self, request):
        serializer = s.ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application = m.Application.objects.create(
                prefix=request.data.get('prefix'), referral=request.data.get('referral'),
                first_name=request.data.get('first_name'), last_name=request.data.get('last_name'), 
                middle_name=request.data.get('middle_name'), mother_name=request.data.get('mother_name'),
                dob=request.data.get('dob'), relationship=request.data.get('relationship'), 
                gender=request.data.get('gender'), occupation=request.data.get('occupation'),
                ssn=request.data.get('ssn'), address=request.data.get('address'),
                state=request.data.get('state'), nationality=request.data.get('nationality'),
                phone=request.data.get('phone'), fax=request.data.get('fax'),
                income=request.data.get('income'), email=request.data.get('email'),
                bank=request.data.get('bank'), description=request.data.get('description')
            )
            
            # mail_subject = 'New Grant submittion'
            
            # # message = render_to_string('partials/email.html', {})
            # message = "I am here"
            
            # to_email = 'frankgab102@yahoo.com'
            # email = EmailMessage(
            #         mail_subject, message, to=[to_email, 'jaysansa@gmail.com']
            #     )
            # email.send()
            
            # send_mail("It works!", "This get sent through djrill",
            #         "Djrill Sender <djrill@example.com>", ["jaysansa@gmail.com"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
