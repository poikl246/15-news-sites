import asyncio
import os
import random
from typing import MappingView

import pyglet
from fuzzywuzzy import fuzz
import time
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

us = UserAgent()
print(us.random)

dltjkgndl=[]


def parsing(data_master_scan_in, data_time=(time.time())):

    url_list_output = []

    output_data = []

    async def fetch_url_data(session, url, caunt):
        print(url, caunt)
        headers = {'Accept': '*/*', 
            'Connection': 'keep-alive',
            'User-Agent': us.random,
            'Cache-Control': 'max-age=0', 'DNT': '1', 
            'Upgrade-Insecure-Requests': '1',
}
        try:


            async with session.get(url, headers=headers) as response:
                resp = await response.text()
                # print(resp)
                soup = BeautifulSoup(resp, 'html.parser')

                try:
                    titul = soup.find(class_="captxt").text
                except:

                    titul = soup.find(class_="urgcaptxt").text


                try:
                    text = soup.find(class_='maincontent').text

                except:
                    text = soup.find(class_='prvNews').text
                    print('Закрыто')
                print(titul, text)

                with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                    file.write(url + '\n\n' + titul + '\n\n' + text)

                # ---------------------------------------Обработчик, можно не трогать----------------------------------------------






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






    def pars(data_master_scan_in, data_time=(time.time())):

        # ******************************************************************************************************************************************

        url_list_output = []
        output_data = []

        if data_time <= 12:
            year = "2021"
            month = str(data_time)
        else:
            year = "2022"
            month = str(data_time - 12)

        timer = time.time()
        urls_list = []
        caunt = 0


        # ******************************************************************************************************************************************
        # Тут нормальный парсинг, нужно достать ссылки на новости

        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↓

        headers = {'Accept': '*/*', 
            'Connection': 'keep-alive',
            'User-Agent': us.random,
            'Cache-Control': 'max-age=0', 'DNT': '1', 
            'Upgrade-Insecure-Requests': '1',
}
        print("https://turan.az/ext/clndr/" +year+ "/" +month+ "/analytics_001_az.htm")
        src = requests.get("https://turan.az/ext/clndr/" +year+ "/" +month+ "/analytics_001_az.htm",headers=headers).text
        soup = BeautifulSoup(src, 'html.parser')

        os.mkdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\turan\{year}-{month}')

        os.chdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\turan\{year}-{month}')

        caunt_ = 0

        for div in soup.find(class_='grid').find_all(class_='grid-item'):
            urls_list.append(['https://turan.az' + div.find(class_='isslstcap').find('a').get('href'), caunt_])
            caunt_ += 1

            # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↑
        # time.sleep(2)
        print(urls_list)
        # exit()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(urls_list))
        loop.run_until_complete(future)

        print(time.time() - timer)






    pars(data_master_scan_in, data_time)

    # return url_list_output, output_data

if __name__ == "__main__":
    ojr = [['Kennedinin', 'əlaqədar'], ['Prezidenti'], ['k']]

    start_pap = os.getcwd()
    # song = pyglet.media.load('U-TOPIA_-_Behind_the_scene.mp3')
    # song.play()
    # pyglet.app.run()

    for skejb in range(1, 4):

        parsing(data_master_scan_in = ojr, data_time=int(skejb))
        print('\n\n\n\n\n\n\n\n\n exit \n\n\n\n\n\n')
        print(dltjkgndl)

        os.chdir(start_pap)

        with open('turan_error.txt', 'a', encoding='utf-8') as file:
            for i in dltjkgndl:
                file.write(f'{i[1]}\n')
        time.sleep(15)
        dltjkgndl = []

    print("stop")
    song = pyglet.media.load('U-TOPIA_-_Behind_the_scene.mp3')
    song.play()
    pyglet.app.run()

# Ну потом можно принты почистить, просто не очень прикольно смотреть на пустую консоль

