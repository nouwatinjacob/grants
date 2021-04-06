from rest_framework import serializers
from . import models as m

class ApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = m.Application
        fields = ('id', 'prefix', 'referral', 'first_name', 'last_name',
                  'middle_name', 'dob', 'mother_name', 'relationship', 'gender',
                  'occupation', 'ssn', 'address', 'state', 'nationality',
                  'phone', 'fax', 'income', 'email', 'bank', 'description')
        
    def create(self, validated_data):
        application = m.Application.objects.create(**validated_data)
        print("application>>>>>", application)
        
        return application