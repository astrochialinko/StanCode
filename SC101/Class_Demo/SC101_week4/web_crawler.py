import requests
from bs4 import BeautifulSoup


def main():
    website = 1
    sort_year = True
    star_average = True

    if website == 1:
        # old website
        url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
    elif website == 2:
        # new website
        url = 'https://www.imdb.com/chart/top/'

    source_code = requests.get(url)
    html = source_code.text
    soup = BeautifulSoup(html, features="html.parser")
    if sort_year:
        if website == 1:
            items = soup.find_all('span', {'class': 'lister-item-year text-muted unbold'})
        elif website == 2:
            items = soup.find_all('td', {'class': 'titleColumn'})

        d = {}
        for item in items:
            if website == 1:
                year = item.text
            elif website == 2:
                year = item.span.text

            if year not in d:
                d[year] = 1
            else:
                d[year] += 1

        for key, value in sorted(d.items(), key=lambda t: t[1]):
            print(key, value)

    if star_average:
        if website == 1:
            item2s = soup.find_all('div', {'class': 'inline-block ratings-imdb-rating'})
        elif website == 2:
            item2s = soup.find_all('td', {'class':'ratingColumn imdbRating'})

        sum = 0
        num = len(item2s)

        for item2 in item2s:
            star = item2.strong.text
            sum += float(star)

        print('average score: ', sum/num)



if __name__ == '__main__':
    main()