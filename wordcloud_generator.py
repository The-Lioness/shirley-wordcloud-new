import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys

# Set up Google Sheets API authentication
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"  # Ensure this matches your file

# Replace with the correct spreadsheet details
SPREADSHEET_ID = "1khXdc__ebQm06aR0vHp_GQqHgf_55DWw8KYObuIu8gQ"
SHEET_NAME = "Shirley Memorial Responses"

# Authenticate and open the sheet
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(credentials)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Read column E (Words to describe Shirley)
words_list = sheet.col_values(5)[1:]  # Skip header

# Convert list to a single string
words_text = " ".join(words_list)

# Define a custom color function for the word cloud (Royal Blue & Complementary Blues)
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ["#4169E1", "#1E90FF", "#4682B4", "#5F9EA0", "#87CEFA"]
    return random.choice(colors)

# Generate Word Cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    color_func=blue_color_func
).generate(words_text)

# Save the word cloud image
wordcloud.to_file("wordcloud.png")  # Ensures it's written as an image

# If running locally (not in GitHub Actions), show in Streamlit
if "--save-only" not in sys.argv:
    st.title("Grandma Shirley Tribute Word Cloud")
    st.image("wordcloud.png")
