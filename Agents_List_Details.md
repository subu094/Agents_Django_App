Steps and Process followed to create the application:
1) installed python
2) django 2.2
3) used sqlite3 db
4) converted tsv file into csv and then inserted within a table in sqlite3 db(Using DBeaver)
5) Created a model with all the following data in the tsv and also 2 more columns latitude and longitude
to Fetch latitude and longitude used Geopy lib installed the packages for geopy.
From the below script added lat and long for all the places in the database.
from  geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="AgentsList")
    x = Agents_Details.objects.all()
    for i in x:
...     loc = geolocator.geocode(i.zipcode)
...     i.latitude = loc.latitude
...     i.longitude = loc.longitude
        i.save()

6) Created 11 htmls templates as mentioned in the problem statement
Note:
Thought of implementing within a single html which will render on base of the 11 states menioned
that is also possible
7) Differentiated all the individual views which will render their own HTml pages

