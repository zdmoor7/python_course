import os
load_dotenv()

response = requests.get("https://api.github.com/users/torvalds")

data = response.json()
print(data["name"])
print(data["public_repos"])
print(data["followers"])

response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")

top_ids = response.json()[:3]

for id in top_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
    print(story.json()["title"])

    # Test it
client = AnthropicClient(os.getenv("ANTHROPIC_API_KEY"))
reply = client.send_message(""Here is a developer's GitHub repos: [github data]. Here are today's top Hacker News stories: [hacker news data]. Which stories would this developer find most relevant and why?"")
print(reply)