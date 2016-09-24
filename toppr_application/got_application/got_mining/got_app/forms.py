from django import forms
from models import GotDetail
class GotListForm(forms.ModelForm):
   class Meta:
      model=GotDetail
      fields=['name','attacker_king','battle_type','location']

      labels={
         'name':'Battle name',
         'attacker_king':'Attacker King',
         'battle_type':'Battle Type',
         'location':'Location'
      }
      
      widgets={
         


      }


 