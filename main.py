from simfs2020 import *
import maprender as map
from nicegui import ui

#ui
@ui.page('/')
def main():
    oPlane = SimFs2020()
    with ui.header().classes('bg-slate-500'):
        ui.label('Fs2020 Tracker').classes('w-full text-center')
    with ui.column():
        with ui.row():
            ui.label('Timestamp').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'date')
        with ui.row():
            ui.label('Altitude: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'altitude')
        with ui.row():
            ui.label('Speed: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'speed')
        with ui.row():
            ui.label('Longitude: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'lon')
        with ui.row():
            ui.label('Latitude: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'lat')
    
        ui.link('NiceGUI on Github', 'https://github.com/zauberzeug/nicegui')
        
        # Timers to handle simconnect refresh info & Folium refresh info
        ui.timer(interval=10.0, callback=lambda: oPlane.SimRender())
        ui.timer(interval=10.0, callback=lambda: map.Marker(oPlane.SimLatLon()))
        
    ui.add_body_html('<style>body{background-color: #dddddd}</style>')


ui.run(show=False, native=True)

