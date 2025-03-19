import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Google Sheets API Authentication
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(creds)

# Google Sheet Information (Replace with Correct ID & Sheet Name)
SPREADSHEET_ID = "1khXdc__ebQmO6aRoVhp_cGQgHf_55DwW8KYOwbIu8gQ"  # Replace with your actual Sheet ID
SHEET_NAME = "Shirley Memorial Responses"

# Read column E (Words describing Shirley)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
words_list = sheet.col_values(5)[1:]  # Skip header

# Convert list to a single string
words_text = " ".join(words_list)

# Define word cloud color function
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ["#4169E1", "#1E90FF", "#4682B4", "#5F9EA0", "#87CEFA"]  # Royal Blue + Complementary Blues
    return random.choice(colors)

# Generate Word Cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    color_func=blue_color_func
).generate(words_text)

# Save word cloud to file
wordcloud.to_file("wordcloud.png")

# Streamlit UI (if not running in GitHub Actions)
import sys
if "--save-only" not in sys.argv:
    st.title("Grandma Shirley Tribute Word Cloud")
    st.image("wordcloud.png")
