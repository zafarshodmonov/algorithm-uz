import requests
from github import Github

import json

from zatoken import TOKEN_ALGORITHM_UZ_BOT
from zaparol import git_hub_user_name, git_hub_password


zagithub = Github(git_hub_user_name, git_hub_password)

def sendMessage(text: str):
    params = {
        "chat_id": 735748607,
        "text": text
    }
    url = f'https://api.telegram.org/bot{TOKEN_ALGORITHM_UZ_BOT}/sendMessage'

    response = requests.get(url, params=params)

def sendDocument():
    params = {
        "chat_id": 735748607,
        "document": "BQACAgIAAxkBAAMDZScs4e7pkdi4GQABkb0jCD6jx_7iAAK1OAACemw5SSTI0ZD4YUkUMAQ",
         
        }
    url = f'https://api.telegram.org/bot{TOKEN_ALGORITHM_UZ_BOT}/sendDocument'
    response = requests.post(url, params=params)

# def sendPhoto(chat_id:str,photo:str):
#     params = {
#         "chat_id": chat_id,
#         "photo": photo
#     }
#     URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

#     response = requests.get(URL, params = params)
#     return response.json()

# last_message_id = -1

# while True:
#     updates = getUpdates()

#     message_id = updates[-1]['message']['message_id']
    
#     message = updates[-1]['message']
#     chat_id = updates[-1]['message']['chat']['id']

#     print(f"MESSAGE ID: {message_id}  LAST MESSAGE ID: {last_message_id}")

#     if message_id != last_message_id:
#         text = message.get('text')
#         photo = message.get('photo')
#         if text != None:
#             if text == "/start":
                
#                 sendMessage(chat_id, "welcome to bot!")
#             else:   
#                 sendMessage(chat_id, text)
#         elif photo != None:
#             file_id = photo[0]['file_id']
#             sendPhoto(chat_id, file_id)
#         else:
#             sendMessage(chat_id, f"other format")
#
#         last_message_id = message_id

#     sleep(2)

def main():
    sendDocument()
    pass

if __name__ == "__main__":
    main()
