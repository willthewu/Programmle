import ast
import string
import random

# initiate the game
def play(list_length=5):
    introduce(list_length) # prints stuff
    mystery = randomize(list_length)
    counter = 1
    keep_playing = True

    while keep_playing:
        integers, nones, booleans, strings, lists = count_types(mystery) # counts the amount of types in mystery
        guess = []
        check_list = ["FILLER" for i in range(len(mystery))] # creates proper # elements for check_list
        for guess_index in range(len(mystery)): # collect the guess
            guess.append(get_valid_input(guess_index))
            if guess[guess_index] == 'i give up':
                keep_playing = False
                print(f"Thanks for playing! The correct answer was {mystery}")
                break
        if keep_playing == False:
            break
        for item_index in range(len(guess)): # change the guess to the proper types
            guess[item_index] = change_type(guess[item_index]) 
        print(f"Guess: {guess}")
        for check_index in range(len(guess)): # checking the answer for fully correct and correct types
            if str(guess[check_index]) == str(mystery[check_index]): # an element is fully correct
                check_list[check_index] = "✅"
                if type(guess[check_index]) == type(1):
                    integers -= 1
                elif guess[check_index] == None:
                    nones -= 1
                elif type(guess[check_index]) == type(True):
                    booleans -= 1
                elif type(guess[check_index]) == type("hi"):
                    strings -= 1
                else:
                    lists -= 1
            elif type(guess[check_index]) == type(mystery[check_index]): # an element is wrong but type is correct
                if type(guess[check_index]) == type(1):
                    integers -= 1
                elif guess[check_index] == None:
                    nones -= 1
                elif type(guess[check_index]) == type(True):
                    booleans -= 1
                elif type(guess[check_index]) == type("hi"):
                    strings -= 1
                else:
                    lists -= 1
                check_list[check_index] = "🤏"

        for check_index_two in range(len(guess)): # checking the answer for incorrect placement 
            if check_list[check_index_two] != "FILLER":
                continue
            elif type(guess[check_index_two]) == type(1) and integers > 0:
                check_list[check_index_two] = "🔄"
                integers -= 1
            elif guess[check_index_two] == None and nones > 0:
                check_list[check_index_two] = "🔄"
                nones -= 1
            elif type(guess[check_index_two]) == type(True) and booleans > 0:
                check_list[check_index_two] = "🔄"
                booleans -= 1
            elif type(guess[check_index_two]) == type("hi") and strings > 0:
                check_list[check_index_two] = "🔄"
                strings -= 1
            elif type(guess[check_index_two]) == type([1,2]) and lists > 0:
                check_list[check_index_two] = "🔄"
                lists -= 1
            else:
                check_list[check_index_two] = "❌"
        print(f"Check: {check_list}")

        for message_element in range(len(check_list)):
            if check_list[message_element] == "🤏":
                if type(guess[message_element]) == type(1):
                    if guess[message_element] > mystery[message_element]: # hint for integer
                        print(f"Your guess for index {message_element} was too high!")
                    else:
                        print(f"Your guess for index {message_element} was too low!")
                elif type(guess[message_element]) == type(True):
                    print(f"Your guess for index {message_element} was close... Good thing booleans only have two values!")
                elif type(guess[message_element]) == type("hi"):
                    if abs(alphabet[guess[message_element][0]] - alphabet[mystery[message_element][0]]) <= 5 and abs(alphabet[guess[message_element][0]] - alphabet[mystery[message_element][0]]) > 0:
                        print(f"The first letter for the element in index {message_element} is within 5 indices in the alphabet.")
                    elif abs(alphabet[guess[message_element][0]] - alphabet[mystery[message_element][0]]) == 0:
                        pass
                    else:
                        print(f"The first letter for the element in index {message_element} is NOT within 5 indices in the alphabet.")

                    if abs(alphabet[guess[message_element][1]] - alphabet[mystery[message_element][1]]) <= 5 and abs(alphabet[guess[message_element][1]] - alphabet[mystery[message_element][1]]) > 0:
                        print(f"The second letter for the element in index {message_element} is within 5 indices in the alphabet.")
                    elif abs(alphabet[guess[message_element][1]] - alphabet[mystery[message_element][1]]) == 0:
                        pass
                    else:
                        print(f"The second letter for the element in index {message_element} is NOT within 5 indices in the alphabet.")
                elif type(guess[message_element]) == type([1,2]):
                    if len(guess[message_element]) < len(mystery[message_element]):
                        print(f"Your list for the element in index {message_element} is too short!")
                    elif len(guess[message_element]) > len(mystery[message_element]):
                        print(f"Your list for the element in index {message_element} is too long!")
                    else:
                        for i in range(len(guess[message_element])):
                            if guess[message_element][i] > mystery[message_element][i]:
                                print(f"For the list in index {message_element}, the {i}th element is too large!")
                            elif guess[message_element][i] < mystery[message_element][i]:
                                print(f"For the list in index {message_element}, the {i}th element is too small!")

        if guess == mystery:
            print(f"WOW! You guessed it correctly! It took you {counter} guesses!")
            keep_playing = False
        else:
            print("Looks like you were incorrect. Let's try again!")
            print("**********")
            counter += 1


            
            

def introduce(list_length):
    print(f"Welcome to Programmle! You will be given a list of length {list_length} and your goal is to figure out what is in each element of the list! The things that can be in the list can be a integer, None, boolean, string, or a list!")
    print("Restrictions: Strings will only have two lower case letters. Integers are from 0-100. Lists have 1-5 elements with integers 0-9. If you guess a string, do not use quotes. If you guess a list, please use [ and ] around the integers in the list.")
    print("Type in 'i give up' to reveal the answer.")
    print("Below shows what each symbol means when checking your answer.")
    print("✅: Everything at this index is correct!")
    print("🤏: The type you put in this spot is correct, but the value is incorrect. You will get a hint to help you find the correct value!")
    print("🔄: This type is somewhere in the solution, but you put it at the wrong spot.")
    print("❌: This type is not found anywhere else in the solution.")

    print("**********")

def change_type(guess):
    correct_type = ''

    if guess == 'i give up':
        return 'i give up'

    try:
        correct_type = 'integer' 
        new = int(guess) # test integer
    except: # test string
        correct_type = 'string'
    
    if guess == 'None' or guess == 'none' or guess == '': # test None
        correct_type = 'None' 
        return None
    
    elif guess[0] == '[' and guess[-1] == ']': # test list
        correct_type = 'list' 
        return ast.literal_eval(guess)
    
    elif guess == 'True' or guess == 'true': # test boolean
        correct_type = 'boolean'
        return True
    
    elif guess == 'False' or guess == 'false':
        correct_type = 'boolean'
        return False
    
    elif correct_type == 'integer':
        return int(guess)
    
    else:
        return guess
    
def count_types(input_list):
    integers = 0
    nones = 0
    booleans = 0
    strings = 0
    lists = 0
    for item in input_list:
        if type(item) == type(1):
            integers += 1
        elif item == None:
            nones += 1
        elif type(item) == type(True):
            booleans += 1
        elif type(item) == type("hello"):
            strings += 1
        else:
            lists += 1
    return integers, nones, booleans, strings, lists
    
# create a list of length num with random elements
def randomize(num):
    randomizer = [1 for i in range(num)]
    for counter in range(len(randomizer)):
        randomizer[counter] = random.randint(1, 5)
    for second_count in range(len(randomizer)):
        if randomizer[second_count] == 1:
            randomizer[second_count] = random.randint(0, 100)
        elif randomizer[second_count] == 2:
            randomizer[second_count] = None
        elif randomizer[second_count] == 3:
            if random.randint(1,2) == 1:
                randomizer[second_count] = True
            else:
                randomizer[second_count] = False
        elif randomizer[second_count] == 4:
            concat = ''
            for _ in range(2):
                value_to_find = random.randint(1,26)
                key = next((k for k, v in alphabet.items() if v == value_to_find), None)
                concat = concat + key
            randomizer[second_count] = concat
        else:
            new_length = random.randint(1,5)
            concat_list = [1 for i in range(new_length)]
            for index_i in range(len(concat_list)):
                concat_list[index_i] = random.randint(0,9)
            randomizer[second_count] = concat_list
    return(randomizer)

def get_valid_input(guess_index):
    while True:
        tried = input(f"Input your guess for the {guess_index}th element: ")
        if tried.lower() == 'i give up': # check give up case
            return 'i give up'
        elif tried.lower() == 'none': # check none case
            return tried
        elif tried == '':
            return tried
        elif tried[0] == '[' and tried[-1] == ']': # check list case
            try:
                can_return = True
                if len(ast.literal_eval(tried)) <= 5 and len(ast.literal_eval(tried)) > 0:
                    for element in ast.literal_eval(tried):
                        if element < 0 or element > 9:
                            can_return = False
                        if type(element) != type(1):
                            can_return = False
                    if can_return:
                        return str(tried)
                tried = str(tried)
            except:
                pass
        elif tried.lower() == 'true' or tried.lower() == 'false': # check bool case
            return tried
        else:
            try:
                tried = int(tried) # check int cases
                if tried >= 0 and tried <= 100:
                    return str(tried)
            except:
                if len(tried) == 2: # check string case
                    if tried[0].lower() in alphabet and tried[1].lower() in alphabet:
                        return tried.lower()
        print("That's not a valid input! Try again.")


    
        

    
    

        

# start the game
alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
#how_long = input("Give integer: ")
#play(how_long)
while True:
    try:
      length = int(input("How difficult do you want your game to be? (Number must be at least 1, 5 is recommended.): "))
      if length > 0:
        break
    except:
        pass
play(length)