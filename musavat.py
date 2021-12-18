import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from multiprocessing import Pool
import random


# options


options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)


# headless mode
# options.headless = False

def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

def get_data(url_list):
    try:
        driver = webdriver.Firefox(
            executable_path=fr"{os.getcwd()}/geckodriver",
            options=options
        )

        # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
        # r"C:\users\selenium_python\chromedriver\chromedriver.exe"
        for url in url_list:
            driver.get(url=url)
            time.sleep(2)

        time.sleep(random.randrange(3, 10))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



def pars_one(data_master_scan_in, data_time=(time.time())):
    try:
        data_time2 = time.localtime(data_time + 24*60*60)
        data_time = time.localtime(data_time)
        print(data_time)
        print(data_time[0])
        print(data_time)
        url_list_out = []
        driver = webdriver.Firefox(
            executable_path=fr"{os.getcwd()}/geckodriver",
            options=options
        )

        # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
        # r"C:\users\selenium_python\chromedriver\chromedriver.exe"

        driver.get(url='https://musavat.com/archive')
        time.sleep(4)

        for i in range(1, 100):
            url = f'https://musavat.com/search?text=&type=news&date_begin={data_time[2]}.{data_time[1]}.{data_time[0]}&date_end={data_time2[2]}.{data_time2[1]}.{data_time2[0]}&id_news_category=&id_author=&page={i}'
            driver.get(url=url)
            time.sleep(4)
            src = driver.page_source

            try:
                soup = BeautifulSoup(src, 'html.parser')

                if int(soup.find(class_='pagination').find_all('li')[-2].text) == i:
                    return url_list_out

                for data in soup.find_all(class_='form-group col-sm-3 col-md-3'):
                    ur = 'https://musavat.com' + data.find('a').get('href')
                    if url_list_out.count(ur) == 0:
                        url_list_out.append(ur)

                print(url_list_out)


            except:
                print('NO')

        time.sleep(1)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def parsing(data_master_scan_in, data_time=(time.time())):

    url_list_output = []

    output_data = []

    print(pars_one(data_master_scan_in, data_time))

    exit()

    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    urls_list = [urls_list]*4
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)


if __name__ == "__main__":
    ojr = [['Kennedinin', 'əlaqədar'], ['bilməməsi'], ['k']]
    parsing(data_master_scan_in = ojr, data_time=int(time.time()))