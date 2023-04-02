from simfs2020 import *
import maprender as map
from nicegui import ui


#ui
@ui.page('/')
def main():
    container = ui.row()
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
        with ui.row():
            ui.button('Refresh Map', on_click=lambda: update_map())
            with container:
                ui.html('')
        ui.link('NiceGUI on Github', 'https://github.com/zauberzeug/nicegui')
        
        
        # Timers to handle simconnect refresh info & Folium refresh info
        ui.timer(interval=10.0, callback=lambda: oPlane.SimRender())
        ui.timer(interval=2.0, callback=lambda: map.Marker(oPlane.SimLatLon()))
        
        def update_map() -> None:
            if container:
                container.remove(0)
                with container:
                    map_render()
            else:
                with container:
                    map_render()
                    
                    
        def map_render() -> None:
                    oPlane = SimFs2020()
                    map.Marker(oPlane.SimLatLon()).get_root().width = f'{600}px'
                    map.Marker(oPlane.SimLatLon()).get_root().height= f'{300}px'
                    iframe = map.Marker(oPlane.SimLatLon()).get_root()._repr_html_()
                    ui.html(iframe).classes('w-full h-full')
        
    ui.add_body_html('<style>body{background-color: #dddddd}</style>')

ui.run(show=False, native=True, reload=False)

