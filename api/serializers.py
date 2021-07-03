from rest_framework import serializers

from taksist.models import TaxiProfile, User #, TaxiStatus, Category, Status, SaherAra, SaherIci, EtrapObalary

class TaxiSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField('get_taksist_first_name')
    last_name = serializers.SerializerMethodField('get_taksist_last_name')
    username = serializers.SerializerMethodField('get_taksist_username')
    category = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    nireden = serializers.StringRelatedField()
    nira = serializers.StringRelatedField()

    class Meta:
        model = TaxiProfile
        fields = ['user_id', 'mobile', 'username', 'first_name', 'last_name', 'nireden', 'nira', 'category', 'status']
    
    def get_taksist_first_name(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.first_name
    
    def get_taksist_last_name(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.last_name

    def get_taksist_username(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.username

