from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('profile/$',views.profile,name='profile'),
    # url('^explore/',views.explore_results,name='explore'),
    url('^update/$',views.update,name='update'),
    # url('^new_post/',views.new_post,name='new_post'),
    # url('^comment/(\d+)',views.comment,name='comment')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
