import pandas as pd
import json

# Read the contents of the text file
with open('data/Amazon_sagemaker_Faq.txt', 'r') as file:
    data = file.read()

# Parse the JSON data
parsed_data = json.loads(data)

# Convert the parsed data into a pandas DataFrame
df = pd.DataFrame(parsed_data)

# Optionally, clean up the DataFrame
# Rename columns for better readability
df = df.rename(columns={'question': 'Question', 'answer': 'Answer', 'found_duplicate': 'Found Duplicate'})

# Optionally, reorder the columns
df = df[['Question', 'Answer', 'Found Duplicate']]

# Display the DataFrame
print(len(df['Answer']))
