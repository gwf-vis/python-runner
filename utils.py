import os
from typing import Any, List, Union
from flask import json
import requests

SERVER_ENDPOINT = 'http://localhost:5000'


def obtainFileContent(path: str):
    fileUrl = os.path.join(SERVER_ENDPOINT, 'files', path)
    return requests.get(fileUrl).content.decode("utf-8")


def generateVis(data):
    filePath = os.environ['RESULT_FILE_PATH']
    with open(filePath, 'w') as file:
        text = dumpsJSON(data)
        file.write(text)


def loadsJSON(data):
    return json.loads(data)


def dumpsJSON(data):
    return json.dumps(data)


def loadsDataIndex(path: str):
    fileContent = obtainFileContent(path)
    dataIndex = loadsJSON(fileContent)
    dataIndex['directoryPath'] = os.path.dirname(path)
    return dataIndex


def loadsGeoData(dataIndex):
    directoryPath = dataIndex['directoryPath']
    geoJSONRelativePath = dataIndex['geoJSON']
    fileContent = obtainFileContent(os.path.join(directoryPath, geoJSONRelativePath))
    return loadsJSON(fileContent)

def useMainPlugin(indexPath: str):
    data = {}
    data['pluginIndexUrl'] = indexPath
    return data

def setPluginProperty(toPlugin: dict, name: str, data):
    if toPlugin is None:
        return
    toPlugin[name] = data

def addPlugin(toPlugin: dict, name: str):
    if toPlugin is None:
        return
    if('plugins' not in toPlugin):
        toPlugin['plugins'] = []
    plugin = {
        'name': name
    }
    toPlugin['plugins'].append(plugin)
    return plugin
