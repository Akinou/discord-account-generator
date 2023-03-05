import requests
import names
import random

emails = ['email1@example.com', 'email2@example.com', 'email3@example.com']

for email in emails:
    name = names.get_full_name()
    username = name.replace(" ", "")
    password = str(random.randint(100000,999999))
    
    response = requests.post('https://discord.com/api/v9/auth/register', json={
        'email': email,
        'username': username,
        'password': password,
        'invite': None,
        'consent': True,
        'date_of_birth': '1990-01-01',
        'gift_code_sku_id': None
    })

    if response.status_code == 200:
        print(f'Account created for {email}')
    else:
        print(f'Failed to create account for {email}')
