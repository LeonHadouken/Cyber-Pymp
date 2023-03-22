from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
# Функция, которая перенаправляет вебхук с адреса http://127.0.0.1:5000/webhook по адресу в значении transfer
def handle_webhook(transfer):
    # получаем данные из запроса
    data = request.json
    print('message: Webhook received!')
    # перенаправляем данные на другой URL
    response = requests.post(transfer, json=data)
    # возвращаем ответ
    return response.content
if __name__ == '__main__':
    app.run(debug=True)