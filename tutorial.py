from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# TikTok Shop OAuth credentials
CLIENT_KEY = os.getenv('TIKTOK_CLIENT_KEY')
CLIENT_SECRET = os.getenv('TIKTOK_CLIENT_SECRET')

# TikTok OAuth endpoints
AUTHORIZATION_URL = 'https://auth.tiktok-shops.com/oauth/authorize/'
TOKEN_URL = 'https://auth.tiktok-shops.com/api/v2/token/get'

REDIRECT_URI = os.getenv('TIKTOK_REDIRECT_URI')

@app.route('/tiktok/oauth', methods=['GET'])
def oauth_callback():
    code = request.args.get('code')
    
    try:
        headers = {
            'Content-Type': 'application/json',
            'x-tts-access-token': ''
        }
        
        data = {
            'app_key': CLIENT_KEY,
            'app_secret': CLIENT_SECRET,
            'auth_code': code,
            'grant_type': 'authorized_code'
        }
        
        response = requests.get(TOKEN_URL, params=data, headers=headers)
        response.raise_for_status()
        
        token_data = response.json()
        print(token_data)

        return jsonify(token_data)
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to get access token: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)