from flask import Flask, render_template, request

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
bot = ChatBot("Pikachu")
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'My name is Pikachu'])
trainer.train(['How are you?', 'I am good' ])
trainer.train(['Bye?', 'Bye, see you later' ])
trainer.train(['hello', 'Hi, please write your questions'])
trainer.train(['Can I ask you few question ?', 'Yes' ])
trainer.train(['I need new sneakers', 'Hi, happy to help you with that, Are you just starting out, run regularly or are you already pretty experienced?' ])
trainer.train(['I am a newbie', 'So, where are you going to use your new sneakers? On the street, on uneven ground or at the gym?' ])
trainer.train(['On the street', 'Just go to the search option and type "Basic sneakers"' ])
trainer.train(['I need a tshirt', 'Just go to the search option and type tshirt and after that you can filter according to your needs.' ])
trainer.train(['How to go to the clothing section?','Select the clothing option or use the voice button to say "clothing".'])
trainer.train([' How to go to the home decor section?','Select the home decor option or use the voice button to say "Home decor".'])
trainer.train([' How to go to the electronics section?',' Select the electronics option or use the voice button to say "Electronics".'])

trainer.train(['How to go to the grocery section?','Select the grocery option or use the voice button to say "grocery".'])
trainer.train(['How to enable colorblind option?','Take the colorblind test by click on the toggle button and it will be enabled according to your type of colorblindness.'])
@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run(host= '0.0.0.0')


