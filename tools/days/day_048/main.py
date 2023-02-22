from days.day_048.files.helpers import *


def day_048():
    title("SELENIUM GAME BOT")
    nls(
        "This program requires that the chromedriver you have matches the version of chrome you have.\nTo check your version, click the vertical dots on the top right of your chrome browser > Help > About Google Chrome.\nOnce you know, visit https://chromedriver.chromium.org/downloads and download the appropriate driver, replacing the current one at the root."
    )
    try:
        INTERVAL = (
            int(nli("How often do you want to save (default is 10)? Type in minutes"))
            * 60
        )
    except:
        INTERVAL = 10 * 60
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    chrome_driver_path = os.path.join(BASE_DIR, "tools", "chromedriver.exe")
    print(chrome_driver_path)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    delay = 5
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    cookie = "https://orteil.dashnet.org/cookieclicker/"
    firstsave = "Mi4wMzF8fDE2MTk5MzQwOTIzNzI7MTYxOTkzNDA5MjM3MjsxNjE5OTU5MTc3ODU1O1JvYm90IE11ZmZpbjtpaGFueXwxMTExMTEwMTEwMDEwMDEwMDEwMTB8MjU4MTkzMTc2OS44Njk5OTE7MzkxNzM2ODM3NjAuODE1OTI2OzI5NTA4OzExOzg5NzMwMTEyNS42MTAzMzg2OzQ1OzA7MDswOzA7MDswOzA7MDswOzExOzA7MDswOzA7MDswOzswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7NTA7MDswOzA7MDsxNjE5OTQzMTgxNzIxOzA7MDs7NDE7MDswOzQ3MTE3MTkuNDYxNjI1ODA2O3wxMDAsMTAwLDMxMDgxODEwNTUsMCwsMCwxMDA7MTAwLDEwMCw3OTg0ODI5ODgsMCwsMCwxMDA7NzAsNzAsMzgzMzU1MTUxLDAsLDAsNzA7NTAsNTAsNzgyMjQyOTM3LDAsLDAsNTA7NTAsNTAsMjMyNDk4MjA5OSwwLCwwLDUwOzQwLDQwLDc3OTQyODI4NzAsMCwsMCw0MDsyMSwyMSwxMTc0MTUwNzc3MSwwLCwwLDIxOzExLDExLDkyNzg4MjczNzIsMCwsMCwxMTsyLDIsMTUxMDkxNzM1OCwwLCwwLDI7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7fDExMTExMTExMTExMTAwMTExMTExMTExMTExMTExMTExMTExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMDExMTExMTExMTExMTExMTAxMDEwMDAxMTExMTAxMTAwMDAwMDAwMTEwMDAwMTAxMDExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDAwMTExMTAwMDAwMDAwMTExMDAwMDAwMDAwMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMXwxMTExMTEwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAxMTEwMTExMTAwMTExMTEwMTEwMTEwMTAwMDAwMDAwMDAwMDAwMTEwMDExMDExMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDEwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfHw%3D%21END%21"
    with open("./tools/days/day_048/files/saves.txt") as newsave:
        save = newsave.read()
    nls("Launching...")
    # Visit the website
    driver.get(cookie)
    # Sleep to await language prompt
    time.sleep(delay)
    # Select language and sleep again until cookie appears
    lang = driver.find_element("id", "langSelect-EN")
    lang.click()
    time.sleep(delay)
    bigone = driver.find_element("id", "bigCookie")

    # Set a start time and an interval of 10 minutes (for saving and upgrading)
    start_time = time.time()
    every_ten = time.time() + INTERVAL

    # Click the cookie to ensure no issues
    bigone.click()

    # For Saving
    options = driver.find_element("id", "prefsButton")
    options.click()
    importsave = driver.find_element(By.LINK_TEXT, "Import save")
    importsave.click()
    textarea = driver.find_element("id", "textareaPrompt")
    textarea.click()
    textarea.send_keys(save)
    loadbtn = driver.find_element("id", "promptOption0")
    loadbtn.click()
    saveg = driver.find_element(By.LINK_TEXT, "Save")
    exs = driver.find_element(By.LINK_TEXT, "Export save")

    def savegame():
        try:
            saveg.click()
            exs.click()
            savedata = driver.find_element("id", "textareaPrompt")
            savefile = savedata.text
            with open("./tools/days/day_048/files/saves.txt", "w") as savetxt:
                savetxt.write(savefile)
            finish = driver.find_element(By.LINK_TEXT, "All done!")
            finish.click()
            nls("Game saved.")
        except:
            pass

    go = True

    # Attempts to find any upgrades and clicks them
    unlocked_store_items = driver.find_elements(
        By.CSS_SELECTOR, "div[class='product unlocked enabled']"
    )
    upgrades = driver.find_elements(
        By.CSS_SELECTOR, "div[class='crate upgrade enabled']"
    )
    upgradesinv = upgrades[::-1]
    unlocked_store_itemsinv = unlocked_store_items[::-1]
    try:
        for item in unlocked_store_itemsinv:
            item.click()
    except:
        pass

    try:
        for upg in upgradesinv:
            upg.click()
    except:
        pass

    # Game Loop - continually runs until program shut down
    while go == True:
        try:
            golden = driver.find_element(By.CLASS_NAME, "shimmer")
            golden.click()
        except:
            pass

        try:
            bigone.click()
        except:
            golden.click()

        #  Save and upgrade every ten minutes or time selected by user
        if time.time() > every_ten:
            saveg = driver.find_element(By.LINK_TEXT, "Save")
            exs = driver.find_element(By.LINK_TEXT, "Export save")

            savegame()
            unlocked_store_items = driver.find_elements(
                By.CSS_SELECTOR, "div[class='product unlocked enabled']"
            )
            upgrades = driver.find_elements(
                By.CSS_SELECTOR, "div[class='crate upgrade enabled']"
            )
            upgradesinv = upgrades[::-1]
            unlocked_store_itemsinv = unlocked_store_items[::-1]
            try:
                for upg in upgradesinv:
                    upg.click()
            except:
                pass
            try:
                for item in unlocked_store_itemsinv:
                    item.click()
            except:
                pass

            runtime = time.time()
            print(datetime.now().time())
            print(f"running for {((runtime-start_time)/60)/60} hours.")
            # Reset interval to account for time passed
            every_ten = time.time() + INTERVAL
