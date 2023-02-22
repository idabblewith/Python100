from days.day_050.files.helpers import *
from days.day_050.files.chromewithprefs import ChromeWithPrefs


def day_050():
    title("TINDER SWIPING BOT")
    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nTINDER_EMAIL and TINDER_PASSWORD values."
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
        TINDER_EMAIL = os.getenv("TINDER_EMAIL")
        TINDER_PASSWORD = os.getenv("TINDER_PASSWORD")
        creds.append(TINDER_EMAIL)
        creds.append(TINDER_PASSWORD)
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
        prefs = {
            "profile.default_content_setting_values": {
                "notifications": 1,
                "geolocation": 1,
            },
            "profile.managed_default_content_settings": {"geolocation": 1},
        }

        # Configuration to ensure geolocation and notifications enabled
        capabilities = DesiredCapabilities().CHROME
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--start-fullscreen")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")

        chrome_options.add_experimental_option("prefs", prefs)
        capabilities.update(chrome_options.to_capabilities())
        driver = ChromeWithPrefs(options=chrome_options)

        # webdriver.Chrome(
        #     executable_path=chrome_driver_path, chrome_options=chrome_options
        # )

        nls("Code altered to save, instead of apply.")
        nls("Launching...")
        nls("Press CTRL C to exit...")

        url = "https://tinder.com/"

        # Visit the website & Login with facebook credentials
        driver.get(url)

        time.sleep(1)
        login_button = driver.find_element(By.LINK_TEXT, "Log in")
        login_button.click()
        time.sleep(0.5)
        facebook_login = driver.find_element(
            By.XPATH, '//div[text()="Login with Facebook"]'
        )
        facebook_login_btn = facebook_login.find_element(By.XPATH, "..")
        time.sleep(2)
        facebook_login_btn.click()

        facebook_signin_window = driver.window_handles[1]
        driver.switch_to.window(facebook_signin_window)
        time.sleep(3)
        email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
        email_input.send_keys(TINDER_EMAIL)
        time.sleep(0.5)
        try:
            password_input = driver.find_element(By.XPATH, '//input[@name="pass"]')
            password_input.click()
            password_input.send_keys(TINDER_PASSWORD)
            time.sleep(1)
            password_input.send_keys(Keys.ENTER)
            time.sleep(2)
            base_window = driver.window_handles[0]
            driver.switch_to.window(base_window)
        except Exception as e:
            print(e)

        # For enabling any popups regarding location
        try:
            time.sleep(3)
            allow_loc = driver.find_element(By.XPATH, '//button[@data-testid="allow"]')
            allow_loc.click()
            time.sleep(0.5)
            allow_loc = driver.find_element(By.XPATH, '//button[@data-testid="allow"]')
            allow_loc.click()
        except Exception as e:
            print(e)

        # For accepting any notifications
        try:
            spans = driver.find_elements(By.XPATH, '//span[@class="Pos(r) Z(1)"]')
            for span in spans:
                if (
                    span.text == "I accept"
                    or span.text == "I ACCEPT"
                    or span.text == "I Accept"
                ):
                    time.sleep(1)
                    btn = span.find_element(By.XPATH, "..")
                    btn.click()
                    time.sleep(3)
                    break
        except Exception as e2:
            print(e2)

        time.sleep(2)

        # Continually swipes right until a match is found
        while True:
            try:
                time.sleep(2)
                body = driver.find_element(By.CSS_SELECTOR, "body")
                body.send_keys(Keys.RIGHT)
                time.sleep(1)
                try:
                    modal = driver.find_element(
                        By.XPATH,
                        '//div[@class="Bdrs(8px) Ov(h) Ta(c) Bgc(#fff) M(10px) W(100%) Miw(300px) W(400px)--ml Mah(100%)--xs Ovy(s)--xs Ovs(touch)--xs Ovsby(n)--xs"]',
                    )
                    if modal:
                        driver.close()
                        nls(f"{bcolors.FAIL}No more likes. Quitting...{bcolors.ENDC}")
                        break
                except:
                    pass
            except:
                nls(e)
                pass
