from django.conf.urls import url,include

from views import *

urlpatterns=[
      
     url(r'^got_list/$','got_app.views.GotList',name="got_list"),
     url(r'^search/got_list/$','got_app.views.SearchGot',name="got_list",name="search_got"),
  
 ]
