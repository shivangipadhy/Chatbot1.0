import re
import long_responses as long

def message_probabability(user_message, recognised_words, single_response= False, required_words =[])):
message_certainity = 0
has_required_words = True

for word in user_message:
    if word in recognized_words:
    message_certainity +=1
#calculate the percentage of recognised words in a user message
percentage = float(message_certainity) / float(len(recognized_words))


    for word in has_required_words:
        if word not in user_message:
        has_required_words = False
        break

    if has_required_words or single response:
        return int(percentage*100)
else:
    return 0

def check_all_messages(message):
    hughest_prob_list ={}

    def respone(bot_reponse, list_of_worse, single_response =False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list(bot-response) = message_probability(message, list_of_words, single_response, required_words)

        #responinse ------------------
        response("hello!", 'hi', 'sup', 'hey', 'heya'], single_response = True)
        response('i \'m doing fine and you?',['how' ,'are', 'you', 'doing'],required_words =['how'])

        best_match =max(highest_prob_list, key=highest_prob_list.get())
        print(highest_prob_list)

        return best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*'), user_input.lower())
    response: None = check_all_messages(Split_message)
    return response


#testing the response system
while True:
    print('Bot:'+ get_response(input('You:')))