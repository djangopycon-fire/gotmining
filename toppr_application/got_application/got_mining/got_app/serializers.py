from rest_framework import serializers

from got_app.models import GotDetail 


class GotSerializer(serializers.ModelSerializer):
    class Meta:
        model = GotDetail
        fields = ('name', 'battle_type', 'battle_number','attacker_king','defender_king','location')



