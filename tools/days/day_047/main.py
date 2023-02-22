from days.day_047.files.helpers import *


def day_047():
    title("AUTOMATED PRICE TRACKER")

    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nMY_EMAIL and MY_EMAIL_PASSWORD values."
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
        MY_EMAIL = os.getenv("MY_EMAIL")
        MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
        creds.append(MY_EMAIL)
        creds.append(MY_EMAIL_PASSWORD)
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
        # Prepared URL of desired item
        item_uri = "https://www.amazon.com.au/Nintendo-Ring-Fit-Adventure/dp/B07XW8BGFQ/ref=sr_1_1?dchild=1&keywords=ring+fit+adventure&qid=1619889211&sr=8-1"

        # Created headers for html request to not get flagged
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "X-Real-Ip": "180.150.80.162",
        }

        # Created request, encoded it and set content to text of response
        html = requests.get(item_uri, headers=headers)
        html.encoding = "utf-8"
        content = html.text

        # Soupified contents to find the price of tiem at url
        soup = BeautifulSoup(content, "html.parser")
        item = soup.find(name="span", id="productTitle").getText().strip()
        price = float(soup.find(name="span", class_="a-price-whole").getText())

        # Sought user input on what they would like to pay vs how much it currently is
        desired_price = float(
            nli(
                f'"{item}" is currently ${price}.\nHow much would you actually pay in dollars?'
            )
        )

        # If price is less or equal to desired price, send email
        if price <= desired_price:
            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
                    conn.starttls()
                    conn.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
                    conn.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs="kaishunmasaji@outlook.com",
                        msg=f"Subject: It's a reasonable price!!\n\n{item}: ${price}\n{item_uri}",
                    )
                nls("Email sent!")
            # Handler where error validating email credentials
            except Exception as e:
                nls(
                    f"{bcolors.FAIL}{e}{bcolors.ENDC}\n{bcolors.OKCYAN}Could not send email due to above error. Message would be as follows:{bcolors.ENDC}"
                )
                nls(
                    f"Subject: It's a reasonable price!!\n\n{item}: ${price}\n{item_uri}"
                )
        # If price still too high, provided feedback
        else:
            nls("Still not at a reasonable price. Check again later.")
