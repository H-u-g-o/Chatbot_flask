from flask import Flask, render_template
import bot

app = Flask(__name__)

#@app.route('/')
#def bonjour():
#    return "BobOt: Bonjour ! Je m'appel BoBot.\n Demandes-moi ce que tu veux sur la promo Data IA. Si tu veux partir, écris q!"

@app.route('/')
def christine():
    return render_template('home.html')

@app.route('/<quest>')
def profile(quest):
    return bot.bobot(quest)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == "__main__":
    app.run()