import requests

def main():
    # url = 'https://api.github.com/events'
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    print(response)

    pass

if __name__ == "__main__":
    main()
