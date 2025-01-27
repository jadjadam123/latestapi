from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_latest_token_profiles():
    url = "https://api.dexscreener.com/token-boosts/top/v1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data  # Return the raw JSON data
        else:
            return {"error": f"Failed to fetch data: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

@app.route("/latest-tokens", methods=["GET"])
def get_latest_tokens():
    data = fetch_latest_token_profiles()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
