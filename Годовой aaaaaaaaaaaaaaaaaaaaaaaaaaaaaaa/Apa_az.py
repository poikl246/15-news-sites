import asyncio
import os
import random

import pyglet
from fuzzywuzzy import fuzz
import time
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import sys

us = UserAgent()
print(us.random)
dltjkgndl = []


def parsing(data_time=(time.time())):
    def request_no_error(url, caunt = 000000, retry=5):

        headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                   'User-Agent': f'{us.random}',
                   'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}
        try:
            response = requests.get(url=url, headers=headers)
            print(f"[+] {url} {response.status_code}")
            if response.status_code != 200:
                lsrgknjosrbg = 100 / 0
        except Exception as ex:
            time.sleep(15)
            if retry:
                print(f"[INFO] retry={retry} => {url}")
                return request_no_error(url, retry=(retry - 1))
            else:
                dltjkgndl.append([ex, url, caunt])
        else:
            return response

    url_list_output = []

    output_data = []


    def restart_url_ban(url_list):

        with open(fr'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\apa_error_2.txt', 'a', encoding='utf-8') as file:
            for skngk in url_list:
                file.write(f'{url_list[1]} {url_list[2]}')
        dltjkgndl = []


        for e, url, caunt in url_list:
            resp = request_no_error(url, caunt=caunt).text

            soup = BeautifulSoup(resp, 'html.parser')

            try:
                text = url + '\n\n' + soup.find(class_='title_news mb-site').text + '\n\n' + soup.find(
                    class_='news_content mt-site').text.replace('\n', '')
            except:
                text = url + '\n\n' + soup.find(class_='title_news mb-site').text + '\n\n' + soup.find(
                    class_='texts mb-site').text.replace('\n', '')

            print(soup.find(class_='title_news mb-site').text)

            with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                file.write(url + '\n\n' + text)


    async def fetch_url_data(session, url, caunt):
        print(url, caunt)
        headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                   'User-Agent': f'{us.random}',
                   'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}
        try:


            async with session.get(url, headers=headers) as response:
                resp = await response.text()
                # print(resp)
                soup = BeautifulSoup(resp, 'html.parser')


                try:
                    text = url + '\n\n' + soup.find(class_='title_news mb-site').text + '\n\n' + soup.find(class_='news_content mt-site').text.replace('\n', '')
                except:
                    text = url + '\n\n' + soup.find(class_='title_news mb-site').text + '\n\n' + soup.find(class_='texts mb-site').text.replace('\n', '')

                print(soup.find(class_='title_news mb-site').text)

                with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                    file.write(url + '\n\n' + text)






                # exit()




        except Exception as e:
            print(e, url, caunt)
            dltjkgndl.append([e, url, caunt])
        else:
            return resp
        return


    async def fetch_async(url_lists):
        tasks = []
        async with ClientSession() as session:
            for url, caint in url_lists:
                # print(url)
                task = asyncio.ensure_future(fetch_url_data(session, url, caint))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
        return responses






    def pars(data_time=(time.time())):



        # ******************************************************************************************************************************************

        kjsebgk = 0
        url_list_output = []
        output_data = []
        timer = time.time()
        urls_list = []
        headers = {'Accept': '*/*',
                   'Connection': 'keep-alive',
                   'User-Agent': us.random,
                   'Cache-Control': 'max-age=0', 'DNT': '1',
                   'Upgrade-Insecure-Requests': '1',
                   }

        if data_time < 12:
            year = "2021"
            month = str(data_time)
            month_ = str(data_time + 1)
            year_ = "2021"
        elif data_time == 12 :
            year = "2021"
            month = str(data_time)
            month_ = str(1)
            year_ = '2022'
        else:
            year = "2022"
            month = str(data_time - 12)
            year_ = "2022"
            month_ = str(data_time - 11)

        os.mkdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\apa\{year}-{month}')

        os.chdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\apa\{year}-{month}')

        print(year, month, year_, month_)
        url = f'https://apa.az/az/archive/search-result?search=&site_type=1&type=4&start_date={month}%2F1%2F{year}&end_date={month_}%2F0%2F{year_}'
        src = requests.get(url=url, headers=headers).text
        soup = BeautifulSoup(src, 'html.parser')

        page_Nom = int(soup.find(class_='pagination').find_all('li')[-2].text) + 1
        print(page_Nom)

        # page_Nom = 3

        for page_N in range(1, page_Nom):
            print(page_N)

            headers = {'Accept': '*/*',
                       'Connection': 'keep-alive',
                       'User-Agent': us.random,
                       'Cache-Control': 'max-age=0', 'DNT': '1',
                       'Upgrade-Insecure-Requests': '1',
                       }

            url = f'https://apa.az/az/archive/search-result?search=&site_type=1&type=4&start_date={month}%2F1%2F{year}&end_date={month_}%2F0%2F{year_}&type=4&site_type=1&page={page_N}'
            src = request_no_error(url=url).text
            soup = BeautifulSoup(src, 'html.parser')
            for blok in soup.find(class_='four_columns_block mt-site').find_all('a'):
                if blok.get('href') != 'javascript:void(0)':
                    urls_list.append([blok.get('href'), kjsebgk])
                    kjsebgk += 1
            print(urls_list)


        print("[URLS_LIST]", urls_list)
        # exit()

        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↑

        # time.sleep(2)
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(urls_list))
        loop.run_until_complete(future)

        print(time.time() - timer)


        url_rest = dltjkgndl
        restart_url_ban(url_rest)




    pars(data_time)

    return url_list_output, output_data

if __name__ == "__main__":
    ojr = [['məclis', 'milli'], ['Mehmet'], ['k']]
    start_pap = os.getcwd()

    max_n = 15
    # max_n = 2

    for skejb in range(2, max_n):

        parsing(data_time=int(skejb))


        print('\n\n\n\n\n\n\n\n\n exit \n\n\n\n\n\n')
        print(dltjkgndl)



        os.chdir(start_pap)

        with open('apa_error.txt', 'a', encoding='utf-8') as file:
            for i in dltjkgndl:
                file.write(f'{i[1]}\n')
        print('Типа спим')

        time_sleeep = 60 * 5

        for temer_start in range(time_sleeep, 0, -1):
            print(f'До запуска {temer_start} сек')
            time.sleep(1)
        dltjkgndl = []

    print("stop")
    song = pyglet.media.load('U-TOPIA_-_Behind_the_scene.mp3')
    song.play()
    pyglet.app.run()

# Ну потом можно принты почистить, просто не очень прикольно смотреть на пустую консоль

