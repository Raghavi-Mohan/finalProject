import requests


def main():
    print("Hello World!")

    url = "https://api.spoonacular.com/food/videos/search?query=soup&excludeIngredients=eggs&includeIngredients=tomato&apiKey=4d770897d0164dd58b78d208d42c4c3a"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)


if __name__ == "__main__":
    main()
