import os
import pandas as pd
import matplotlib.pyplot as plt


def create_analysis():
    comunidades = os.listdir('results/')
    for comunidad in comunidades:
        analyse(comunidad)


def analyse(comunidad):
    # List all files (provincias) in the comunidad directory
    provincias = os.listdir('results/' + comunidad)

    # Initialize global counts for comunidad
    global_email_counts = pd.Series(dtype=int)
    global_website_counts = pd.Series(dtype=int)

    # Initialize lists to store pie plot data for all provincias
    email_plots = []
    website_plots = []

    # Iterate over each provincia
    for provincia in provincias:
        df = pd.read_csv('results/' + comunidad + '/' + provincia)

        # Process the data
        has_email = df['Emails'].apply(lambda x:
                                        'NOT_FOUND' not in str(x) and
                                        'NO_MAIL' not in str(x) and
                                        'SSL ERROR' not in str(x) and
                                        'CONN ERROR' not in str(x) and
                                        'Invalid URL' not in str(x) and
                                        'Content decoding error' not in str(x))
        has_website = df['Website'].apply(lambda x: 'NO_WEB' not in str(x))

        # Count the number of entries with and without each piece of information
        email_counts = has_email.value_counts().sort_index()
        website_counts = has_website.value_counts().sort_index()

        # Add provincia counts to global counts
        global_email_counts = global_email_counts.add(email_counts, fill_value=0)
        global_website_counts = global_website_counts.add(website_counts, fill_value=0)

        # Store pie plot data for the current provincia
        email_plots.append((provincia, email_counts))
        website_plots.append((provincia, website_counts))

    # Plot the data for all provincias
    try:
        fig, axs = plt.subplots(len(provincias), 2, figsize=(12, len(provincias) * 4))

        for i, (provincia, email_counts) in enumerate(email_plots):
            # Plot for emails
            email_labels = [f'Without Email ({email_counts[False]})', f'With Email ({email_counts[True]})']
            try:
                axs[i, 0].pie(email_counts, labels=email_labels, autopct='%1.1f%%', startangle=90)
                axs[i, 0].set_title(f'{provincia} - Emails')
            except IndexError:
                axs[0].pie(email_counts, labels=email_labels, autopct='%1.1f%%', startangle=90)
                axs[0].set_title(f'{provincia} - Emails')

        for i, (provincia, website_counts) in enumerate(website_plots):
            # Plot for websites
            website_labels = [f'Without Website ({website_counts[False]})', f'With Website ({website_counts[True]})']
            try:
                axs[i, 1].pie(website_counts, labels=website_labels, autopct='%1.1f%%', startangle=90)
                axs[i, 1].set_title(f'{provincia} - Websites')
            except IndexError:
                axs[1].pie(website_counts, labels=website_labels, autopct='%1.1f%%', startangle=90)
                axs[1].set_title(f'{provincia} - Websites')

        # Plot the global stats for comunidad
        global_fig, global_axs = plt.subplots(1, 2, figsize=(12, 4))

        # Plot for emails
        global_email_labels = [f'Without Email ({global_email_counts[False]})', f'With Email ({global_email_counts[True]})']
        global_axs[0].pie(global_email_counts, labels=global_email_labels, autopct='%1.1f%%', startangle=90)
        global_axs[0].set_title(f'{comunidad} - Emails (Total)')

        # Plot for websites
        global_website_labels = [f'Without Website ({global_website_counts[False]})', f'With Website ({global_website_counts[True]})']
        global_axs[1].pie(global_website_counts, labels=global_website_labels, autopct='%1.1f%%', startangle=90)
        global_axs[1].set_title(f'{comunidad} - Websites (Total)')

        plt.tight_layout()
        fig.savefig('analysis/' + comunidad)
        global_fig.savefig('analysis/' + comunidad + '_global')
        plt.close()
    except ValueError:
        pass
