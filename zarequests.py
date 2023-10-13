import requests

def main() -> None:
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
if __name__ == "__main__":
    main()
