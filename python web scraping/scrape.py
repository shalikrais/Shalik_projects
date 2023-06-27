import requests
from bs4 import BeautifulSoup
import pprint

def get_news(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.select('.titleline > a'), soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select_one('.score')
        if vote:
            points = int(vote.getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# Send GET requests and retrieve HTML content
links1, subtext1 = get_news('https://news.ycombinator.com/news')
links2, subtext2 = get_news('https://news.ycombinator.com/news?p=2')

# Merge the links and subtext from both pages
mega_links = links1 + links2
mega_subtext = subtext1 + subtext2

# Print the custom Hacker News list using pretty printing
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
