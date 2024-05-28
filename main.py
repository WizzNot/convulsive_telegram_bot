from flask import Flask, request, jsonify
import telebot

token = open("bot_key.txt", "r").readline()
user_id = open("user_id.txt", "r").readline()

app = Flask(__name__)
bot = telebot.TeleBot(token)


@app.route('/checkout', methods=['POST'])
def accept_orders():
    data = request.get_json()
    
    order_info = "Заказ:\n" + \
        f"Имя: {data['name']}\n" + \
        f"Email: {data['email']}\n" + \
        f"Телефон: {data['phone']}\n" + \
        f"Товары: {data['items']}\n" + \
        f"Цена: {data['price']}"
    
    bot.send_message(user_id, order_info)
    return jsonify({"success": True, "message": "Заказ успешно принят"})

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    
    name = data['name']
    phone = data['phone']
    bot.send_message(user_id, f"С вами хотят связаться:\n{name}\n{phone}")
    return jsonify({"success": True, "message": "Запрос на контакт успешно отправлен"})

if __name__ == '__main__':
    app.run()
