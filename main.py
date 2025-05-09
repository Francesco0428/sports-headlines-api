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
