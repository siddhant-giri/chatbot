from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")
bot.set_trainer(ListTrainer)
bot.train(['What is your name?', 'My name is Candice'])
bot.train(['Who are you?', 'I am a bot'])
bot.train(['who created you?', 'Tony stark'])
bot.train(['which planet?', 'earth'])

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    a = str(bot.get_response(userText))
    return a




if __name__ == "__main__":
    app.run()
