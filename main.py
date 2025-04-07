import os

from flask import Flask, jsonify, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio Credentials
twilio_sid = os.environ['TWILIO_SID']
twilio_token = os.environ['TWILIO_TOKEN']
twilio_from = "whatsapp:+14155238886"

# Twilio Client
client = Client(twilio_sid, twilio_token)


@app.route('/')
def health():
    return jsonify({'status': 'ok'})


def enviar_mensagem(to: str, body: str):
    client.messages.create(from_=twilio_from, body=body, to=to)


@app.route('/receive', methods=['POST'])
def receive():
    data: dict = request.form.to_dict()
    print(data)
    # Apresenta o Menu
    if data['Body'].lower() == 'menu':
        message_body = "Escolha uma opção:\n1. Opção 1\n2. Opção 2\n3. Opção 3"
        enviar_mensagem(data['From'], message_body)
    else:
        message_body = "Opção inválida. Digite 'menu' para ver as opções disponíveis."
        enviar_mensagem(data['From'], message_body)
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
