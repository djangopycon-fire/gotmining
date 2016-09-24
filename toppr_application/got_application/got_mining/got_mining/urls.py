from django.conf.urls import url,include
from django.contrib import admin
from got_app.views import GotList,SearchGot,GotListView,GotDetailView,GotCountView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^got/',include('got_app.urls',namespace="got_app",app_name="got_app")),
    url(r'^gotlist/$',GotList),
    url(r'^got/search/$',SearchGot,name="search_got"),
   	# url(r'^api/', include('api.urls', namespace='api')),

    url(r'^api/got/list/$',
        GotListView.as_view(),
        name='got_list'),

    url(r'^api/got/(?P<pk>\d+)/$',
        GotDetailView.as_view(),
        name='got_detail'),

    ## returning count of total record
    url(r'^api/got/count/$',
        GotCountView.as_view(),
        name='got_count'),

]


urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
