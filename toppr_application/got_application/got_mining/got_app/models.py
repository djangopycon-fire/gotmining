from django.db import models
from commander.models import AttackerCommander,DefenderCommander

class GotDetail(models.Model):

    BATTLE_TYPE=(
        ('ambush','Ambush'),
        ('siege','Siege'),
        ('pitched battle','Pitched Battle'),
        ('razing','Razing'),
        )
    name                =models.CharField(max_length=200,verbose_name="Name",blank=True)
    year                =models.IntegerField(default=0,null=True)
    battle_number       =models.IntegerField(default=0)
    attacker_king       =models.CharField(max_length=200,null=True,verbose_name="Attacker_king",blank=True)
    attacker_1          =models.CharField(max_length=200,null=True,verbose_name="Attacker_1")
    attacker_2          =models.CharField(max_length=200,null=True,verbose_name="Attacker_2")
    attacker_3          =models.CharField(max_length=200,null=True,verbose_name="Attacker_3")
    attacker_4          =models.CharField(max_length=200,null=True,verbose_name="Attacker_4")
    defender_king       =models.CharField(max_length=200,null=True, verbose_name="Defender_king")
    defender_1          =models.CharField(max_length=200,null=True, verbose_name="Defender_1")
    defender_2          =models.CharField(max_length=200,null=True, verbose_name="Defender_2")
    defender_3          =models.CharField(max_length=200,null=True, verbose_name="Defender_3")
    defender_4          =models.CharField(max_length=200,null=True, verbose_name="Defender_4")
    attacker_coutcome   =models.CharField(max_length=200,verbose_name="Attacker_outcome")
    battle_type         =models.CharField(max_length=200,verbose_name="Battle_Type",choices=BATTLE_TYPE,blank=True)
    major_death         =models.IntegerField(default=0)
    major_capture       =models.IntegerField(default=0) 
    attacker_size       =models.PositiveIntegerField(default=0)
    defender_size       =models.PositiveIntegerField(default=0)
    attacker_commander  =models.ForeignKey(AttackerCommander,null=True,related_name="got_attacker_comander")
    defender_commander  =models.ForeignKey(DefenderCommander,null=True,related_name="got_defender_commander")   
    summer              =models.IntegerField(default=0,null=True)
    location            =models.CharField(max_length=100,verbose_name="Location",null=True,blank=True)
    region              =models.CharField(max_length=100,verbose_name="Region",null=True)
    note                =models.CharField(max_length=100,verbose_name="Note",null=True)

    def __unicode__(self):
        return self.name
        
    # class Meta:
    #     app_label = 'ritu'  