
import multiprocessing
import os
import signal
import tempfile

from nicegui import ui
import webview

ui.icon('thumb_up')
ui.markdown()
ui.html('This is <strong>HTML</strong>.').classes('bg-red')
with ui.row():
    ui.label('CSS').style('color: #888; font-weight: bold')
    ui.label('Tailwind').classes('front-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on Github', 'https://github.com/zauberzeug/nicegui')

ui.add_body_html('<style>body {background-color: red}')
ui.run(show=False, native=True)
