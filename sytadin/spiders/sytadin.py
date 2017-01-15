import re
from datetime import datetime
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "sytadin"

    start_urls = ['http://www.sytadin.fr/sys/temps_de_parcours.jsp.html?type=secteur',
]
# hint pour relancer : scrapy crawl quotes -o until90.csv -s JOBDIR=crawls/quotes_new-until90Z


    # début du parse des pages
    def parse(self, response):
        data_sytadin_globale = response.css("div[id='secteur']")
        data_td_sytadin = data_sytadin_globale.css("td::text")
        #début de la loop pour sortir les td
        #création d'une var d'incrémentation
        i=0

        while i<(887/6):

            yield {
                'date_heure':str(datetime.now()),
                'axe':re.sub(r'(\s{2,}|\t|\n)','',data_td_sytadin.extract()[i]),
                'parcours':re.sub(r'(\s{2,}|\t|\n)','',data_td_sytadin.extract()[i*6+1]),
                'temps':re.sub(r'(\s{2,}|\t|\n)','',data_td_sytadin.extract()[i*6+2]),
                'temps_ref':re.sub(r'(\s{2,}|\t|\n)','',data_td_sytadin.extract()[i*6+3]),
                'dist':re.sub(r'(\s{2,}|\t|\n)','',data_td_sytadin.extract()[i*6+4]),
                'pourcent':re.sub(r'(\s{2,}|\t|\n)','',data_td_sytadin.extract()[i*6+5]),
            }
            i+=1
