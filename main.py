import phonenumbers
from phonenumbers import geocoder
import folium
from tkinter import *
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import pytz
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from datetime import datetime
import webview

window = Tk()


def track_phone():
    while True:
        try:
            # Getting Country
            entry_box = entry.get()
            check_number = phonenumbers.parse(entry_box)
            number_location = geocoder.description_for_number(check_number, "en")
            # print(number_location)

            # Getting Service Provider
            service_provider = phonenumbers.parse(entry_box)
            pint = carrier.name_for_number(service_provider, "en")

            # Getting phone timezone
            zone = phonenumbers.parse(entry_box)
            time = timezone.time_zones_for_number(zone)
            # print(time)

            # Using maps to point location
            api_key = "dc1b429407694787af62e71f5a3eddbf"
            geo = OpenCageGeocode(api_key)
            query = str(number_location)
            result = geo.geocode(query)

            # Finding latitude and longitude
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']
            # print(lat, lng)

            # To get the pointer on a map
            map_location = folium.Map(location=[lat, lng], zoom_start=8)
            folium.Marker([lat, lng], popup=number_location).add_to(map_location)
            map_location.save("new_location.html")

            entry.delete(0, END)
            result_label = Label(window,
                                 text="Country: {}\n"
                                      "Service Provider: {}\n"
                                      "Phone Time Zone: {}\n"
                                      "Latitude: {}\n"
                                      "Longitude: {}".format(number_location, pint, time, lat, lng).replace(",",
                                                                                                            "").replace(
                                     "'", ""),
                                 width=55,
                                 height=5,
                                 font=("comic sans", 10, "bold"),
                                 justify="center")
            result_label.place(x=0, y=300)
            #
            webview.create_window('Number Location', 'new_location.html')
            webview.start()

        except:
            pass


label = Label(window,
              text="Enter Phone Number:",
              foreground="white",
              background="green",
              font=("comic sans", 15, "bold"))
label.place(x=30, y=80)
entry = Entry(window,
              width=23,
              font=("comic sans", 20, "bold"))
entry.place(x=30, y=120)

button = Button(window,
                width=10,
                text="Track\n"
                     "Number",
                font=("comic sans", 15, "bold"),
                background="indigo",
                foreground="white",
                command=track_phone)
button.place(x=130, y=230)
window.config(background="green")
window.geometry("420x420")
window.title("Number Tracker")
window.resizable(0, 0)
window.mainloop()
