from django.conf.urls import url
from basic_app import views

# FOR TEMPLATE TAGGING.  Global variable that tells django which app
# to look in for the appropriate template tags
app_name = 'basic_app'

# Adding the '$' will include anything after relative
urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
