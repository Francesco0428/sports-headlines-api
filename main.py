import requests

@app.route("/reddit_nhl")
def get_reddit_nhl():
    url = "https://www.reddit.com/r/nhl.json"
    headers = {"User-Agent": "FrancescoScriptBot/0.1"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        posts = data["data"]["children"]

        # Sort: "Discussion" posts first, then by upvotes
        discussion_posts = []
        other_posts = []

        for post in posts:
            post_data = post["data"]
            post_info = {
                "title": post_data.get("title"),
                "link": "https://reddit.com" + post_data.get("permalink", ""),
                "flair": post_data.get("link_flair_text", "None"),
                "upvotes": post_data.get("ups", 0)
            }

            if post_data.get("link_flair_text") == "Discussion":
                discussion_posts.append(post_info)
            else:
                other_posts.append(post_info)

        # Combine: Fill up to 15 with discussion first, then other
        final_posts = discussion_posts[:15]
        if len(final_posts) < 15:
            final_posts += other_posts[:15 - len(final_posts)]

        return jsonify(final_posts)

    except Exception as e:
        return jsonify({"error": str(e)})
