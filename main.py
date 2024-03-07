from email import message
import cohere

#setup cohere client
co = cohere.Client('first_trial_key')

# chat_history = []
# max_turns = 10

# for _ in range(max_turns):
# 	# get user input
# 	message = input("Send the model a message: ")
	
# 	# generate a response with the current chat history
# 	response = co.chat(
# 		message,
# 		temperature=0.8,
# 		chat_history=chat_history
# 	)
# 	answer = response.text
		
# 	print(answer)

# 	# add message and answer to the chat history
# 	user_message = {"user_name": "User", "text": message}
# 	bot_message = {"user_name": "Chatbot", "text": answer}
	
# 	chat_history.append(user_message)
# 	chat_history.append(bot_message)

#Call the endpoint via the co.chat()
response = co.chat(
  chat_history=[
    {"role": "USER", "message": "Who discovered gravity?"},
    {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
  ],
  message="What year was he born?",
  # perform web search before answering the question. You can also use your own custom connector.
  connectors=[{"id": "web-search"}]
)
print(response)


