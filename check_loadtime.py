#!/usr/bin/env python
# -*- coding: utf-8 -*-

from browsermobproxy import Server
from selenium import webdriver
from xvfbwrapper import Xvfb
import json
import argparse
import urlparse
import os


class performance(object):
    # create performance data

    def __init__(self, mob_path):
        # initialize
        from datetime import datetime
        #print "Start: %s" % (datetime.now())
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None

    @staticmethod
    def __store_into_file(args,title, result):
        #store data collected into file
        if 'path' in args:
            har_file = open(args['path'] + '/'+ title + '.har', 'w')
        else:
            har_file = open(title + '.har', 'w')
        har_file.write(str(result))
        har_file.close()

    def __start_server(self):
        # prepare and start server
        self.server = Server(self.browser_mob)
        self.server.start()
        self.proxy = self.server.create_proxy()

    def __start_driver(self, args):
        # prepare and start driver

        # chromedriver
        if args['browser'] == 'chrome':
            #print "Browser: Chrome"
            #print "URL: {0}".format(args['url'])
            #print "Domain: {0}".format(urlparse.urlparse(args['url']).netloc)
            chromedriver = os.getenv("CHROMEDRIVER_PATH", "./chromedriver")
            os.environ["webdriver.chrome.driver"] = chromedriver
            url = urlparse.urlparse(self.proxy.proxy).path
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--proxy-server={0}".format(url))
            chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        # firefox
        if args['browser'] == 'firefox':
            #print "Browser: Firefox"
            profile = webdriver.FirefoxProfile()
            profile.set_proxy(self.proxy.selenium_proxy())
            self.driver = webdriver.Firefox(firefox_profile=profile)

    def start_all(self, args):
        # start server and driver
        self.__start_server()
        self.__start_driver(args)

    def get_onload(self, args):
        # start request and parse response
        self.proxy.new_har(args['url'], options={'captureHeaders': True})
        self.driver.get(args['url'])
        loading_page = json.dumps(self.driver.execute_script(
            "return ( window.performance.timing.loadEventEnd - window.performance.timing.navigationStart )"))
        print "PageOnLoad: %s" % loading_page
        loading_content = json.dumps(self.driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.loadEventStart ) "))
        print "PageContentLoad: %s" % loading_content
        loading_dom = json.dumps(self.driver.execute_script(
            "return (window.performance.timing.domComplete - window.performance.timing.domLoading ) "))
        print "DomContentLoad: %s" % loading_dom

        result = json.dumps(self.proxy.har, ensure_ascii=True)
        self.__store_into_file(args,'har', result)

        performance = json.dumps(self.driver.execute_script("return window.performance"), ensure_ascii=True)
        self.__store_into_file(args,'perf', performance)


    def stop_all(self):
        # stop server and driver
        from datetime import datetime
        print "Finish: %s" % (datetime.now())

        self.server.stop()
        self.driver.quit()

if __name__ == '__main__':
    # for headless execution
    with Xvfb() as xvfb:
        parser = argparse.ArgumentParser(description='Performance Testing using Browsermob-Proxy and Python')
        parser.add_argument('-u', '--url', help='URL to test', required=True)
        parser.add_argument('-b', '--browser', help='Select Chrome or Firefox', required=True)
        parser.add_argument('-p', '--path', help='Select path', required=False)
        args = vars(parser.parse_args())
        path = os.getenv('BROWSERMOB_PROXY_PATH', '/home/rop/browsermob-proxy-2.1.2/bin/browsermob-proxy') # full path to browsermob-proxy - bin file
        RUN = performance(path)
        RUN.start_all(args)
        #RUN.create_har(args)
        RUN.get_onload(args)
        RUN.stop_all()

con = 0
con1 = 0
with open('log/har.har') as data_file:
    d = json.load(data_file)
    for entries in d['log']['entries']:
        con += entries['response']['bodySize']
        con1 += 1
print "CountReq: %s" % con1
print "SizeDownload: %s" % con

with open('log/perf.har') as data_file:
    d = json.load(data_file)
jssize = d['memory']['totalJSHeapSize']
usedJSHeapSize = d['memory']['usedJSHeapSize']
jsHeapSizeLimit = d['memory']['jsHeapSizeLimit']
full = d['timing']

print "totalJSHeapSize: %s" % jssize
print "usedJSHeapSize: %s" % usedJSHeapSize
print "jsHeapSizeLimit: %s" % jsHeapSizeLimit
print "ololo full: %s" % full
