from rest_framework import serializers

from taksist.models import TaxiProfile, User, TaxiStatus, Category, Status, SaherAra, SaherIci, EtrapObalary

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
        # if self.context.get('cat')==2:
        nireden = SaherAra.objects.get(taxi_id=taksist)
        return nireden.city1.name
        # elif self.context.get('cat')==3:
        #     nirede = SaherIci.objects.get(taxi_id=taksist)
        #     return nirede.city
        # elif self.context.get('cat')==1:
        #     nirede = EtrapObalary.objects.get(taxi_id=taksist)
        #     return nirede.city
        # else:
        #     taxi = TaxiProfile.objects.get(user_id=taksist)
        #     return taxi.user_id


    def get_nira(self, taksist):
        # if self.context.get('cat')==2:
        nira = SaherAra.objects.get(taxi_id=taksist)
        return nira.city2.name
        # else:
        #     return ''
        