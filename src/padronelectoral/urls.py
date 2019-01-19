
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.loadIndex, name='index'),
    path('search', views.get_electors, name='get_electors'),
    path('stats/province/<int:pk>', views.get_province_data, name='get_province_data'),
    path('stats/canton/<int:pk>', views.get_canton_data, name='get_canton_data'),
    path('stats/district/<int:pk>', views.get_district_data, name='get_district_data'),
    path('newelector',views.createElector,name='new_elector')
    #  path('stats/<str:pk>/', views.DeleteDistrict, name='deleteDistrict'),
]