from flask import Flask, request, jsonify
import feedparser
app = Flask(__name__)

@app.route('/headlines', methods=['GET'])
def get_headlines():
    feed_url = 'https://www.espn.com/espn/rss/news'
    feed = feedparser.parse(feed_url)
    headlines = []
    for entry in feed.entries[:5]:
        headlines.append({
            'title': entry.title,
            'summary': entry.summary,
            'link': entry.link
        })
    return jsonify(headlines)

@app.route('/openapi.yaml')
def openapi_spec():
    return send_from_directory('.', 'openapi.yaml')

@app.route('/action.yaml')
def action_spec():
    return send_from_directory('.', 'action.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
@app.post("/story_context")
def story_context():
    """
    Return a summary + notable stats for one sports headline.
    Accepts JSON: {"headline": "<headline text>"}   # use the text for now
    """
    data = request.get_json(force=True, silent=True) or {}
    headline_text = data.get("headline", "No headline provided")

    # --- TEMPORARY STUB – replace with real summary logic later ---
    response = {
        "headline": headline_text,
        "summary": [
            "Placeholder summary bullet 1.",
            "Placeholder summary bullet 2.",
            "Placeholder summary bullet 3."
        ],
        "notable_stats": [
            {"label": "Example stat", "value": "123"},
            {"label": "Another stat", "value": "ABC"}
        ],
        "source_url": "https://example.com"
    }
    return jsonify(response)
