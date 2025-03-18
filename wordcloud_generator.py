import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Set up Google Sheets API authentication
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(creds)

# Replace with your Google Sheet ID and Sheet Name
SPREADSHEET_ID = "your_google_sheet_id_here"
SHEET_NAME = "Shirley Memorial Responses"

# Load words from Google Sheet
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
words_list = sheet.col_values(5)[1:]  # Assuming column 5 has the words

# Convert list to a string
words_text = " ".join(words_list)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(words_text)

# Save the image
wordcloud.to_file("wordcloud.png")  # Ensures the image is properly saved

# Display in Streamlit
st.title("Grandma Shirley Tribute Word Cloud")
st.image("wordcloud.png")  # Ensures Streamlit loads the correct updated image
