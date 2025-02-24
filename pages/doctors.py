import streamlit as st
import streamlit.components.v1 as components

GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"     

st.set_page_config(page_title="Find Doctors Near Me", page_icon="🩺", layout="centered")

st.title("🩺 Find Doctors Near You")
st.write("This app detects your **live location** and fetches **nearby doctors & clinics**.")

map_js = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}&libraries=places"></script>
    <script>
        function initMap() {{
            if (navigator.geolocation) {{
                navigator.geolocation.getCurrentPosition(position => {{
                    var lat = position.coords.latitude;
                    var lng = position.coords.longitude;
                    
                    document.getElementById("latitude").value = lat;
                    document.getElementById("longitude").value = lng;

                    var map = new google.maps.Map(document.getElementById('map'), {{
                        center: {{ lat: lat, lng: lng }},
                        zoom: 14
                    }});

                    var userMarker = new google.maps.Marker({{
                        position: {{ lat: lat, lng: lng }},
                        map: map,
                        title: "Your Location",
                        icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
                    }});

                    var service = new google.maps.places.PlacesService(map);
                    var request = {{
                        location: new google.maps.LatLng(lat, lng),
                        radius: 5000,
                        keyword: document.getElementById("specialty").value
                    }};

                    service.nearbySearch(request, function(results, status) {{
                        if (status === google.maps.places.PlacesServiceStatus.OK) {{
                            for (var i = 0; i < results.length; i++) {{
                                (function(place) {{
                                    var marker = new google.maps.Marker({{
                                        position: place.geometry.location,
                                        map: map,
                                        title: place.name
                                    }});

                                    // Click Event for Interactive Markers (Redirects to Correct Google Maps Location)
                                    marker.addListener('click', function() {{
                                        window.open("https://www.google.com/maps/search/?api=1&query=" + place.geometry.location.lat() + "," + place.geometry.location.lng());
                                    }});
                                }})(results[i]); // IIFE to properly scope variables
                            }}
                        }}
                    }});
                }}, error => {{
                    document.getElementById("error").innerText = "⚠️ Location access denied! Enable permissions.";
                }});
            }} else {{
                document.getElementById("error").innerText = "⚠️ Geolocation is not supported by this browser.";
            }}
        }}
    </script>
</head>
<body onload="initMap()">
    <form>
        <input type="hidden" id="latitude" name="lat">
        <input type="hidden" id="longitude" name="lng">
        <select id="specialty" onchange="initMap()">
            <option value="hematologist">Hematologist</option>
            <option value="general physician">General Physician</option>
            <option value="pediatrician">Pediatrician</option>
            <option value="cardiologist">Cardiologist</option>
            <option value="dermatologist">Dermatologist</option>
            <option value="endocrinologist">Endocrinologist</option>
        </select>
    </form>
    <div id="map" style="height: 500px; width: 100%;"></div>
    <div id="error" style="color: red;"></div>
</body>
</html>
"""
components.html(map_js, height=600)

if st.button("🔙 Back to Home"):
    st.switch_page("app.py") 
