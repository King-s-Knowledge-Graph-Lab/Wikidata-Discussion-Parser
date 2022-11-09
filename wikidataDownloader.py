import os
import urllib
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

    def get_links(self, data_type: str = None, filetype: str = "bz2"):
        """
        A function than finds the required links to the wikidata dump files
        :param filetype: The type of compressed file wanted (7z or bz2)
        :param data_type: A string denoting which files are of interest (e.g. "meta")
        :return: None
        """
        prefix = 'https://dumps.wikimedia.org'
        reqs = requests.get(self.dump_url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for link in soup.find_all('a'):
            if data_type is None and link.has_attr('href') and link['href'].split(".")[-1] == filetype:
                self.urls_to_download.append(prefix + link['href'])
            elif link.has_attr('href') and data_type in link['href'] and link['href'].split(".")[-1] == filetype:
                self.urls_to_download.append(prefix + link['href'])

    def download_file(self, link: str, filename: str):
        """
        A function that download a single file
        :param link: the link to the file to be downloaded
        :param filename: The filename for saving the file
        :return: none
        """
        ftype = link.split(".")[-1]
        urllib.request.urlretrieve(link, os.path.join(self.save_dir, filename + '.' + ftype))

    def download_all_files(self):
        """
        A function that downloads all the files contained in the wikidata dump specified
        :return: None
        """
        for idx, link in enumerate(self.urls_to_download):
            ftype = link.split(".")[-1]
            urllib.request.urlretrieve(link, os.path.join(self.save_dir, str(idx) + '.' + ftype))

    def reset_downloader(self):
        """
        Resets the downloader object
        :return: None
        """
        self.save_dir = ""
        self.urls_to_download.clear()
        self.dump_url = ""

    def set_save_directory(self, path: str = None):
        """
        Sets the save directory
        :param path: The directory where the dump files will be saved
        :return: None
        """
        self.save_dir = path if path is not None else os.path.join(os.getcwd(), "Dump")

    def set_dump_url(self, url: str = None):
        """
        Sets the url of the wikidata dump
        :param url: The dump url
        :return: None
        """
        if url is not None:
            self.dump_url = url
        else:
            raise ValueError('Invalid url. Please provide a valid wikidata dump url')

    @property
    def links(self):
        return self.urls_to_download

    @property
    def url(self):
        return self.dump_url

    @property
    def directory(self):
        return self.save_dir
