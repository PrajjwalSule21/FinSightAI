import requests
import os
from dotenv import load_dotenv

load_dotenv()



def chat_with_agent(message, user_api_key):
    url = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": user_api_key
    }

    data = {
        "user_id": os.getenv("USER_ID"),
        "agent_id": os.getenv("AGENT_ID"),
        "session_id": os.getenv("SESSION_ID"),
        "message": message
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        try:
            response_json = response.json()
        except ValueError:
            raise Exception("Empty or malformed JSON response from the agent API.")
        
        if 'response' not in response_json:
            raise Exception("Valid API Key, but no 'response' field in the JSON response.")
        
        return response_json['response']
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error communicating with the agent API: {str(e)}")
    except Exception as e:
        raise Exception(f"An error occurred while processing the response: {str(e)}")

