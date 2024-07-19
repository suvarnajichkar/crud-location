
from django.urls import path
from .views import *

urlpatterns = [
	# country
    path('',indexView.as_view(),name="index"),
	path('country/',CountryView.as_view(),name="country"),
	path('country/<int:id>/',CountryView.as_view(),name="country"),
	path('update/<int:id>/',CountryUpdate.as_view(),name='update'),

	# state
	path('state/',StateView.as_view(),name="state"),
	path('delete/<int:id>/',Statedelete.as_view(),name="delete"),
	path('supdate/<int:id>/', StateUpdate.as_view(), name='supdate'),

	# city
	# path('city/',CityView.as_view(),name="city"),

    path('city/', CityView.as_view(), name='city'),
	path('ajax/load-states/', StateListView.as_view(), name='ajax_load_states'),
	path('city/update/<int:id>/', CityUpdateView.as_view(), name='updatecity'),
	path('city/delete/<int:id>/', CityDeleteView.as_view(), name='deletecity'),

]




