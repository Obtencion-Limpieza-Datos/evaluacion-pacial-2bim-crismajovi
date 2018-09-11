import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "mundial"

    def start_requests(self):
        """
        urls = [
            'https://es.fifa.com/worldcup/teams/',
        ]
        """
        archivo = open("data/url.csv", "r")
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
            @reroes
        """
        filename = "data/alcaldes.csv"
        with codecs.open(filename, 'a', encoding='utf-8') as f:
            f.write('%s|%s|%s\n'%('Canton','Nombre','Partido'))
            tablas = response.xpath('//table[@class="wikitable"]') 
            tr = tablas.xpath('tbody/tr') 
            for x in tr:
                lista = x.xpath('td')
                if len(lista) > 0:
                    canton = lista[0].xpath('text()')
                    nombre = lista[1].xpath('text()')
                    partido = lista[2].xpath('a/text()')
                    if len(canton) > 0:
                        canton = lista[0].xpath('text()').extract()[0].strip()
                    else:
                        canton = lista[0].xpath('a/text()').extract()[0].strip()
                    if len(nombre) > 0:
                        nombre = lista[1].xpath('text()').extract()[0].strip()
                    else:
                        nombre = lista[1].xpath('a/text()').extract()[0].strip()
                    if len(partido) > 0:
                        partido = lista[2].xpath('a/text()').extract()[0].strip()
                    else:
                        partido = lista[2].xpath('text()').extract()[0].strip()
                    f.write(u"%s|%s|%s\n" % (canton,nombre,partido))
            #filename.close()
            
        self.log('Saved file %s' % filename)
