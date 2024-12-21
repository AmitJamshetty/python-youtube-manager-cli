import requests
import certifi

def fetch_random_user_freeapi():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()

    if "results" in data:
        user_data = data["results"]
        username = data['results'][0]['login']['username']
        country = data['results'][0]['location']['country']
        return username, country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()