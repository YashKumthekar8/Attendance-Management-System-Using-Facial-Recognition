from django.urls import path,include
from App import views
urlpatterns = [
 path('ohms-law-calculator/',views.ohmslawcalculator),
 path('acceleration-of-particle-in-electric-field-calculator/',views.accelerationofparticleinelectricfield),
 path('momentum-with-time-calculator/',views.momentumwithtimecalculator),
 path('weight-other-planets/',views.weightotherplanets),
 path('specific-heat-calculator/',views.specificheatcalculator), 
 path('half-life-calculator/',views.halflifecalculator),
 path('wet-bulb-calculator/',views.wetbulbcalculator),
 path('arrow-speed-calculator/',views.arrowspeedcalculator),
 path('friction-loss-calculator/',views.frictionlosscalculator),
 path('voltage-divider-calculator/',views.voltagedividercalculator),
 path('frequency-calcultor/',views.frequencycalcultor),
 

]
