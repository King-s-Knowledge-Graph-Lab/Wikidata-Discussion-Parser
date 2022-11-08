import os
import statics
import requests
from bs4 import BeautifulSoup
from typing import List


class Downloader:
    save_dir: str
    dump_url: str
    urls_to_download: List[str]

    def __init__(self, save_dir: str = None, url: str = None):
        """
        The downloader class constructor
        :param save_dir: The path to the directory where the data will be saved
        """
        self.save_dir = save_dir if save_dir is not None else os.path.join(os.getcwd(), "Dump")
        self.urls_to_download = []
        statics.check_and_make_dir(self.save_dir)
        if url is not None:
            self.dump_url = url
        else:
            raise ValueError('Invalid url. Please provide a valid wikidata dump url')

    def get_links(self, data_type: str):
        """
        A function than finds the required links to the wikidata dump files
        :param data_type: A string denoting which files are of interest (e.g. "meta")
        :return: None
        """
        reqs = requests.get(self.dump_url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for link in soup.find_all('a'):
            if link.has_attr('href') and data_type in link['href'] and link['href'].split(".")[-1] == "bz2":
                self.urls_to_download.append(link['href'])

    def download_file(self, link: str):
        """
        A function that downloads the file specified in a link
        :return:
        """
        # urllib.request.urlretrieve(link, r'dumps_xml_Nov2021/num_' + str(n) + '.bz2')
        pass

    def reset_downloader(self):
        """
        Resets the downloader object
        :return: None
        """
        self.save_dir = ""
        self.urls_to_download.clear()
        self.dump_url = ""

    @property
    def links(self):
        return self.urls_to_download
