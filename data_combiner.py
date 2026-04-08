import requests
import os
from dotenv import load_dotenv
from api_wrapper import AnthropicClient

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")


# Fetch GitHub data
github_response = requests.get("https://api.github.com/users/torvalds")
github_data = github_response.json()
github_summary = f"Name: {github_data['name']}, Public Repos: {github_data['public_repos']}, Followers: {github_data['followers']}"
#This section of code is used to fetch data from the GitHub API
# Fetch Hacker News data
hn_response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
top_ids = hn_response.json()[:5]
#This section of code is used to fetch data from the hacker news API
hn_titles = []
for id in top_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
    hn_titles.append(story.json()["title"])

hn_summary = "\n".join(hn_titles)#titles are joined here to create a single string.
#This section, starting with hn_titles and finishing with hn_summary, i used to join the titles of the top 5 hacker news stories int a single string.
# Combine and send to Claude
client = AnthropicClient(api_key)
reply = client.send_message(f"""
Here is a developer's GitHub profile: {github_summary}

Here are today's top Hacker News stories:
{hn_summary}

Which of these stories would this developer find most relevant and why?
""")
# the above is context forth eaI to use in generating a response
print(reply)