from days.day_046.files.helpers import *


def day_046():
    title("SPOTIFY TIME MACHINE")
    # VALIDATE DOT ENV & API KEYS
    nls(
        "NOTE: This file requires that you fill in the .env file's\nSPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET values."
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
        SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
        SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
        creds.append(SPOTIFY_CLIENT_ID)
        creds.append(SPOTIFY_CLIENT_SECRET)
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
        # A redirect url that contains secret - user will copy and paste into console
        RDURI = "http://example.com"

        # Establish Spotify API client with user's credentials. This will create a token.txt file
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_CLIENT_ID,
                client_secret=SPOTIFY_CLIENT_SECRET,
                redirect_uri=RDURI,
                scope="playlist-modify-private",
                show_dialog=True,
                cache_path="./tools/days/day_046/files/token.txt",
            )
        )
        user_id = sp.current_user()["id"]

        # Ask user for time period and use it in request
        time_period = nli("What time would you like to travel to?\nFormat: YYYY-MM-DD")
        URL = f"https://www.billboard.com/charts/hot-100/{time_period}"
        response = requests.get(URL)
        # Ensure encoded correctly to avoid errors. Then use response contents to create text
        response.encoding = "utf-8"
        contents = response.text
        # Scrape the text contents
        soup = BeautifulSoup(contents, "html.parser")
        songs_raw = soup.select("h3.c-title.a-font-primary-bold-s")
        song_titles = [song.getText() for song in songs_raw]
        song_titles = [str(song).strip() for song in song_titles]
        print(f"SONGS TITLES: {song_titles}")
        # Create a list for song urls and separate years to create a search for each song on the
        # Billboard list. If a song is found, append it to the list, otherwise skip.
        song_uris = []
        year = time_period.split("-")[0]
        for song in song_titles:
            result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except (IndexError):
                print(f'"{song}" doesn\'t exist in Spotify. Skipped.')
        pprint(song_uris)

        # Create a Spotify playlist based on the time period
        playlist = sp.user_playlist_create(
            user=user_id, name=f"{time_period} - Billboard 100", public=False
        )
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

        nls("Playlist successfully created! Check your spotify!")
