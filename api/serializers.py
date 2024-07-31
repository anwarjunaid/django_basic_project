from rest_framework import serializers
from api.models import Company

# create serializers here.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # fields = ['id', 'name', 'location', 'about', 'addedDate', 'url']
        fields = "__all__"      # It will display all fields but not id.
        