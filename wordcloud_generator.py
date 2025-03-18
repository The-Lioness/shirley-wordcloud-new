import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load words and generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate("Your words here")

# Save the generated word cloud as an image
wordcloud.to_file("wordcloud.png")
plt.savefig("wordcloud.png")  # Ensures it's written as an image

# If running locally (not in GitHub Actions), show in Streamlit
if "--save-only" not in sys.argv:
    import streamlit as st
    st.title("Grandma Shirley Tribute Word Cloud")
    st.image("wordcloud.png")


# Set up Google Sheets API authentication
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"  # Ensure this matches your file

# Authenticate and connect to Google Sheets
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(creds)

# Open the spreadsheet and select the correct sheet
SPREADSHEET_ID = "1khXdc__ebQmO6aRoVhp_cGQgHf_55DwW8KYOwbIu8gQ"  # Replace with your actual Google Sheet ID
SHEET_NAME = "Shirley Memorial Responses"  # Change if your sheet has a different name
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Read column E (Words to describe Shirley)
words_list = sheet.col_values(5)[1:]  # Skip header

# Convert list to a single string
words_text = " ".join(words_list)

# Define a custom color function for the word cloud
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ["#4169E1", "#1E90FF", "#4682B4", "#5F9EA0", "#87CEFA"]  # Royal Blue + Complimentary Blues
    return random.choice(colors)

# Generate Word Cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    color_func=blue_color_func
).generate(words_text)

# Streamlit UI
st.title("Grandma Shirley Tribute Word Cloud")

# Display the word cloud
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Refresh Button (Optional)
if st.button("Refresh Word Cloud"):
    st.rerun()
plt.show()  # Save and display word cloud

