# Day 36
# Updated 2023, Jarid Prince

from days.day_036.files.helpers import *


def day_036():
    title("STOCK NOTIFIER")

    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file'\nNEWS_API, STOCK_API, TWILIO_ID, TWILIO_TOKEN, TWILIO_NUMBER & MY_PHONE_NUMBER values."
    )
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    ENV_FILE = os.path.join(BASE_DIR, ".env")
    env_error = False

    def error_env_msg(e):
        nls(
            f"It seems that you do not have an environment variable for a required file!\n{e}"
        )

    creds = []
    try:
        load_dotenv(ENV_FILE)
        TWILIO_ID = os.getenv("TWILIO_ID")
        TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
        TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
        MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
        NEWS_API = os.getenv("NEWS_API")
        STOCK_API = os.getenv("STOCK_API")
        creds.append(TWILIO_ID)
        creds.append(TWILIO_TOKEN)
        creds.append(TWILIO_NUMBER)
        creds.append(MY_PHONE_NUMBER)
        creds.append(NEWS_API)
        creds.append(STOCK_API)
    except Exception as e:
        error_env_msg(e)
        env_error = True
    else:
        for cred in creds:
            if cred == None or cred == "":
                error_env_msg(f"Error with credential: {cred}")
                env_error = True

    # RUN ONLY IF NO ERROR WITH KEYS
    if not env_error:
        # Stock, company and desired data type
        STOCK = "TSLA"
        COMPANY_NAME = "Tesla"
        FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"  # TIME_SERIES_DAILY is no longer free, so using ADJUSTED
        # Today, Yesterday and Day befores' var set with time delta.
        今日 = dt.utcnow().date()
        昨日 = 今日 - td(days=1)
        一昨日 = 今日 - td(days=2)
        # Preparing Stock API parameters for request
        stock_params = {
            "apikey": STOCK_API,
            "symbol": STOCK,
            "function": FUNCTION,
            "outputsize": "compact",
        }
        # Use parameters and send a request to API, raising error if one present
        stock_response = requests.get(
            "https://www.alphavantage.co/query", params=stock_params
        )
        stock_response.raise_for_status()
        # Format to JSON and grab Daily data
        データ = stock_response.json()
        日データ = データ["Time Series (Daily)"]
        nls("Received Stock data...")
        # Format yesterday and previous days' data in string variables
        昨日のデータ = 日データ[str(昨日)]
        一昨日のデータ = 日データ[str(一昨日)]
        # Preparing News API parameters for request
        news_params = {
            "apiKey": NEWS_API,
            "q": COMPANY_NAME,
            "pageSize": 3,
            "country": "us",
        }
        # Use parameters and send a request to API, raising error if one present
        news_response = requests.get(
            "https://newsapi.org/v2/top-headlines", params=news_params
        )
        nls(news_response.content)
        news_response.raise_for_status()
        # Grab maximum 3 articles from response
        news_data = news_response.json()["articles"]
        if len(news_data) < 3:
            endrange = len(news_data)
        else:
            endrange = 3
        # Cast ytd and previous days closes to floats
        yesterdays_close = float(昨日のデータ["4. close"])
        day_before_yd_close = float(一昨日のデータ["4. close"])
        # Calculate difference
        difference = day_before_yd_close - yesterdays_close
        percentage_change = difference / day_before_yd_close * 100
        # Append articles to dictionary in desired format
        articles = {}
        for artnum in range(0, endrange):
            articles[artnum + 1] = {
                "Headline": news_data[artnum]["title"],
                "Brief": news_data[artnum]["description"],
                "Date": news_data[artnum]["publishedAt"],
            }

        # Returns news for each article in articles dict. Articles are formatted,
        def show_news():
            news = ""
            for num in articles:
                news += f'\nHeadline: {articles[num]["Headline"]}\nBrief: {articles[num]["Brief"]}\nDate: {articles[num]["Date"][:10]}\n'
            return news

        # Preparing messages and Twilio Client for SMS. Message differs based on percentage change.
        nls("Sending Twilio SMS...")
        client = Client(TWILIO_ID, TWILIO_TOKEN)

        # Up or down message if percentage change is 5%, otherwise stable message
        if yesterdays_close > (day_before_yd_close * 1.05):
            message = client.messages.create(
                body=f"🔺 {STOCK} is UP by {round(percentage_change, 2)}%:\n {show_news()}",
                from_=TWILIO_NUMBER,
                to=MY_PHONE_NUMBER,
            )
        elif yesterdays_close < (day_before_yd_close * 0.95):
            message = client.messages.create(
                body=f"🔻 {STOCK} is DOWN by {round(percentage_change, 2)}%:\n {show_news()}",
                from_=TWILIO_NUMBER,
                to=MY_PHONE_NUMBER,
            )
        else:
            message = client.messages.create(
                body=f"{STOCK} is fairly stable @ {round(percentage_change, 2)}% change:\n {show_news()}",
                from_=TWILIO_NUMBER,
                to=MY_PHONE_NUMBER,
            )
