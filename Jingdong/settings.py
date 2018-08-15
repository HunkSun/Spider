# -*- coding: utf-8 -*-

# Scrapy settings for Jingdong project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Jingdong'

SPIDER_MODULES = ['Jingdong.spiders']
NEWSPIDER_MODULE = 'Jingdong.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   ':authority': 'search.jd.com',
   ':method': 'GET',
   ':path': '/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&stock=1&page=3&s=1&click=0',
   ':scheme': 'https',
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'accept-encoding': 'gzip, deflate, br',
   'accept-language': 'zh-CN,zh;q=0.9',
   'cache-control': 'max-age=0',
   'cookie': '__jdc=122270672; __jdu=15338639093011992102218; PCSYCityID=1213; shshshfp=38db0cdb464d112082089ddce155a4'
             '4b; shshshfpa=8707c18d-aad3-e463-184b-157cd66d742d-1533863910; shshshfpb=15b161f01c8d64dbcb2fe336e2e46242'
             '345d834af6286617c5b6ce7e63; xtest=1278.cf6b6759; ipLoc-djd=1-72-2799-0; Hm_lvt_e60c55838acbc89c7409eced09'
             '1b4723=1533863915; 3AB9D23F7A4B3C9B=GOAV3WVOEMBV3T7H3QDGFHTD4N5WDUHR2UE3FMFSPNQ3TBFOZBHZGH57W7QEW2IBVU54A'
             'UTZXB35DADIMOUVUDK6KE; qrsc=3; rkv=V0300; __jda=122270672.15338639093011992102218.1533863909.1533880869.'
             '1533885146.5; unpl=V2_ZzNtbUAASh11DBZTfh8IBmJXRV8RUkVFfQ4RA3wdCFc1BRsOclRCFXwUR11nGV0UZwcZXUFcRhNFCHZUehh'
             'dBWYGF1lKZ3Mldgh2UEsZWAdlChVfSlZLF3QIRlxzGlwEZAASVHJnRCVFOEdkeildNSoDFl9AXkQXfQlOVnoZXA1vABJcQVRDHEUJdlc'
             '%3d; CCC_SE=ADC_oQL%2bhjj7SdDY5mt%2bRD1J%2fkZdpLZ7rWZ9BvFQ1mkiCcHplfYZgzx0H2%2bpni8%2b%2f%2b2cgWVSknXf%2f'
             'nbw71GDxrH1UMr2AiUen4rtSJZ0DHLewsvczKOkQIdwjQFjLMsxXTcTuBYtEuBgBC4ipxuR90a%2b97BQjGd1YOj98EgDo59LBMz49U6M'
             'i7Lf6JuhyOqs2J%2b01kybzdC%2bm5vBAaKDCSGLFpf%2bwh7LIVjZWjNIVRspIYwWPj%2b5qIX549gwnh9kXGz52bJs0abNqtYgEcKJ9'
             'cTRejbxN5Mo%2bW6Hy2E1LiVGZhldLEv5pByFrwbpSXON%2bA5fNUC794O5HLSHXn5idpQlJ4BcoT2TRx4kyDn6cqK84HhvK5ecC2alSg'
             'bY3%2fBxxpphFJy1eEykCPokQuPDY9GRnXSgqCfTa9d64eZIkX%2bp%2fyYkJoWeu2i%2fvnBG5gFUVXtZ4XZpiN5hgD4zY1LqrIdJOXh'
             'dXLPZghjZ%2faOCJNIOMCh5wDrPRfClAowVT6wmtDh8; __jdb=122270672.2.15338639093011992102218|5.1533885146; __jd'
             'v=122270672|www.piadu.com|t_1000104459_|tuiguang|3f8915a647e24ef3b47a97ff65ecc78b-p_1217413149|1533885168'
             '743; shshshsID=dce2bdf7f905ce85a3d5e263f2d63ade_2_1533885168950; Hm_lpvt_e60c55838acbc89c7409eced091b472'
             '3=1533885169',
   'upgrade-insecure-requests': '1',
   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Jingdong.middlewares.JingdongSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Jingdong.middlewares.JingdongDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Jingdong.pipelines.JingdongPipeline': 300,
    # 'Jingdong.pipelines.MongoDBPipeline': 301,
    'Jingdong.pipelines.MySQLPipeline': 302
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
