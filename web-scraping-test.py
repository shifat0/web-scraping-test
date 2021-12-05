import csv
from requests_html import HTML, HTMLSession

# Creating a csv file (excel)
csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

# Starting Session
session = HTMLSession()
res = session.get('https://coreyms.com/')

# Getting response from the site
articles = res.html.find('article')

for article in articles:
    headline = article.find(".entry-title-link", first=True).text
    print(headline)

    summary = article.find(".entry-content p", first=True).text
    print(summary)

    try:
        vid_src = article.find("iframe", first=True).attrs['src']
        vid_id = vid_src.split('?')[0]
        vid_id = vid_id.split('/')[4]
    except Exception as err:
        yt_link = None

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
