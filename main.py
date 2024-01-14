from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('Bullet')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

from chatterbot.trainers import ListTrainer
trainer = ListTrainer(chatbot)
trainer.train([
               "what is your name",
               "my name is bullet"
  ])

print("What type of interface you want?")
interface=int(input("1.TERMINAL 2.WEB USING FLASK\n"))

if(interface==1):
    name=input("Enter Your Name: ")
    print("Helloo I m Bullet! Ask me ")
    while True:
        request=input(name+':')
        if request=='Bye' or request =='bye':
          print('Bot: Bye')
          break
        else:
          response=chatbot.get_response(request)
          print('Bot:',response)
 
     

if(interface==2):
   app=Flask(__name__,template_folder='template')
   @app.route('/')
   def home():
      return render_template("index.html")

   @app.route('/get_response', methods=['POST'])
   def get_response():
      user_message = request.form['user_message']
    
    # Get a response from the chatbot
      response_message = chatbot.get_response(user_message).text
    
      return jsonify({'response': response_message})
   if __name__ == '__main__':
       app.run()

    



