from days.day_049.files.helpers import *


def day_049():
    title("AUTOMATED JOB APPLICATION")

    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nLINKEDIN_SEARCH_QUERY, LINKEDIN_EMAIL and LINKEDIN_PASSWORD values."
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
        LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
        LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
        LINKEDIN_SEARCH_QUERY = os.getenv("LINKEDIN_SEARCH_QUERY")
        creds.append(LINKEDIN_EMAIL)
        creds.append(LINKEDIN_PASSWORD)
        creds.append(LINKEDIN_SEARCH_QUERY)
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
        # Setup
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        chrome_driver_path = os.path.join(BASE_DIR, "tools", "chromedriver.exe")
        print(chrome_driver_path)
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        delay = 5
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_path
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

        nls("Code altered to save, instead of apply.")
        nls("Launching...")
        nls("Press CTRL C to exit...")

        # Visit the website & Login
        driver.get(LINKEDIN_SEARCH_QUERY)
        login_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
        login_btn.click()
        time.sleep(1)
        email_input = driver.find_element(By.ID, "username")
        email_input.click()
        email_input.send_keys(LINKEDIN_EMAIL)
        password_input = driver.find_element(By.ID, "password")
        password_input.click()
        password_input.send_keys(LINKEDIN_PASSWORD)
        sign_in_btn = driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large")
        sign_in_btn.click()

        # Await page load then scroll to the bottom with job result column selected
        time.sleep(3)
        left_column = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
        left_column.click()
        html = driver.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.END)
        time.sleep(3)
        html.send_keys(Keys.HOME)

        # Find all job results on page
        all_jobs = driver.find_elements(
            By.CSS_SELECTOR, ".job-card-container--clickable"
        )
        print(len(all_jobs))

        # Click each job and wait 2 seconds for it to load, then apply/save
        for job in all_jobs:
            job.click()
            time.sleep(2)
            try:
                save_job_btn = driver.find_element(
                    By.CSS_SELECTOR, "button.jobs-save-button"
                )
                save_job_btn.click()
                time.sleep(2)
                close = driver.find_element(
                    By.CSS_SELECTOR,
                    ".artdeco-toast-item__dismiss.artdeco-button.ember-view",
                )
                close.click()
            except NoSuchElementException:
                nls("No application button, skipped.")
                continue

        # Keeps browser open after process
        while True:
            pass
