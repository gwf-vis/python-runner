import time
from flask import Flask, request, json
from flask_cors import CORS
import sys
import os
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/run', methods=['POST'])
def run():
    text = request.data.decode("utf-8")
    filePath = f'temp_{int(time.time() * 10000000)}.py'
    with open(filePath, 'w+') as file:
        file.write(text)
    resultFilePath = f'{filePath}.result'
    myEnv = os.environ
    myEnv['RESULT_FILE_PATH'] = resultFilePath
    output = subprocess.check_output(['python3', filePath], env=myEnv).decode("utf-8")
    os.remove(filePath)
    result = ''
    try:
        with open(resultFilePath) as file:
        result = file.read()
        os.remove(resultFilePath)
    except:
        pass
    return json.dumps({
        'output': output,
        'result': json.loads(result)
    })


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        port = 8000
    app.run(port=port, host="0.0.0.0")
