import requests

response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")

top_ids = response.json()[:3]

for id in top_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
    print(story.json()["title"])