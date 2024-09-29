import google.generativeai as genai
api_key = "AIzaSyCCiUC5VY9wGtSLyoacU844awZbQ24bmTs"

# Set your API key (replace with your actual API key)
genai.configure(api_key="AIzaSyCCiUC5VY9wGtSLyoacU844awZbQ24bmTs")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)