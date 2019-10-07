# IllusionalResult

自動取引は他の方々に任せ、各種仮想通貨の変動等を見れる支援ツール構築(予定)

## ServerSide
dockerを用いて構築

OS：fedora31

bottleを使用し、appへの情報提供サーバとする

### /アクセス
WebSocekt通信を開始させます
失敗の場合ステータスコード500を返す

### データ取得
/api/v1/tradebinにGETメソッドにてアクセスすると現状サーバが保有しているデータを取得できる

### データ要求
/api/v1/selectにPOSTメソッドにてアクセスし、json形式で欲しいデータを要求する
```
{"key" : <欲しい通貨名>,...}
```

### 接続終了
/api/v1/finにアクセスするとWebSocket通信を終了しBitMEXから切断する

## app

作成開始後記載予定

## 備忘録

### イメージ作成
```
docker build -t <任意の名称> .
```

### 起動
```
docker run -it <イメージ名>
```
