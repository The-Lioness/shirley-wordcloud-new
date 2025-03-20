import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file (Make sure it's in the same folder)
csv_file = "shirley_memorial_responses.csv"

# Read the CSV and extract the relevant column (Adjust the column name if necessary)
df = pd.read_csv(csv_file)

# Select the column that contains words for the word cloud
words_column = "What is on word that comes to mind when you think of Shirley?"
words_list = df[words_column].dropna().tolist()  # Remove empty cells

# Convert list to a single string
words_text = " ".join(words_list)

# Define function for a royal blue color scheme
def royal_blue_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return "royalblue"  # Sets all words to royal blue

# Generate the word cloud with royal blue font
wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color="white", 
    color_func=royal_blue_color
).generate(words_text)

# Save word cloud to file
wordcloud.to_file("wordcloud.png")

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
