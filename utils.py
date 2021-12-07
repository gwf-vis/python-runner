import os
from flask import json
import requests

SERVER_ENDPOINT = 'http://localhost:5000'


def obtainFileContent(path: str):
    fileUrl = f'{SERVER_ENDPOINT}/files/{path}'
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
