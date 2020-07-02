import os
import sys
from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# TODO: 同じZOOM_TOKEN_URLを使って、再度起動したときには、前回実行の続きの値を初期値にする必要あり
sub_id = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comment')
def comment():
    global sub_id
    v = request.args["value"]

    url = "{}&lang=jp-JP&seq={}".format(os.environ["ZOOM_TOKEN_URL"], sub_id)
    resp = requests.post(url, data=v.encode('utf-8'))
    sub_id += 1
    print("sub_id: {}".format(sub_id))

    return "OK", 200


if __name__ == "__main__":
    if "ZOOM_TOKEN_URL" not in os.environ:
        print("Zoomミーティング画面中の字幕より、APIトークンをコピーし、ZOOM_TOKEN_URLの環境変数にセット後、再実行してください")
        sys.exit()

    app.run(debug=True)

