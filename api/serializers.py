from rest_framework import serializers

from taksist.models import TaxiProfile, User, TaxiStatus, Category, Status, SaherAra

class TaxiSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_taksist_name')
    cat_id = serializers.StringRelatedField()
    status_id = serializers.StringRelatedField()
    nireden = serializers.SerializerMethodField('get_nireden')
    nira = serializers.SerializerMethodField('get_nira')

    class Meta:
        model = TaxiProfile
        fields = ['user_id', 'mobile', 'username', 'cat_id', 'status_id', 'nireden', 'nira']

    def get_taksist_name(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.first_name

    def get_nireden(self, taksist):
        nireden = SaherAra.objects.get(taxi_id=taksist)
        return nireden.city1.name

    def get_nira(self, taksist):
        nira = SaherAra.objects.get(taxi_id=taksist)
        return nira.city2.name