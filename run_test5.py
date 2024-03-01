# run_main.py
import json
import time
import re
import sys
import pandas as pd
from test8 import get_response

def banking_bot(user_message):
    # Load data from JSON
    with open('data.json', 'r') as f:
        data = json.load(f)

    usernames = data['usernames']
    username1 = data['username1']
    username2 = data['username2']
    amount = data['amount']
    authorization_code = data['auth']

    # Load balances from CSV
    df = pd.read_csv('balances.csv')

    while True:
        try:        
            response = get_response(usernames, user_message)
            response_dict = json.loads(response)
            intent = response_dict['Intent'].lower()  # Convert the intent to lowercase
            username = response_dict['Creds']['username']
            if intent == 'greetings':
                if username in usernames:
                    username1 = username
                    data['username1'] = username1
                    # Save the updated data to the JSON
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    return f'Hi {username}, how may I help you?'
                else:
                    return 'Hi! please tell your username'
            elif username1 != "":
                auth = input("Please enter your authorization code: ")
                if df.loc[df['username'] == username1, 'auth'].values[0] == auth:
                    if intent == 'check balance':
                        if username1 in usernames:
                            balance = df.loc[df['username'] == username1, 'amount'].values[0]
                            return f'Your current balance is {balance}.'
                        else:
                            return 'Username not found.'
                    elif intent == 'transfer money' and username in usernames:
                        username2 = username
                        data['username2'] = username2
                        # Extract the integer from the user message
                        numbers = re.findall(r'\d+', user_message)
                        if numbers:
                            amount = int(numbers[0])  # Convert the first number found in the user message to int
                            data['amount'] = amount
                            # Update balances in the DataFrame
                            df.loc[df['username'] == username1, 'amount'] -= amount
                            df.loc[df['username'] == username2, 'amount'] += amount
                            # Save the updated balances to the CSV
                            df.to_csv('balances.csv', index=False)
                            # Save the updated data to the JSON
                            with open('data.json', 'w') as f:
                                json.dump(data, f)
                            balance = df.loc[df['username'] == username1, 'amount'].values[0]
                            return f'Transferred {amount} from {username1} to {username2}. Your final balance is {balance}'
                else:
                    return 'Invalid Authorization Code! Please restart the server.'
        except Exception as e:
            # print(f"An error occurred while running main.py: {e}. Retrying...")
            time.sleep(1)  # Optional: wait for 5 seconds before retrying
