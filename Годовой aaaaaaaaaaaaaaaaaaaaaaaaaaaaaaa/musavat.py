import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from multiprocessing import Pool
import random
from fuzzywuzzy import fuzz


# options

url_list_output = []

output_data = []
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", True)


# headless mode
options.headless = True



def func_chunks_generators(seq, size):
    return (seq[i::size] for i in range(size))



# data_master_scan = []
def get_data(url_list):
    try:
        driver = webdriver.Firefox(
            executable_path=fr"F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\geckodriver.exe",
            options=options
        )

        # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
        # r"C:\users\selenium_python\chromedriver\chromedriver.exe"
        for url, caunt, data_master_scan in url_list:
            driver.get(url=url)
            time.sleep(2)
            src = driver.page_source
            soup = BeautifulSoup(src, 'html.parser')
            titul = soup.find("title").text
            txt = soup.find(class_="news-content").text.replace('\n', ' ')
            print(titul, txt)

            with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                file.write(url + '\n\n' + titul + '\n\n' + txt)


        time.sleep(random.randrange(1, 5))


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
            executable_path=fr"F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\geckodriver.exe",
            options=options
        )
        os.mkdir(fr'{data_time[0]}-{data_time[1]}-{data_time[2]}')
        os.chdir(fr'{data_time[0]}-{data_time[1]}-{data_time[2]}')
        # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
        # r"C:\users\selenium_python\chromedriver\chromedriver.exe"

        driver.get(url='https://musavat.com/archive')
        time.sleep(4)
        caunt_l = 0
        for i in range(1, 1000):
            url = f'https://musavat.com/search?text=&type=news&date_begin={data_time[2]}.{data_time[1]}.{data_time[0]}&date_end={data_time2[2]}.{data_time2[1]}.{data_time2[0]}&id_news_category=&id_author=&page={i}'
            driver.get(url=url)
            time.sleep(4)
            src = driver.page_source
            # print(data_master_scan_in)
            try:
                soup = BeautifulSoup(src, 'html.parser')

                if int(soup.find(class_='pagination').find_all('li')[-2].text) == i:

                    return url_list_out



                for data in soup.find_all(class_='form-group col-sm-3 col-md-3'):
                    if data.find('a') != None:
                        ur = 'https://musavat.com' + data.find('a').get('href')
                        print(ur)
                        url_list_out.append([ur, caunt_l, data_master_scan_in])
                        caunt_l += 1

                print(url_list_out)


            except:
                print('NO')


        return url_list_out

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def parsing(data_master_scan_in, data_time=(time.time()), process_count = 1):

    url_list_output = []

    # with open(f'files/Musavat.com/123.txt', 'w', encoding='utf-8') as file:
    #     file.write('')


    # exit()

    # process_count = int(input("Enter the number of processes: "))
    #process_count = 6


    urls_list = list(func_chunks_generators(pars_one(data_master_scan_in, data_time), process_count))
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)



    out_data_list = []




if __name__ == "__main__":
    ojr = [['əlaqəsini', 'həyata'], ['edən'], ['k']]
    sieufgbj = 1642087581.392654

    start_pap = rf'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\парсинг\files'
    for timer in range(13, 380):
        if timer % 5 == 0:
            time.sleep(30)
        os.chdir(start_pap)
        print(parsing(data_master_scan_in = ojr, data_time=int(sieufgbj - timer*24*60*60), process_count=5))
        os.chdir(start_pap)
        time.sleep(5)
