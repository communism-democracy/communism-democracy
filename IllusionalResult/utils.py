import json
import websocket
import logger
import os
import sys

# サーバとのやり取りを確認するための処理、確認不要の際はFalse
websocket.enableTrace(True)

# 接続先URIと各コールバック関数を引数に指定しWebSocketAppのインスタンスを作成
ws = websocket.WebSocketApp(url = 'wss://www.bitmex.com/realtime',
        on_open = on_open,
        on_message = on_message,
        on_close = on_close,
        on_error = on_error)

flag = False
data = {"key":"","data":""}

# サーバとの接続時に行う処理を記載
def on_open(ws):
        ws.run_forever()
        # BitMEXにpingを送りつける
        ws.send('ping')

        """
        不要な可能性が出てきたのでコメントアウトしておきましょうか…
        
        # セッションの有効時間をここでは仮に60秒とでもしておく(必要に応じて伸ばす予定)
        expires = int(time.time()) + 60
        # 決めた有効時間を送る処理でも考えますか(最悪初期値データとしてBitCoinのデータを購読しておいてもいいかも…)
        # 送るデータを変数authにでも記載しておきjson化して送信します
        ws.send(json.dumps(auth))
        """

# サーバからメッセージを受信した際の処理
def on_message(self, message: str):
        logger.debug('Receive message -> ' + message)

        # json形式からDictionary型への変換処理
        message = json.loads(message)
        
        # successnのキーが存在しかつ紐づく値がTrueであれば購読成功
        if 'success' in message and message['success'] and message['request']['op'] == 'subscride':
                # 購読成功時の処理
                for coins in message["data"]:
                        data["key"] = coins["synbol"]
                        coindata = {"open": coins["open"],"close": coins["close"], "high": coins["high"], "low": coins["low"]}
                        data["data"] = coindata

        elif message == "pong":
                # pongが返ってきた
                print("通信成功")
                flag == True
        else:
                print("通信エラーを確認、再起動します")
                flag == False
        

        
# エラー発生時に実行する処理
def on_error(ws, error):
        reload

# サーバとの切断時に実行する処理
def on_close(ws):
        ws.send('close')
        ws.close()

def reload():
        os.execv(sys.executable, [sys.executable] + sys.argv)

def start_socket():
        # WebSocket通信の開始
        ws.on_open = on_open
        if (flag == True):
                # 成功でpongが返ってきたはず…
                print("通信準備完了")
        else:
                print("errorが発生しています")
                reload

def get_item():
        # 現在変数に保管してあるデータ（json）を渡す
        print(data)
        return(data)

def select_item(items):
        # appサイドから要求のあった通過の1分足情報の購読
        # appから送られてきたjsonデータをDictionary型へ変換する
        items = json.loads(items)
        args = None
        # forループ回してitemの数だけ購読する送信データに加える
        for selecter in items.values():
                addItem = "tradeBin1m:" + selecter
                if args == None:
                        args += addItem
                else:
                        args += "," + addItem
        
        selectData = {"op": "subscride","args": [args]}
        # BitMEXに向けて送信
        ws.send(json.dumps(selectData))

def stop_socket():
        # bitMEXサーバとの通信切断用処理
        on_close

