from days.day_044.files.helpers import *


def day_044():
    title("PERSONAL SITE")
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    # Locate chrome driver and use it to open index.html
    try:
        this_directory = input(
            f"Where is the Python100 Folder located?\ne.g. c:/Users/Bob/Downloads\nPress enter for default ({os.getcwd()}).\n"
        )
        if this_directory == "":
            this_directory = os.getcwd()
        print(f"Set directory location: {this_directory}")
        webbrowser.get(chrome_path).open(
            f"file://{this_directory}/tools/days/day_044/files/index.html"
        )
    except:
        # If exception, use a hardcoded path
        try:
            webbrowser.get().open(
                "file://d:/dev/Python100/tools/days/day_044/files/index.html"
            )
        except:
            nls(
                "There is likely a problem with the file locations. You need to adjust the url location for your files."
            )
