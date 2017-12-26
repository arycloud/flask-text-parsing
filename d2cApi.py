from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/text')
def Text():
    return render_template('index.html')


@app.route('/parseText')
def Parsing():
            with open('/Users/abdul/PycharmProjects/d2cApi/some/description_0.txt', encoding='utf-8') as fo:
                lines = fo.readlines()
                data = []
                count = 0
                for line in lines:
                    if line != "\n" and line != "input":
                        data.insert(count, line)
                        count += 1
                jData = json.dumps(data)
                return jData


if __name__ == '__main__':
    app.run()
