# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv
class MoviePipeline():    
    def __init__(self):
        field_names = ["title", "gross", "theatres", "release_date", "distributor",\
            "opening", "budget", "running_time", "mpaa", "genres"]
        self.csvwriter = csv.DictWriter(open("MovieInfo2002.csv", "w", newline=''), fieldnames=field_names)
        self.csvwriter.writeheader()
    def process_item(self, item, spider):
        self.csvwriter.writerow(item)    
        return item   
    def close_spider(self, spider):
        print("Done")
