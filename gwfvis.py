import os
from flask import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO

SERVER_ENDPOINT = 'http://localhost:5000'


def generate_vis(data):
    filePath = os.environ['RESULT_FILE_PATH']
    with open(filePath, 'w') as file:
        text = dumps_json(data)
        file.write(text)


def loads_json(data):
    return json.loads(data)


def dumps_json(data):
    return json.dumps(data)


def render_pyplot_figure():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    bufferValue = buffer.getvalue()
    buffer.close()
    b64 = base64.b64encode(bufferValue)
    b64String = b64.decode('utf-8')
    dataUrl = f'data:image/png;base64,{b64String}'
    print(dataUrl)

# config helpers

def load_default_vis_config():
    return {
        'imports': {
            'data-fetcher': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-data-fetcher.js',
            'tile-layer': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-tile-layer.js',
            'geojson-layer': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-geojson-layer.js',
            'user-selection': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-selection.js',
            'metadata': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-metadata.js',
            'line-chart': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-line-chart.js',
            'radar-chart': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-radar-chart.js',
            'dimension-control': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-dimension-control.js',
            'variable-control': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-variable-control.js',
            'legend': 'http://gwfvis.usask.ca/RiverFlow/api/file/fetch/public/plugins/default/gwf-vis-plugin-legend.js'
        },
        'plugins': {
            'data': {
                'name': 'data-fetcher',
                'props': {
                    'sqliteWorkerUrl': 'http://gwfvis.usask.ca/RiverFlow/assets/sqljs/worker.sql-wasm.js'
                }
            },
        }
    }

def add_plugin(vis_config, container, plugin_config):
    plugins = vis_config['plugins']
    if plugins is None:
        vis_config['plugins'] = {}
    if container == 'data':
        plugins['data'] = plugin_config
    else:
        plugin_container = plugins[container]
        if plugin_container is None:
            plugin_container = plugins[container] = []
        plugin_container.append(plugin_config)

DEFAULT_SATELITTE_LAYER = {
    'name': 'tile-layer',
    'props': {
        'name': 'Satelitte',
        'type': 'base-layer',
        'urlTemplate': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        'options': {
            'attribution': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
        }
    }
}