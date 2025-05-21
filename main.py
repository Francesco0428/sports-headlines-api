from flask import Flask, jsonify, send_from_directory
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
@app.route("/nhl_headlines")
def get_nhl_headlines():
    feed_urls = [
        "https://www.nhl.com/rss/news",  # NHL.com
        "https://www.sbnation.com/rss/hockey",  # SB Nation Hockey
        "https://thehockeynews.com/.rss/full/"  # The Hockey News
    ]
    
    all_headlines = []
    
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # Pull top 5 from each
            all_headlines.append({
                "title": entry.title,
                "summary": entry.get("summary", "null"),
                "link": entry.link
            })

    return jsonify(all_headlines)
