# Project Summary
This is the geospatioal data visulaization dashboard developed for visualizing the urban water consumption in the city of Durban. The user can select the different map backgrounds, select the counties as well as display the top ten counties by water consumptions. 

> `--capt-add=SYS-ADMIN`
Built with Python-Django, PostGIS satabase, Leaflet, Openstreetmap, JavScript,and Boostrap.

# Getting Started

1.  CD into your preferred directory and git clone the project :

```bash
$ git clone https://github.com/ksopan/Water_Consumption_dashboard
```

2.  Install required Database : 

```bash
brew install postgresql
```
After installing PostgreSQL issue following command to get Postgresql started :
```bash
sudo mkdir /usr/local/var/postgres
sudo chmod 775 /usr/local/var/postgres
sudo chown sopank /usr/local/var/postgres
initdb /usr/local/var/postgres
```

3.  Install required Libraries for Geospatail Visualzation using homebrew on MacOS :

```bash
brew install postgis
brew install gdal
brew install libgeoip
```
4. Create Data Base :

```bash
createdb cpwater ### Create Database
createuser -s waterwatch -P ## Create username and set password
grant all privileges on database cpwater to waterwatch; ### Grant all cptwater privileges to user waterwatch
CREATE EXTENSION postgis; ### Create extension to anable database to store data
CREATE EXTENSION postgis_topology; ## Create second extension
```

4. Change to your favourite Python Virtual Environment :
```bash
pip install django-toolbelt
pip install django-leaflet # Install leaflet
pip install geojson
cd WaterWatch
```

5. Make important changes in the settings.py file for database (line # 85 to 88) :
``` bash
'NAME':'cpwater',
'USER':'waterwatch',
'PASSWORD':'', ### Create your own password
```

6. Migrate database and run app :
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
7. Webpage :

```bash
localhost:PORT 
```


Following is the demo of the App.
