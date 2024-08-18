from playwright.sync_api import sync_playwright
from selectolax.lexbor import LexborHTMLParser
import json, time


def get_page(playwright, from_place, to_place, departure_date, return_date):
    page = playwright.chromium.launch(headless=False).new_page()
    page.goto('https://www.google.com/travel/flights?gl=IN&hl=en')

    # type "From"
    from_place_field = page.query_selector_all('.e5F5td')[0]
    from_place_field.click()
    time.sleep(1)
    from_place_field.type(from_place)
    time.sleep(1)
    page.keyboard.press('Enter')

    # type "To"
    to_place_field = page.query_selector_all('.e5F5td')[1]
    to_place_field.click()
    time.sleep(1)
    to_place_field.type(to_place)
    time.sleep(1)
    page.keyboard.press('Enter')

    # type "Departure date"
    departure_date_field = page.query_selector_all('[aria-label="Departure"]')[0]
    departure_date_field.click()
    time.sleep(1)
    departure_date_field.type(departure_date)
    time.sleep(1)
    page.query_selector('.WXaAwc .VfPpkd-LgbsSe').click()
    time.sleep(1)

    # type "Return date"
    return_date_field = page.query_selector_all('[aria-label="Return"]')[0]
    return_date_field.click()
    time.sleep(1)
    return_date_field.type(return_date)
    time.sleep(1)
    page.query_selector('.WXaAwc .VfPpkd-LgbsSe').click()
    time.sleep(1)

    # press "Explore"
    page.query_selector('.MXvFbd .VfPpkd-LgbsSe').click()
    time.sleep(2)

    # press "More flights"
    page.query_selector('.zISZ5c button').click()
    time.sleep(2)

    parser = LexborHTMLParser(page.content())
    page.close()

    return parser


def scrape_google_flights(parser):
    data = {}

    categories = parser.root.css('.zBTtmb')
    category_results = parser.root.css('.Rk10dc')

    for category, category_result in zip(categories, category_results):
        category_data = []

        for result in category_result.css('.yR1fYc'):
            date = result.css('[jscontroller="cNtv4b"] span')
            departure_date = date[0].text()
            arrival_date = date[1].text()
            company = result.css_first('.Ir0Voe .sSHqwe').text()
            duration = result.css_first('.AdWm1c.gvkrdb').text()
            stops = result.css_first('.EfT7Ae .ogfYpf').text()
            price = result.css_first('.U3gSDe .FpEdX span').text()
            price_type = result.css_first('.U3gSDe .N872Rd').text() if result.css_first('.U3gSDe .N872Rd') else None

            flight_data = {
                'departure_date': departure_date,
                'arrival_date': arrival_date,
                'company': company,
                'duration': duration,
                'stops': stops,
                'price': price,
                'price_type': price_type
            }

            airports = result.css_first('.Ak5kof .sSHqwe')
            airport_containers = airports.css('.QylvBf')
            
            if len(airport_containers) == 2:
                departure_airport = airport_containers[0].css_first('.eoY5cb').text()
                arrival_airport = airport_containers[1].css_first('.eoY5cb').text()
                flight_data['departure_airport'] = departure_airport
                flight_data['arrival_airport'] = arrival_airport
            else:
                # Handle cases where there are not exactly two airport containers
                print("Unexpected number of airport containers:", len(airport_containers))

            category_data.append(flight_data)

            if(len(category_data)==10):
              break

        data[category.text().lower().replace(' ', '_')] = category_data

    return data


def run(playwright):
    from_place = 'Delhi'
    to_place = 'Mumbai'
    departure_date = '14-10-2024'
    return_date = '18-10-2024'

    parser = get_page(playwright, from_place, to_place, departure_date, return_date)
    google_flights_results = scrape_google_flights(parser)

    print(json.dumps(google_flights_results, indent=2, ensure_ascii=False))


with sync_playwright() as playwright:
    run(playwright)