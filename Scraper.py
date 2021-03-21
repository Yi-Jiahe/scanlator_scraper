import os
import requests
import csv


class Scraper:
    def __init__(self):
        self.update_cache = False
        self.page = None
        self.all_manga = list()

    def retrieve_page(self, all_manga_page, filename):
        new_file = False
        try:
            with open(os.path.join('cached', filename), 'r') as f:
                if f.read() == '':
                    new_file = True
        except FileNotFoundError:
            new_file = True

        if self.update_cache or new_file:
            with open(os.path.join('cached', filename), 'w') as f:
                page = requests.get(all_manga_page)
                f.write(page.content.decode())

        with open(os.path.join('cached', filename), 'r') as f:
            self.page = f.read()

    def save_csv(self, filename):
        with open(os.path.join('data', filename), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for manga in self.all_manga:
                writer.writerow(manga)