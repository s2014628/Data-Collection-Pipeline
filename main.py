from scraper import Scraper
import time

if __name__=='__main__':
    bot=Scraper('https://www.ocado.com/')
    bot.accept_cookies()
    time.sleep(1)
    bot.browse_button()
    time.sleep(1)
    bot.search_bar()
    time.sleep(10)


   