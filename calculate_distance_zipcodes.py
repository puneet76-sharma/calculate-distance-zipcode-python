# pip install pgeocode

from pgeocode import GeoDistance

country= input("enter your country: ")
dist= GeoDistance(country)

origin= input("Enter Your Origin Location Zipcode: ")
destination= input("Enter Your Destination Location Zipcode: ")
d= dist.query_postal_code(origin, destination)

print(d, "km")

input()