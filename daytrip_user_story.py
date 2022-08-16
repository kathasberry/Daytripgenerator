
import random



places_to_go = ['New york', 'Seattle', 'New Orleans', 'Houston']

things_to_eat = ['Eleven Madison park', 'Sushi Kashiba', 'GW Fins', 'State of Grace']

getting_there = ['Taxi', 'Double Decker bus', 'Train', 'Plane']

fun_fun_fun = ['Escape the room', 'Portal Virtual Reality', 'Aquarium', "Funplex"]
 

random_destination = random.choice(places_to_go)
random_resturant = random.choice(things_to_eat)
random_transport = random.choice(getting_there)
random_entertainment = random.choice(fun_fun_fun)



def  user_choosed_destination(list_of_dest, str_choice):
    print(f'Welcome and Thankyou for choosing Happy Trips for all your day trip needs! Today we have a very special trip planned for your convenience. The destination we have choosen for you today will be a nice trip to {str_choice}!')
    user_likes_dest = False 
    while user_likes_dest == False:
        user_input = input("Would this be satisfactory? Y/N ")
        if user_input == 'Y':
            print('Thankyou for your selection. Now let us find a mode of transportation!')
            print("")
            user_likes_dest = True
        elif user_input == 'N':
            str_choice = random.choice(list_of_dest)
            print(f'Im so sorry you didnt like that destination. How about we try {str_choice}?')
    return str_choice

final_destination = user_choosed_destination(places_to_go, random_destination)


def  user_choosed_transportation(list_of_trans, str_choice_trans):
    print(f'Now that we have the destination, how about we find a way to get there? We have choosen for you a nice ride in a {str_choice_trans} for your convience!')
    user_likes_trans = False 
    while user_likes_trans == False:
        user_input = input("Would this be satisfactory? Y/N ")
        if user_input == 'Y':
            print('Thankyou for your selection. Now for the food while you are out!')
            print("")
            user_likes_trans = True
        elif user_input == 'N':
            str_choice_trans = random.choice(list_of_trans)
            print(f'Im so sorry you didnt like that mode of transportation. How about we try {str_choice_trans}?')
    return str_choice_trans

final_transportation = user_choosed_transportation(getting_there, random_transport)

def  user_choosed_resturant(list_of_rest, str_choice_rest):
    print(f'For the nights enjoyment you will be dinning like Royalty at {str_choice_rest}!')
    user_likes_rest = False 
    while user_likes_rest == False:
        user_input = input("Would this be satisfactory? Y/N ")
        if user_input == 'Y':
            print('Thankyou for your selection. Lastly you will want some fun added to the extravagent evening!')
            print("")
            user_likes_rest = True
        elif user_input == 'N':
            str_choice_rest = random.choice(list_of_rest)
            print(f'Im so sorry you didnt like that selection of resturant. How about we try {str_choice_rest}?')
    return str_choice_rest

final_resturant = user_choosed_resturant(things_to_eat, random_resturant)

def  user_choosed_entertainment(list_of_ent, str_choice_ent):
    print(f'For the last part of your trip we will be providing an exclusive event for you at the {str_choice_ent}!')
    user_likes_ent = False 
    while user_likes_ent == False:
        user_input = input("Would this be satisfactory? Y/N ")
        if user_input == 'Y':
            print('Thankyou for your selection. Get ready for a night to remember!')
            print("")
            user_likes_ent = True
        elif user_input == 'N':
            str_choice_ent = random.choice(list_of_ent)
            print(f'Im so sorry you didnt like that selection. How about we try {str_choice_ent}?')
    return str_choice_ent

final_entertainment = user_choosed_entertainment( places_to_go, random_entertainment)

list_of_trip = [final_destination, final_transportation, final_resturant, final_entertainment]

print(f'So for your Day trip you will be taking a luxury {list_of_trip[1]} to {list_of_trip[0]} for some fun and relaxation! ')
print(f'There you will enjoy a nice time sightseeing before you go on a fun adventure to The {list_of_trip[3]}!')
print(f'After that we hope you have worked up an appetite because you will be dining like Kings and Queens in the amazing Five Star {list_of_trip[2]}')
print('I hope you enjoy your amazing day and please feel free to tell us about your experience! Have FUN!!!')

