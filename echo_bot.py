import requests
import json
from zatoken import TOKEN_algorithm_uz_bot
import zarequests
# from time import sleep

def get_response_json(url) -> dict:
    response = requests.get(url)
    updates = response.json() # ['result']
    return updates

def f(data, path, indent = None) -> None:
    with open(path, "w") as f:
        if indent is None:
            json.dump(data, f)
        else:
            json.dump(data, f, indent=4)


def sendMessage(chat_id: str, text: str, ):
    params = {
        "chat_id": chat_id,
        "text": text
    }
    url = f'https://api.telegram.org/bot{""}/sendMessage'

    response = requests.get(url, params=params)

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

#         last_message_id = message_id

#     sleep(2)

def main():
    # url = f'https://api.telegram.org/bot{TOKEN_algorithm_uz_bot}/getUpdates'
    # response = zarequests.response_raise_for_status()
    url1 = "https://github.com/backend-2023J/echo-bot/blob/main/README.md/"
    url2 = "https://github.com/backend-2023J/echo-bot/blob/main/README.md#echo-bot"
    data = zarequests.get_response_text(url2)
    with open("README.md", "w") as f:
        f.write(data)

    pass

if __name__ == "__main__":
    main()
