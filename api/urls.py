from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(
        r'^items/(?P<typee>(\d,?){0,30})/(?P<cpu>(\d,?){0,30})/(?P<cpu_type>(\d,?){0,30})/(?P<ram>(\d,?){0,30})/(?P<hdd>(\d,?){0,30})/(?P<gpu>(\d,?){0,30})/$', views.Items.as_view()),
    re_path(r'cputypes/(?P<id>(\d,?){0,30})/$', views.cpuTypes),
]
