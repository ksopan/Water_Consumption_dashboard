from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from waterwatchapp.models import WaterConsumption

# Register your models here.

class WaterConsumptionAdmin(LeafletGeoAdmin):
    pass

admin.site.register(WaterConsumption, WaterConsumptionAdmin)

df_excelReader = pd.read_excel('/Users/sopank/Projects/Water_Consumption_dashboard/WaterWatch/waterwatch_clean2.xlsx', sheet_name="Sheet1")

for index, row in df_excelReader.iterrows():
    Id = index
    Suburb = row['Suburb']
    NoOfSingleResProp = row['Single_properties_number']
    AvgMonthlyKL = row['Oct 2017\nkl/month']
    AvgMonthlyKLPredicted = 0
    PredictionAccuracy = 0
    Month = row['Month']
    Year = row['Year']
    DateTime = datetime.now()
    Longitude = row['Longitude']
    Latitude = row['Latitude']

    WaterConsumption(Id=Id, Suburb=Suburb, NoOfSingleResProp=NoOfSingleResProp,
                     AvgMonthlyKL=AvgMonthlyKL, AvgMonthlyKLPredicted=AvgMonthlyKLPredicted,
                     PredictionAccuracy=PredictionAccuracy, Month=Month, Year=Year,
                     DateTime=DateTime, geom=Point(Longitude, Latitude)).save()
    
    
### Following code gives list of all the Django users       
from django.contrib.auth.models import User
all_users = User.objects.values()
print(all_users)
print(all_users[0]['username'])
#raise SystemExit