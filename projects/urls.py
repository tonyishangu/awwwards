from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.index, name='index'),
    url('^accounts/login/', views.login, name='login'),
    url('^profile/',views.profile, name='profile'),
    url('^new_project/',views.submit_project, name='submit_project'),
    url('^search/',views.search_project,name='search_project'),
    url('^project/(\d+)',views.project,name='project'),
    url('^api/profiles/$',views.ProfileList.as_view(),name='profile_list'),
    url('^api/projects/$',views.ProjectList.as_view(),name='project_list'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)