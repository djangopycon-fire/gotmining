from django.shortcuts import render_to_response,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from models import GotDetail
from django.template import RequestContext
from forms import GotListForm
import json
import traceback

## Api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from rest_framework import generics, viewsets
from serializers import GotSerializer
from rest_framework.renderers import JSONRenderer


## utility function

def intersect_list(a,b):
    return list(set(a) & set(b))

def union_list(a,b):
    return list(set(a) | set(b))

def GotList(request):
    if request.method=="GET":
        form=GotListForm()
        return render_to_response('searching_got_list.html',{'form':form})
        
    
@csrf_exempt
def SearchGot(request):
    print 'inside searching Got'
    form_data=request.POST.get('form_data','')
    form_data=json.loads(form_data)

    got_detail_list=GotDetail.objects.all()
    query_list = ''

    for i in range(len(form_data)):
        current_dict = form_data[i]
        print current_dict


        if current_dict['name'] == 'name':
            list_of_name=current_dict['value'].split(',')
            for k in range(len(list_of_name)):
                battle_id=list_of_name[k]
                print battle_id
                if battle_id != '' and battle_id != None:
                    try:
                        got_detail = GotDetail.objects.filter(name=battle_id)
                        ## for debugging
                        for detail in got_detail:
                            print detail.name, detail.year,detail.attacker_commander
                        print '############' 
                        query_list=union_list(query_list,list(got_detail))  

                    except Exception as e:
                        print e
                        traceback.print_exc()
                    ##query_list=union_list(query_list,list(got_detail)) 

        if current_dict['name'] == 'battle_type':
            list_of_battle_type=current_dict['value'].split(',')
            for k in range(len(list_of_battle_type)):
                battle_id=list_of_battle_type[k]
                print battle_id
                if battle_id != '' and battle_id != None:
                    try:
                        got_detail = GotDetail.objects.filter(battle_type=battle_id) 
                        for detail in got_detail:
                            print detail.name, detail.year,detail.attacker_commander
                        print '############' 
                        query_list=union_list(query_list,list(got_detail))  

                    except Exception as e:
                        print e
                        traceback.print_exc()
                    ##query_list=union_list(query_list,list(got_detail)) 
                                   
        if current_dict['name'] == 'attacker_king':
            list_of_attacker_king=current_dict['value'].split(',')
            for k in range(len(list_of_attacker_king)):
                attacker_king_id=list_of_attacker_king[k]
                print attacker_king_id
                if attacker_king_id != '' and attacker_king_id != None:
                    try:
                        got_detail = GotDetail.objects.filter(attacker_king=attacker_king_id) 
                        for detail in got_detail:
                            print detail.name, detail.year,detail.attacker_commander
                        print '############' 
                        query_list=union_list(query_list,list(got_detail))  

                    except Exception as e:
                        print e
                        traceback.print_exc()
                    ##query_list=union_list(query_list,list(got_detail))     

        if current_dict['name'] == 'location':
            list_of_location=current_dict['value'].split(',')
            for k in range(len(list_of_location)):
                location_id=list_of_location[k]
                print location_id
                if location_id != '' and location_id != None:
                    try:
                        got_detail = GotDetail.objects.filter(location=location_id) 
                        for detail in got_detail:
                            print detail.name, detail.year
                        print '############' 
                        query_list=union_list(query_list,list(got_detail))  

                    except Exception as e:
                        print e
                        traceback.print_exc()
                    ##query_list=union_list(query_list,list(got_detail))
                     
                        
 
    list_of_matching_profiles = []
    for got_detail in query_list:
        list_of_matching_profiles.append([got_detail.name,got_detail.year,
                                        got_detail.battle_number,got_detail.attacker_king,got_detail.defender_king,
                                        got_detail.battle_type,got_detail.location,
                                        got_detail.attacker_size,got_detail.defender_size])
    print list_of_matching_profiles    
    return JsonResponse(list_of_matching_profiles,safe=False)




### for api


class GotListView(generics.ListAPIView):
    queryset = GotDetail.objects.all()
    serializer_class=GotSerializer


class GotDetailView(generics.RetrieveAPIView):
    queryset =GotDetail.objects.all()
    serializer_class=GotSerializer


## api returning count of total records

class GotCountView(APIView):

    def get(self, request, format=None):
        got_count = GotDetail.objects.all().count()
        content = {'got_count': got_count}
        return Response(content)    