"""
Module: Lookup
Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.8.3 (64-Bit)
Description:
This is a module that would acquire information,
of an IPv4 or IPv6 address provided by the user.
"""

import urllib.request
import json

def ip_info():
    """
    This function will look up the IPv4 or IPv6 address information
    (ex. Country reserved for, type of ip address, etc.).
    """

    try:
        # This will prompt the user for an IPv4 or IPv6 address
        ip_addr = input("Enter an IP(v4/v6) Address: ")

        # This file will be in write mode, 
        # and have all of the IPv4/v6 address.
        file = open("IP Info.txt", "w")
        # This is the url used for acquring 
        # the information about the IPv4/v6 address.
        url = "https://ipapi.co/{0}/json/".format(ip_addr)
        # This will open the url to acquire information.
        response = urllib.request.urlopen(url=url)
        # This will store the information from the url.
        data = json.load(response)
        # This will store the type of IP address the user entered.
        ip_type = data["version"]
        # These will store the country that the IPv4/v6 address is reserved for.
        country_name, country_code = data["country_name"], data["country_code"] 
        # This will store the city in the country specified
        city = data["city"]
        # This will store the region of the country.
        region = data["region"]
        # These will store the latitude and longitude of location.
        lati, longi = data["latitude"], data["longitude"]
        # This will store the timezone of the country.
        utc_code, time_zome = data["utc_offset"], data["timezone"]

        info = [ip_type, country_name, country_code, 
        city, region, lati, longi, utc_code, time_zome]
        
        # This will store all of the 
        # information stored in 
        # mutliple variables, into one variable.
        info = """
{0} Address: {1} 
Country: {2} ({3})
City: {4}
Region: {5}
Latitude: {6}
Longtitude: {7}
Timezone: {8}({9})
""".format(info[0],info[1],
info[2],info[3],info[4],info[5],
info[6],info[7],info[8],info[9])

        # This will print the information
        print(info)
        # This will write all of the information into a txt file
        file.write(info)
        # This will close the file, once 
        # all of the information has been writen.
        file.close()

    except urllib.error.URLError:
        print("You're offline")
    