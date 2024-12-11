import requests
import json

#Random cat facts api
#print(response.status_code)
#print(response.json())
cat_response1 = requests.get('https://meowfacts.herokuapp.com/')
cat_response2 = requests.get('https://meowfacts.herokuapp.com/')
cat_response3 = requests.get('https://meowfacts.herokuapp.com/')
cat_response4 = requests.get('https://meowfacts.herokuapp.com/')
cat_response5 = requests.get('https://meowfacts.herokuapp.com/')

# random dog facts api
dog_response1 = requests.get('https://dog-api.kinduff.com/api/facts')
dog_response2 = requests.get('https://dog-api.kinduff.com/api/facts')
dog_response3 = requests.get('https://dog-api.kinduff.com/api/facts')
dog_response4 = requests.get('https://dog-api.kinduff.com/api/facts')
dog_response5 = requests.get('https://dog-api.kinduff.com/api/facts')


def jprint():
    text = json.dumps(response.json(), indent=4)
    print(text)

#json.loads('')
# see facts about cats
def num_catFacts():
    if user_inputCat == '1':
        print(f'Your fact is:\n{cat_response1.json()["data"][0]}')
    elif user_inputCat == '2':
        print(f'Your facts are:\n{cat_response2.json()["data"][0]}\n{cat_response1.json()["data"][0]}')
    elif user_inputCat == '3':
        print(f'Your facts are:\n{cat_response3.json()["data"][0]}\n{cat_response2.json()["data"][0]}\n{cat_response1.json()["data"][0]}')
    elif user_inputCat == '4':
        print(f'Your facts are:\n{cat_response4.json()["data"][0]}\n{cat_response3.json()["data"][0]}\n{cat_response3.json()["data"][0]}\n{cat_response1.json()["data"][0]}')
    elif user_inputCat == '5':
        print(f'Your facts are:\n{cat_response5.json()["data"][0]}\n{cat_response4.json()["data"][0]}\n{cat_response3.json()["data"][0]}\n{cat_response2.json()["data"][0]}\n{cat_response1.json()["data"][0]}')
    else:
        print('Invalid input. Please try again.')

# see facts about dogs
def num_dogFacts():
    if user_inputDog == '1':
        print(f'Your fact is:\n{dog_response1.json()["facts"][0]}')
    elif user_inputDog == '2':
        print(f'Your facts are:\n{dog_response2.json()["facts"][0]}\n{dog_response1.json()["facts"][0]}')
    elif user_inputDog == '3':
        print(f'Your facts are:\n{dog_response3.json()["facts"][0]}\n{dog_response2.json()["facts"][0]}\n{dog_response1.json()["facts"][0]}')
    elif user_inputDog == '4':
        print(f'Your facts are:\n{dog_response4.json()["facts"][0]}\n{dog_response3.json()["facts"][0]}\n{dog_response2.json()["facts"][0]}\n{dog_response1.json()["facts"][0]}')
    elif user_inputDog == '5':
        print(f'Your facts are:\n{dog_response5.json()["facts"][0]}\n{dog_response4.json()["facts"][0]}\n{dog_response3.json()["facts"][0]}\n{dog_response2.json()["facts"][0]}\n{dog_response1.json()["facts"][0]}')
    else:
        print('Invalid input. Please try again.')


if __name__ == '__main__':
    #get user input
    while True:
        user_input = input('Would you like to see facts about dogs or cats? Enter "c" or "d" to proceed. Enter q to quit: ')
        if user_input == 'c':
            user_inputCat = input('You can choose 1 - 5 facts. How many facts do you want? (press q to quit): ')
            while user_inputCat != 'q':
                num_catFacts()
                break
            else:
                print('Goodbye!')
        elif user_input == 'd':
            user_inputDog = input('You can choose 1 - 5 facts. How many facts do you want? (press q to quit): ')
            while user_inputDog != 'q':
                num_dogFacts()
                break
        elif user_input == 'q':
            print('Goodbye!')
            break
