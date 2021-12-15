def get_rising_submissions(subreddit):

    url = f"https://www.reddit.com/r/{cybersecurity}/rising.json?limit=1"
    headers = {"User-Agent": "Reddit Rising Checker v1.0"}

    with requests.get(url, headers=headers) as response:

        data = response.json()["data"]["children"]

        # Iterate over all the children.
        for item in data:

            item_data = item["data"]

            # We will collect only the fields we are interested in.
            title = item_data["title"]
            permalink = "https://reddit.com" + item_data["permalink"]
            author = item_data["author"]
            score = item_data["score"]
            image_url = item_data["url"]

            # Compose a Markdown message using string formatting.
            message = f"[{title}]({permalink})\nby **{author}**\n**{score:,}** points"

            return (message, image_url)

def post_message(message, image_url):

    payload = {
        "username": "Rising Posts",
        "embeds": [
            {
                "title": "Top Rising Post",
                "color": 102204,
                "description": message,
                "thumbnail": {"url": image_url},
                "footer": {"text": "Powered by Elf Magic™"}
            }
        ]
    }

    with requests.post(WEBHOOK_URL, json=payload) as response:
        print(response.status_code)