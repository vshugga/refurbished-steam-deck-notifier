# refurbished steam deck notifier - notifies when refurbished steam deck is in stock
#  Copyright (C) <2025>  <Oliver Blass>
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from time import gmtime, strftime
import requests
from discord_webhook import DiscordWebhook
import time
import os

# The country we want check for availability
# List of possibilities here https://github.com/RudeySH/SteamCountries/blob/master/json/countries.json
# DE, UK, US ...
country_code = 'DE'

# This is the endpoint to check availability
url = 'https://api.steampowered.com/IPhysicalGoodsService/CheckInventoryAvailableByPackage/v1?origin=https:%2F%2Fstore.steampowered.com&country_code='+country_code+'&packageid='

# The webhook we'll send updates to
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/some_webhook", content="error") # NEVER ever upload your webhook to github! Anyone could use it to send spam messages to your discord.

def superduperscraper (version, urlSuffix, isOLED: bool) :

    # This part is for pinging roles in a discord server with multiple regions
    # For personal use you can remove this part
    roleIdWithCountry = ""

    if(urlSuffix == "903905"): #64gb lcd
        roleIdWithCountry = "1343233406791716875"
    elif(urlSuffix == "903906"): #256gb lcd
        roleIdWithCountry = "1343233552896229508"
    elif(urlSuffix == "903907"): #512gb lcd
        roleIdWithCountry = "1343233731795881994"
    elif(urlSuffix == "1202542"): #512gb oled
        roleIdWithCountry = "1343233909655343234"
    elif(urlSuffix == "1202547"): #1tb oled
        roleIdWithCountry = "1343234052957802670"

    oldvalue = ""
    # previous availability is stored in a file
    # we get the value before checking here
    if (os.path.isfile(urlSuffix + "gb.txt")):
        file_read = open(urlSuffix + "gb.txt", "r")
        oldvalue = file_read.read()
        file_read.close()
    print("ov: "+ oldvalue)

    # make the request to steam to see if the steam deck is available
    response = requests.get(url+urlSuffix)
    # True / False depending on if it's available or not
    availability = str(response.json()["response"]["inventory_available"])
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " >> "+version+"GB Result: " + availability + " | raw: " + str(response.text))
    # save the new availability to the same file as above
    file = open(urlSuffix + "gb.txt", "w")
    file.write(availability)
    file.close()
    # if the new availability is different form the old one
    if oldvalue != availability and oldvalue != None :
        # and if it's available send a positive message to discord
        if availability == "True" :
            if isOLED:
                webhook.content = "refurbished "+version+"GB OLED steam deck available <@&" + roleIdWithCountry + ">" # If you removed the roles at the top you need to remove this <@&" + roleIdWithCountry + ">" as well
            else:
                webhook.content = "refurbished "+version+"GB LCD steam deck available <@&" + roleIdWithCountry + ">"
            webhook.execute()
        # if not send a negative message
        else:
            if isOLED:
                webhook.content = "refurbished "+version+"GB OLED steam deck not available"
            else:
                webhook.content = "refurbished "+version+"GB LCD steam deck not available"
            webhook.execute()

# The numbers are the individual ids for the refurbished steam deck
# You can see these on steamdb
superduperscraper("64", "903905", False) # 64gb lcd
superduperscraper("256", "903906", False) # 256gb lcd
superduperscraper("512", "903907", False) # 512gb lcd
superduperscraper("512", "1202542", True) # 512gb oled
superduperscraper("1024", "1202547", True) # 1tb oled
