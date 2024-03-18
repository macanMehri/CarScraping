
# Car Scraper

A program to scrape car informations for a specific brand like toyota. Any scraped data will save in a csv file in the program folder with car brands name.


## Acknowledgements

 - [PyPi BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
 - [PyPi Requests](https://pypi.org/project/requests/)
 - [Python Pandas](https://www.w3schools.com/python/pandas/default.asp)


## Deployment

To deploy this project run

```bash
   pip install -r requirements.txt
```

Change sample_headers.py file name to local_headers.py and compelet info like this

```bash
   HEADERS = {
    'USER_AGENT': ' your user agent'
}
```

You can find your user agent by searching it in a browser like chrome


## Run Locally

Clone the project

```bash
  git clone https://github.com/macanMehri/CarScraping.git
```

Go to the project directory

```bash
  cd CarScraping
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```


## Features

- Scrape very fast and high quality
- Ease of use
- User friendly


## FAQ

#### Why should I use this program

Get the latest information about cars of different brands

#### What is the difference between this program and other programs?

Store the information of each brand independently


## Tech Stack

**Server:** Python

