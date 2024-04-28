import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Process the data
has_email = df['Emails'].apply(lambda x: 'NOT_FOUND' not in str(x))
has_website = df['Website'].notna()
has_phone = df['Phone'].notna()

# Count the number of entries with and without each piece of information
email_counts = has_email.value_counts()
website_counts = has_website.value_counts()
phone_counts = has_phone.value_counts()

# Plot the data
fig, ax = plt.subplots(1, 3, figsize=(12, 4))

# Plot for emails
ax[0].pie(email_counts, labels=['With Email', 'Without Email'], autopct='%1.1f%%', startangle=90)
ax[0].set_title('Emails')

# Plot for websites
ax[1].pie(website_counts, labels=['With Website', 'Without Website'], autopct='%1.1f%%', startangle=90)
ax[1].set_title('Websites')

# Plot for phones
ax[2].pie(phone_counts, labels=['With Phone', 'Without Phone'], autopct='%1.1f%%', startangle=90)
ax[2].set_title('Phones')

plt.show()
