import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport','cond, temp, scale, loc')


def main():
    print_the_header()
    code = input("What zipcode do you want the weather for (93065)? ")
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print('The temp in {} is {} {} and {}'.format(report.loc, report.temp, report.scale, report.cond))


def print_the_header():
    print('--------------------------')
    print('       Weather App')
    print('--------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    responce = requests.get(url)
    return responce.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()