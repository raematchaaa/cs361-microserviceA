# Pet Training Tips Microservice
# Author: Seo Young "Rae" Moon


# User Story #1: Retrieve Training Tips by Category
# User Story #2: Handle Empty Tip Category Gracefully
# User Story #3: View My Favorite Tips

import requests

local_url = "http://localhost:5000"

def get_tips_by_category(category):
    print(f"Requesting tips for '{category}' category...")
    response = requests.get(f"{local_url}/tips", params={"category": category})
    print("Status code:", response.status_code)
    try:
        data = response.json()
        tips = data.get('tips')
        if tips:
            print("Tips:\n", tips)
        else:
            print("Response:\n", data)
    except Exception:
        print("Cannot decode JSON: ", response.text)


def view_favorite_tips(username):
    print(f"Requesting {username}'s favorite training tips...")
    response = requests.get(f"{local_url}/favorites", params={"username": username})
    print("Status code:", response.status_code)
    print("Response:\n", response.json())


if __name__ == "__main__":
    # get_tips_by_category("puppy")
    # print("\n")
    # get_tips_by_category("N/A")
    # print("\n")
    # get_tips_by_category("")
    # print("\n")
    
    # view_favorite_tips("alex")
    # print("\n")
    # view_favorite_tips("henry")
    # print("\n")
    # view_favorite_tips("N/A")
    # print("\n")
    # view_favorite_tips("")
    # print("\n")