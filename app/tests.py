from django.test import TestCase
import datetime
import folium
from chart_studio import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
# Create your tests here.

time = datetime.datetime.now()
datetime_obj = time.strftime("%H:%M")  
print(str(datetime_obj))
print(time.hour)
print(time.minute)
hour = time.hour
minute = time.minute
actual_time = str(hour) + '.' + str(int((minute*5)/3))
print(float(actual_time))