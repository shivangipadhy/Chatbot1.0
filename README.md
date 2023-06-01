# ChatBot
This code is implementing a simple chatbot with a response system based on matching user input to predefined messages

#Built with 
the code contains two major libraries ,

re: This library is used for regular expressions. It allows you to work with patterns and perform operations like splitting strings based on a pattern, searching for specific patterns, and replacing patterns in strings.

long_responses: This appears to be a custom module that contains long response messages

#Getting started 
this is a simpler model, you can use your conversational style in the long responses. ans the chat bot will answer to questions like you would. 

You will need only basic pycharm or visualStudioCode or jupyter. 

The code imports the necessary modules: re for regular expressions and a module called long_responses.

The main function message_probability calculates the likelihood of a user message matching recognized words. It takes the user's message, a list of recognized words, and optional parameters single_response and required_words. It iterates over the words in the user's message and increments the message_certainity counter for each recognized word found. The percentage is calculated by dividing the message_certainity by the total number of recognized words. If the message contains all the required words or single_response is True, it returns the percentage multiplied by 100; otherwise, it returns 0.

The function check_all_messages is defined to evaluate multiple bot responses and determine the best match. It initializes an empty dictionary highest_prob_list to store response probabilities. The nested function response takes a bot response, a list of words to be recognized, and optional parameters single_response and required_words. It calculates the probability of the message matching the recognized words using message_probability and adds it to the highest_prob_list dictionary. The example responses provided in the code are "hello!", "hi", "sup", "hey", "heya", and "I'm doing fine and you?" with matching conditions for each.

The check_all_messages function returns the response with the highest probability by finding the key with the maximum value in highest_prob_list. The function prints highest_prob_list (presumably for debugging purposes) and returns the best match.

The get_response function processes user input by splitting it into a list of words using regular expressions and converting them to lowercase. It then calls check_all_messages with the split message and assigns the result to response.

FinaTlly, the code enters an infinite loop where it prompts the user for input, calls get_response with the input, and prints the response from the chatbot.

#Usage 
This chatbot is a project i made for fun!! , how ever if you have many fans and are unable to ansewer messages to all of them , you can send them the link after building the project.




