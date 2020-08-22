# calculate-distance-zipcode-python

Postal code geocoding and distance calculations  pgeocode is a Python library for high performance off-line querying of GPS coordinates, region name and municipality name from postal codes. Distances between postal codes as well as general distance queries are also supported. The used GeoNames database includes postal codes for 83 countries.

Geocoding format
The result of a geo-localistion query is a pandas.DataFrame with the following columns,

country code: iso country code, 2 characters
postal code : postal code
place name : place name (e.g. town, city etc)
state_name : 1. order subdivision (state)
state_code : 1. order subdivision (state)
county_name : 2. order subdivision (county/province)
county_code : 2. order subdivision (county/province)
community_name : 3. order subdivision (community)
community_code : 3. order subdivision (community)
latitude : estimated latitude (wgs84)
longitude : estimated longitude (wgs84)
accuracy : accuracy of lat/lng from 1=estimated to 6=centroid
