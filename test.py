from nicegui import ui
from simfs2020 import *

with ui.header().classes('bg-slate-500'):
    ui.label('Fs2020 Tracker').classes('w-full text-center')
with ui.column():
    ui.label('Altitude: ').style('color: #888; font-weight: bold')
    ui.label('Speed: ').style('color: #888; font-weight: bold')
    ui.label('Longitude: ').style('color: #888; font-weight: bold')
    ui.label('Latitude: ').style('color: #888; font-weight: bold')
    
    ui.link('NiceGUI on Github', 'https://github.com/zauberzeug/nicegui')
        
ui.add_body_html('<style>body{background-color: #dddddd}</style>')
ui.run(show=False, native=True)
oPlane = SimFs2020()
oPlane.SimRender()
