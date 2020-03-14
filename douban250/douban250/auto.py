from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'douban_movie_top250', '-o', 'doubanauto.csv'])
