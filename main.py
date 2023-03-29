from simfs2020 import *
import maprender as map
from nicegui import ui


@ui.page('/')
def main():
    oPlane = SimFs2020()
    oPlane.SimRender()
    with ui.header().classes('bg-slate-500'):
        ui.label('Fs2020 Tracker').classes('w-full text-center')
        ui.button('Update Data', on_click=lambda: oPlane.SimRender())
    with ui.column():
        with ui.row():
            ui.label('Altitude: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'altitude')
        with ui.row():
            ui.label('Speed: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'speed')
        with ui.row():
            ui.label('Longitude: ').style('color: #888; font-weight: bold')
            ui.label().bind_text_from(oPlane, 'latlon')
        ui.label('Latitude: ').style('color: #888; font-weight: bold')
    
        ui.link('NiceGUI on Github', 'https://github.com/zauberzeug/nicegui')

    ui.add_body_html('<style>body{background-color: #dddddd}</style>')
    


ui.run(show=False, native=True)


