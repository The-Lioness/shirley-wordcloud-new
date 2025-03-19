import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Google Sheets API authentication
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"  # Ensure this file matches your repo secrets

SPREADSHEET_ID = "1hkXdc_ebQm06aR0vHp_cGQHgF_55DwW8KYOxbIuBgQ"
SHEET_NAME = "Shirley McDonald Ross Memorial Responses"

# Authenticate and open Google Sheet
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(credentials)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Read words (Column E contains words describing Shirley)
words_list = sheet.col_values(5)[1:]  # Skip header row

# Convert list to a single string
words_text = " ".join(words_list)

# Define a custom color function for the word cloud (Royal Blue Theme)
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ["#4169E1", "#1E90FF", "#4682B4", "#5F9EA0", "#87CEFA"]  # Shades of Royal Blue
    return random.choice(colors)

# Generate the Word Cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    color_func=blue_color_func
).generate(words_text)

# Save the generated word cloud as an image
wordcloud.to_file("wordcloud.png")  # Ensures it's written as an image

# Streamlit UI - Display only if running locally (not in GitHub Actions)
import sys
if "--save-only" not in sys.argv:
    st.title("Grandma Shirley Tribute Word Cloud")
    st.image("wordcloud.png")
