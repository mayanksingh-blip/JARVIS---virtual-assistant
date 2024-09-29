# This is to test the working of google genai
import google.generativeai as genai
api_key = "your_api_key"

# Set your API key (replace with your actual API key)
genai.configure(api_key="your_api_key")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
