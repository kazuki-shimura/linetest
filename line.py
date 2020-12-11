import requests

#取得したトークン
TOKEN = 'P8PsUaDOnsVd9FpztlAJsJdVbDqJHp7xyEgsxPb1JbY'
#APIのURL
api_url = 'https://notify-api.line.me/api/notify'
#通知内容
send_contents = 'lineの通知だよ！'

#情報を辞書型にする
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}
print(TOKEN_dic)
print(send_dic)

requests.post(api_url, headers=TOKEN_dic, data=send_dic)