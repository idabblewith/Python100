def prac():
    response = requests.get("https://news.ycombinator.com/")
    contents = response.text
    # print(contents)
    soup = BeautifulSoup(contents, "html.parser")

    articles = soup.find_all(name="a", class_="storylink")

    art_texts = []
    art_links = []
    for article_tag in articles:

        text = article_tag.getText()
        art_texts.append(text)

        link = article_tag.get("href")
        art_links.append(link)

    article_votes = [
        int(upvotes.getText().split()[0])
        for upvotes in soup.find_all(name="span", class_="score")
    ]

    # print(votes)
    highest_vote = max(article_votes)
    hv_index = article_votes.index(highest_vote)

    print(
        f"\nARTICLE: {art_texts[hv_index]},\nLINK: {art_links[hv_index]},\nVOTES: {article_votes[hv_index]}\n"
    )

    # print(art_texts)
    # print(art_links)
    # print(article_votes)
