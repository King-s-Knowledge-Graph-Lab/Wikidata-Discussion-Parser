from wikidataDownloader import Downloader

def main():
    url = "https://dumps.wikimedia.org/wikidatawiki/20220801/"
    wiki_downloader = Downloader(url=url)
    wiki_downloader.get_links("meta")
    print(wiki_downloader.links)
    wiki_downloader.download_file(link=wiki_downloader.links[0],filename="test")
    print(wiki_downloader.links)



if __name__ == '__main__':
    main()

