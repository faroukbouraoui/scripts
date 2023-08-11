import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="the prompt to send to Openai api")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "****"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write a python script to {args.prompt}",
    "max_tokens": 100,
    "temperature": 0.5

}

response = requests.post(api_endpoint, headers=headers, json=request_data)

if response.status_code == 200:
    print (response.json()["choices"][0]["text"])
else:
    print(f"Request failed with status: {str(response.status_code)}")