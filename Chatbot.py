from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Lakshmi Kiranmai 
chatbot = ChatBot('MyChatterbotx')

trainer = ListTrainer(chatbot)

trainer.train(['Hey Hi','Hello','How are you.?','I am fine and You.?','Great','What are you Doing.?','nothing just thinking on being productive.'])

while True:
	input_data = input("You- ")
	response = chatbot.get_response(input_data)
	print("MyChatterbotx- ",response)

