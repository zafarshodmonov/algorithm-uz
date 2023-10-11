import requests

url = 'https://api.github.com/events'

response = requests.get(url)

def get_response_status_code(url: str | bytes) -> int:
    response = requests.get(url)
    return response.status_code

def get_response_json(url: str | bytes):
    response = requests.get(url)
    return response.json()

def get_response_url(url: str | bytes) -> str:
    payload = {
        "key": "value",
        "key1": "value1"
    }
    response = requests.get(url, params=payload)
    return response.url

def get_response_text(url: str | bytes) -> str:
    respons = requests.get(url)
    return respons.text

def get_response_encoding(url: str | bytes) -> str | None:
    response = requests.get(url)
    return response.encoding

def get_response_content(url: str | bytes) -> bytes:
    response = requests.get(url)
    return response.content


def main():
    # print(get_response_status_code(url))
    # print(get_response_json(url))
    # print(get_response_url(url))
    # print(get_response_text(url))
    # print(get_response_encoding(url))
    # print(get_response_content(url))

    pass

if __name__ == "__main__":
    main()
