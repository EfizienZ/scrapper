import csv
import scrapes


cities = [
    '/sevilla',
    '/cadiz',
    '/cordoba',
    '/granada',
    '/huelva',
    '/jaen',
    '/malaga'
]
cities = [
    '/albacete',
    '/ciudad-real',
    '/cuenca',
    '/guadalajara',
    '/toledo'
]
cities = [
    '/caceres',
    '/badajoz'
]
for city in cities:
    print("###########" + city + "###########")
    print("########### HREFS ###########")
    hrefs = scrapes.scrape_page(city)
    print("########### WEBS ###########")
    web_pages, phones, names = scrapes.scrape_web_pages(hrefs)
    print("########### MAILS ###########")
    emails = scrapes.find_emails(web_pages)

    # Save emails to a CSV file
    combined_data = list(zip(names, emails, web_pages, phones))
    with open('results' + city + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Emails', 'Website', 'Phone'])
        writer.writerows(combined_data)
