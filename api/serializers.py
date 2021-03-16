from rest_framework import serializers

from taksist.models import TaxiProfile, User, TaxiStatus, Category, Status

class TaxiSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_taksist_name')
    # xstatus = serializers.SerializerMethodField('get_taksist_status')
    # xcategory = serializers.SerializerMethodField('get_taksist_category')
    cat_id = serializers.StringRelatedField()
    status_id = serializers.StringRelatedField()

    class Meta:
        model = TaxiProfile
        fields = ['user_id', 'mobile', 'username', 'cat_id', 'status_id']

    def get_taksist_name(self, taksist):
        user = User.objects.get(taxiprofile = taksist)
        return user.first_name

    # def get_taksist_status(self, taksist):
    #     try:
    #         xstatus = TaxiStatus.objects.get(user_id=taksist.user_id)
    #         if xstatus:
    #             return xstatus.status
    #     except:
    #         return 'no status'
    
    # def get_taksist_category(self, taksist):
    #     return TaxiProfile.get_category(taksist)