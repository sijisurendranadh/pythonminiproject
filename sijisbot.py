from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
 
#creating a new chatbot
chatbot = ChatBot( 'Sijis')
trainer = ListTrainer(chatbot)
trainer.train([ 'hi, can I help you find a course', 'sure I\'d love to find you a course', 'your course have been selected'])
 
#getting a response from the chatbot
response = chatbot.get_response(input("Welcome to Sijis!!  How can I help you ?\n"))
print(response)