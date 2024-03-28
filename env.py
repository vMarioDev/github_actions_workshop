import os

# Get a specific environemnt variable
api_key = os.environ.get("API_KEY")

# Print the value or handle if it's not set
if api_key:
  print(f"API Key: {api_key}")
else:
  print("API Key not set")