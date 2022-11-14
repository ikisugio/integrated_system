from rest_framework import serializers
from .models import Office

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'
        # [
        #     'id',
        #     'care_office_code',
        #     'name',
        #     'care_service_code',
        #     'postal_code',
        #     'address',
        #     'latitude',
        #     'longitude',
        #     'type',
        #     'company',
        #     'owner',
        #     'manager',
        #     'capacity_of_guests',
        #     'url',
        #     'foundation_date',
        #     'number_of_employees',
        # ]