import scrapy

from ..items import MovieItem

class MojoSpider(scrapy.Spider):

    name = "mojo"

    start_urls = [
    "https://www.boxofficemojo.com/year/2002/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2001/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2002/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2003/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2004/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2005/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2006/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2007/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2008/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2009/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2010/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2011/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2012/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2013/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2014/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2015/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2016/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2017/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2018/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2019/?grossesOption=totalGrosses",
      # "https://www.boxofficemojo.com/year/2020/?grossesOption=totalGrosses"
    ]

    def parse(self, response):
        year = response.request.url.replace('https://www.boxofficemojo.com/year/','').split('/?')[0]
        table_rows = response.xpath('//*[@id="table"]//div//table/tr')
        for row in table_rows[1:]:
        #for each row in the table, uses xpath selectors
            link = row.xpath('./td[2]/a/@href')
            # print(row.xpath('./td[3]/text()'))
            url = response.urljoin(link[0].extract())
            try:
              item = MovieItem()
              item['title'] = row.xpath('./td[2]/a/text()').extract()[0]
              item['gross'] = row.xpath('./td[6]/text()').extract()[0]
              item['theatres'] = row.xpath('./td[10]/text()').extract()[0]
              item['release_date'] = row.xpath('./td[11]/text()').extract()[0] + ' ' + year
              # item['distributor'] = row.xpath('./td[13]/a/text()').extract()[0]
              item['opening'] = row.xpath('./td[8]/text()').extract()[0]
              #print(item)
              # yield item
              yield scrapy.Request(url, self.parse_link, meta={'item': item})
            except IndexError:
              print(row.xpath('./td[13]').extract())
            # scrapy.Request(url, self.parse_link)

    def parse_link(self, response):

        item = response.meta.get('item') #since there are no return values this is how to return item
        distributor = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Distributor"]/span[2]/text()').extract() 
        running_time = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Running Time"]/span[2]/text()').extract()
        genres = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "Genres"]/span[2]/text()').extract()
        mpaa = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span = "MPAA"]/span[2]/text()').extract()

        budget = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[span[1] = "Budget"]//span[@class="money"]/text()').extract()
        #distributor = data.xpath('[span[1]="Distributor"]/span[2].text()').extract()
        # movie_title = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
        #print(movie_title)

        #title and field name must match
        item['distributor'] = "-" if len(distributor) == 0 else distributor[0]
        item['running_time'] = "-" if len(running_time) == 0 else running_time[0]
        item['genres'] = "-" if len(genres) == 0 else genres[0]
        item['mpaa'] = "-" if len(mpaa) == 0 else mpaa[0]
        item['budget'] = "-" if len(budget) == 0 else budget[0]
        print(item)
        yield item