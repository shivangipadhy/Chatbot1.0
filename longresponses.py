import random

R_EATING = "I dont like to eat anything because the food in hostel is bad obviously!"





def unknown():
    response = ['could you please re-phrase that?'
                "" 
                "sounds about right",
                "what does that mean?"][random.randrange(4)]
    return response