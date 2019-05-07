from flask import Flask
import bot

app = Flask(__name__)

@app.route('/')
def bonjour():
    return "BobOt: Bonjour ! Je m'appel BoBot.\n Demandes-moi ce que tu veux sur la promo Data IA. Si tu veux partir, écris q!"

@app.route('/<quest>')
def profile(quest):
    return bot.bobot(quest)

if __name__ == "__main__":
    app.run()