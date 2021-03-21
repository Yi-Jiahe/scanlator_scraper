from bs4 import BeautifulSoup

from Scraper import Scraper


class MerakiScans(Scraper):
    homepage = 'https://merakiscans.com/'
    all_manga_page = 'https://merakiscans.com/manga/'

    def get_manga(self):
        self.retrieve_page(self.all_manga_page, 'merakiscans_manga.html')

        soup = BeautifulSoup(self.page, 'html.parser')
        all_manga_list = soup.find(id='all').find_all(id='listitem')
        for listitem in all_manga_list:
            title = listitem.find('h1').string
            link = listitem.find('a')['href']
            self.all_manga.append((title, link))

        self.save_csv('merakiscans.csv')


class LevitanScans(Scraper):
    homepage = 'https://leviatanscans.com/'
    all_manga_page = 'https://leviatanscans.com/manga/'

    def get_manga(self):
        # TODO Navigate additional pages
        self.retrieve_page(self.all_manga_page, 'levitanscans_manga.html')

        soup = BeautifulSoup(self.page, 'html.parser')
        all_manga_list = soup.find_all(attrs={'class': ['page-item-detail', 'manga']})
        for listitem in all_manga_list:
            print(listitem)
            title = listitem.find('a')['title']
            link = listitem.find('a')['href']
            self.all_manga.append((title, link))

        self.save_csv('levitanscans.csv')

