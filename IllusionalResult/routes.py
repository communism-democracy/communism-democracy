from bottle import route, response, abort, request
from utils import *

@route('/', method = ['GET', 'POST'])
def api_stert():
    try:
        # 成功でWebSocket通信を開始
        response.headers['Content-Type'] = 'application/json'
        return stert_socket()
    except:
        # 失敗でステータスコード500(サーバエラー)を返す
        abort(500)

@route('/api/v1/tradebin', method = 'GET')
def api_request():
    try:
        # 成功で変数内に保持されたデータをappへ送る
        response.headers['Content-Type'] = 'application/json'
        if request.method == 'GET':
            # GETメソッドできた場合データを渡す
            return get_item()
        else:
            # GET以外のメソッドであればステータスコード405(許可されていないメソッド)を返す
            abort(405)
    except:
        # 失敗でステータスコード500を返す
        abort(500)

@route('/api/v1/select', method = 'POST')
def api_select(items):
    try:
        # 成功で購読する通貨を決定させる
        responce.header['Content-Type'] = 'application/json'
        if request.method == 'POST':
            # POSTメソッドでのアクセスの場合変更を受け付ける
            return select_item(items)
        else:
            # POST以外であればステータスコード405を返す
            abort(405)
    except:
        # 失敗でステータスコード500を返す
        abort(500)

@route('/api/v1/fin', method = ['POST', 'GET'])
def api_stop:
    try:
        # 成功でWebSocket通信を終了させる
        return stop_socket()
    except:
        # 失敗でステータスコード500を返す
        abort(500)
