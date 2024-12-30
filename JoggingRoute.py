from tkinter import Toplevel, Label, Listbox, Scrollbar

def JoggingRoute():
    # Create a new window for displaying jogging routes
    route_window = Toplevel()
    route_window.title("Jogging Routes")
    route_window.geometry("400x300")

    # Header label
    Label(route_window, text="Available Jogging Routes", font=("Arial", 16)).pack(pady=10)

    # Scrollable list of routes
    scrollbar = Scrollbar(route_window)
    scrollbar.pack(side="right", fill="y")

    route_listbox = Listbox(route_window, font=("Arial", 12), yscrollcommand=scrollbar.set, width=50)
    routes = [
        "1. Lake Trail - 2 km (Easy)",
        "2. Campus Perimeter - 5 km (Moderate)",
        "3. Forest Track - 7 km (Challenging)",
        "4. Evening Stroll - 1 km (Relaxed)",
        "5. Hill Loop - 4 km (Moderate to Hard)"
    ]

    for route in routes:
        route_listbox.insert("end", route)

    route_listbox.pack(padx=10, pady=10, fill="both", expand=True)
    scrollbar.config(command=route_listbox.yview)

    # Close button
    Label(route_window, text="Choose the route that suits your preference!", font=("Arial", 12, "italic")).p


import folium
import webbrowser
from tkinter import *


def JoggingRoute():
    # Create a map centered around a specific location (e.g., UMPSA)
    map_center = [3.724557993583096, 103.12370589881438]  # Example: Coordinates for UMPSA (Replace with your location)
    my_map = folium.Map(location=map_center, zoom_start=15)

    # Define the coordinates for the route
    route_coords = [
        [3.725286013179642, 103.1240492215694],  # Start Point (e.g., UMPSA)
        [3.719622432975618, 103.12323383003782],  # Midpoint
        [3.7189051149308, 103.12274030358886],  # Another point on the route
        [3.718466158824434, 103.12152794513808]  # End Point
    ]

    # Add the route (line) to the map
    folium.PolyLine(route_coords, color="blue", weight=4, opacity=0.7).add_to(my_map)

    # Add markers at the start and end points
    folium.Marker([3.725286013179642, 103.1240492215694], popup="Start Point").add_to(my_map)
    folium.Marker([3.718466158824434, 103.12152794513808], popup="End Point").add_to(my_map)

    # Save the map to an HTML file
    map_file = 'jogging_route_map.html'
    my_map.save(map_file)

    # Open the generated map in the default web browser when the button is pressed
    webbrowser.open(map_file)

