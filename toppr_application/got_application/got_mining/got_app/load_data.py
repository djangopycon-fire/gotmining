import sys,os,django
from django.conf import settings

sys.path.append("/home/ritu/Desktop/got_application/got_mining") #Set it to the root of your project
os.environ["DJANGO_SETTINGS_MODULE"] = "got_mining.settings"
django.setup()


import csv

# Full path and name to your csv file
csv_filepathname="/home/ritu/Desktop/got_application/got_mining/battle_1.csv"
# Full path to your django project directory
##your_project_home="/home/ritu/Desktop/got_application/battle_1.csv"


from got_app.models import GotDetail
from commander.models import AttackerCommander,DefenderCommander

dataReader = csv.reader(open(csv_filepathname, 'rU') ,  dialect='excel')
print '##############'
print dataReader
print '#############'

attacker_commander= AttackerCommander.objects.all()
tempMap= {}

for attacker in attacker_commander:
    tempMap[attacker.name]=attacker
print(tempMap)

## adding defender commander

defender_commander= DefenderCommander.objects.all()
tempMap_2= {}

for defender in defender_commander:
    tempMap_2[defender.name]=defender
print(tempMap_2)

for row in dataReader:
    got_detail=GotDetail()
    got_detail.name=row[0]
    got_detail.year=row[1]
    got_detail.battle_number=row[2]
    if row[3]:
        got_detail.attacker_king=row[3]
    if row[4]:    
        got_detail.attacker_1=row[4]
    got_detail.attacker_2=row[5]
    got_detail.attacker_3=row[6]
    got_detail.attacker_4=row[7]
    got_detail.defender_1=row[8]
    if row[9]:
        got_detail.defender_king=row[9]
    got_detail.defender_2=row[10]
    got_detail.defender_3=row[11]
    got_detail.defender_4=row[12]
    got_detail.attacker_outcome=row[13]
    got_detail.battle_type=row[14]
    got_detail.major_death=row[15]
    got_detail.major_capture=row[16]
    if row[17]:
        got_detail.attacker_size=row[17]
    if row[18]:    
        got_detail.defender_size=row[18]
    if row[19]:
            attacker = row[19]
            if(attacker in  tempMap.keys()):
                got_detail.attacker_commander=tempMap[attacker]
            else:
                pass

    if row[20]:
            defender= row[20]
            if(defender in  tempMap_2.keys()):
                got_detail.defender_commander=tempMap_2[defender]
            else:
                pass            
    if row[21]:
        got_detail.summer=row[21]
    if row[21]:
        got_detail.location=row[22]
    if row[23]:
        got_detail.region=row[23]
    if row[24]:
        got_detail.note=row[24]

    got_detail.save()


    

        