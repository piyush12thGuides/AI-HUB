     # Load pre-trained model and tokenizer
     chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

     # Simple loop to interact with the chatbot
     print("Type 'quit' to exit.")
     while True:
         user_input = input("You: ")
         if user_input.lower() == 'quit':
             break
         response = chatbot(user_input)
         print(f"Bot: {response[0]['generated_text']}"
