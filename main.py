import logging
import pandas as pd
from request_manager import Request


# Logging basic configuration
logging.basicConfig(filename='Loggings.log')


def data_cleaning(frame: pd.DataFrame) -> None:
    """ This function cleans data in your data frame """

    # Delete all none value datas
    frame.dropna(inplace=True)
    # Delete all duplicatied datas
    frame.drop_duplicates(inplace=True)



if __name__ == '__main__':
    try:

        while True:

            # Brand name of cars
            brand = input('Please enter a car brand such as toyota: ').lower()

            # Exit the program
            if brand == '':
                break

            url = f'https://www.truecar.com/shop/new/?filterType=brand&makeSlug={brand}'

            request = Request(url=url)

            titles = list()
            price = list()

            cars = request.get_all(
                html_tag='div',
                tag_id_by='class',
                tag_id='mt-5'
            )

            for car in cars:
                info = car.find('a', {'class': 'block'}).text

                index = info.find('Starting at')

                titles.append(info[:index+1])
                price.append(info[index+12:])

            cars = {
                'Name': titles,
                'Price': price,
            }

            frame = pd.DataFrame(cars)

            data_cleaning(frame=frame)

            print(frame)

            frame.to_csv(f'{brand}_cars.csv')

    except TimeoutError as error:
        print('ERROR:', error)
        logging.error(error)
    except ValueError as error:
        print('ERROR:', error)
        logging.error(error)
    except AttributeError as error:
        print('ERROR:', error)
        logging.error(error)
