# Name: Makenzie Totushek
# Date: 3/20/26
# Title: Capital Quiz

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random
stateCapitals = {'Alabama': 'Montgomery',
                 'Alaska': 'Juneau',
                 'Arizona': 'Phoenix',
                 'California': 'Sacramento',
                 'Colorado': 'Denver',
                 'Connecticut': 'Hartford',
                 'Delaware': 'Dover',
                 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta',
                 'Hawaii': 'Honolulu',
                 'Idaho': 'Boise',
                 'Illinois': 'Springfield',
                 'Indiana': 'Indianapolis',
                 'Iowa': 'Des Moines',
                 'Kansas': 'Topeka',
                 'Kentucky': 'Frankfort',
                 'Louisiana': 'Baton Rouge',
                 'Maine': 'Augusta',
                 'Maryland': 'Annapolis',
                 'Massachusetts': 'Boston',
                 'Michigan': 'Lansing',
                 'Minnesota': 'Saint Paul',
                 'Mississippi': 'Jackson',
                 'Missouri': 'Jefferson City',
                 'Montana': 'Helena',
                 'Nebraska': 'Lincoln',
                 'Nevada': 'Carson City',
                 'New Hampshire': 'Concord',
                 'New Jersey': 'Trenton',
                 'New Mexico': 'Santa Fe',
                 'New York': 'Albany',
                 'North Carolina': 'Raleigh',
                 'North Dakota': 'Bismarck',
                 'Ohio': 'Columbus',
                 'Oklahoma': 'Oklahoma City',
                 'Oregon': 'Salem',
                 'Pennsylvania': 'Harrisburg',
                 'Rhode Island': 'Providence',
                 'South Carolina': 'Columbia',
                 'South Dakota': 'Pierre',
                 'Tennessee': 'Nashville',
                 'Texas': 'Austin',
                 'Utah': 'Salt Lake City',
                 'Vermont': 'Montpelier',
                 'Virginia': 'Richmond',
                 'Washington': 'Olympia',
                 'West Virginia': 'Charleston',
                 'Wisconsin': 'Madison',
                 'Wyoming': 'Cheyenne'}
def quiz():
    random_key, random_value = random.choice(list(stateCapitals.items()))
    # print(f"State: {random_key}")  # , random_value)
    # print(stateCapitals)
    return random_key, random_value


if __name__ == "__main__":
    print('This is a five question quiz on the US States and Capitals.')
    total_correct = 0
    total_incorrect = 0
    for i in range (5):
        state, capital = quiz()
        answer = input(f'What is the capital of {state}: ')
        if answer.upper() == capital.upper():
            print('That is correct!')
            total_correct += 1
        else:
            print(f'That is incorrect! The correct answer is {capital}.')
            total_incorrect += 1

    print(f'Your total of correct answers is {total_correct}')
    print(f'Your total of incorrect answers is {total_incorrect}')