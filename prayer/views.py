from django.shortcuts import render
import requests
from .prayer import get_prayer_times
import socket
import json
# Create your views here.
class IpLocation:
    def visitor_ip_address(self):
        return socket.gethostbyname(socket.gethostname())

    def ip_valid(self):
        try:
            socket.inet_aton(self.visitor_ip_address())
            ip_valid = True
        except socket.error:
            ip_valid = False

    def geo_location(self):
        request_url = 'https://geolocation-db.com/jsonp/'
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result  = json.loads(result)
        return result

ip_geo = IpLocation()
ip = ip_geo.visitor_ip_address()
x = ip_geo.geo_location()
def prayer_views(request):
    city = x['city']
    country = x['country_name']
    response = get_prayer_times(city, country)
    prayer = response['data']
    prayer_calendar_timings = []
    #prayer_calendar_date = []
    #prayer_calendar_meta = []
    for i in range(len(prayer)):
        prayer_calendar_timings.append(prayer[i]['timings'])
        prayer_calendar_timings.append(prayer[i]['date'])
        prayer_calendar_timings.append(prayer[i]['meta'])
    context = {
        'response':prayer_calendar_timings,
    }
    return render(request, 'prayer.html', context)

