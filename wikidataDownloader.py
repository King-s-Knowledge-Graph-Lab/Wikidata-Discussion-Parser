import os

import statics
import urllib


class Downloader:
    save_dir: str

    def __init__(self, save_dir: str = None, ):
        """
        The downloader class constructor
        :param save_dir: The path to the directory where the data will be saved
        """
        self.save_dir = save_dir if save_dir is not None else os.path.join(os.getcwd(), "Dump")
        statics.check_and_make_dir(self.save_dir)

    def get_links(self):
        """
        A function that gets the links for the files of the desired wikidata dump
        :return:
        """
        pass

    def download_file(self, link: str):
        """
        A function that downloads the file specified in a link
        :return:
        """
        # urllib.request.urlretrieve(link, r'dumps_xml_Nov2021/num_' + str(n) + '.bz2')
        pass
