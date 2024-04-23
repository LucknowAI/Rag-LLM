import requests


class FastAPIChatClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def chat(self, user_id, prompt):
        url = f"{self.base_url}/chat/{user_id}/{prompt}"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            user_prompt = json_data.get(user_id)
            lallan_response = json_data.get("Lallan")
            file_path = json_data.get("lol")
            return lallan_response
        else:
            return None
