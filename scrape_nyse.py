from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time
import csv
import datetime

class scrape_nyse():

    def __init__(self, num_loops):
        self.num_loops = int(num_loops)
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.nyse.com/listings_directory/stock")

    def scrape_site(self):
        self.stock_symbols = []
        try:
            for i in range(self.num_loops):
                print (self.stock_symbols)
                time.sleep(5)
                trs = self.driver.find_elements(By.XPATH, '//tr')
                trs = trs[1:]
                for tr in trs:
                    stock_name = " ".join(str(tr.text).split(" ")[1:])
                    self.stock_symbols.append([str(tr.text).split(" ")[0], stock_name])

                next_button = self.driver.find_element_by_xpath(".//a[@rel='next']")
                next_button.click()
        except:
            print ("Your iterations suck")

    def write_scraped_data(self):

        now = datetime.datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        file_write_csv = open("./data/scraped_stocks/scrape_nyse_" + dt_string + ".csv", 'w')
        file_write_csv.write("stock_symbol,stock_name\n")
        for stock_symbol in self.stock_symbols:
            file_write_csv.write(stock_symbol[0] + "," + stock_symbol[1] + "\n")

        file_write_csv.close()
    def stop(self):
        self.driver.close()
    
    def run(self):
        print ("----- Scraping Site -----")
        self.scrape_site()
        print ("----- Writing Scraped Site Data -----")
        self.write_scraped_data()
        print ("----- Stopping -----")
        self.stop()

if __name__ == "__main__":
    
    num_loops = 646
    if len(sys.argv) > 1:
        num_loops = sys.argv[1]
    
    sn = scrape_nyse(num_loops)
    sn.run()