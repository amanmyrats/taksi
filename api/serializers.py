from rest_framework import serializers

from taksist.models import TaxiProfile, User #, TaxiStatus, Category, Status, SaherAra, SaherIci, EtrapObalary

class TaxiSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField('get_taksist_first_name')
    last_name = serializers.SerializerMethodField('get_taksist_last_name')
    username = serializers.SerializerMethodField('get_taksist_username')
    car_photo_url = serializers.SerializerMethodField('get_car_photo_url')
    user_photo_url = serializers.SerializerMethodField('get_user_photo_url')
    category = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    nireden = serializers.StringRelatedField()
    nira = serializers.StringRelatedField()

    class Meta:
        model = TaxiProfile
        fields = ['user_id', 'mobile', 'username', 'first_name', 'last_name', 'nireden', 'nira', 'category', 'status', 'car_photo', 'user_photo','car_photo_url', 'user_photo_url']
    
    def get_taksist_first_name(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.first_name
    
    def get_taksist_last_name(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.last_name

    def get_taksist_username(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.username
    
    def get_car_photo_url(self, taksist):
        return taksist.car_photo.url
    
    def get_user_photo_url(self, taksist):
        return taksist.user_photo.url

