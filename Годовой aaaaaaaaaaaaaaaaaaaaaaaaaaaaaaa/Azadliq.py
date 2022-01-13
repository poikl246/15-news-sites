import asyncio
import os
import random

import pyglet
from fuzzywuzzy import fuzz
import time
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
from fake_useragent import UserAgent

dltjkgndl = []

monthes = [

    "0",
    "Yanvar",
    "Fevral",
    "Mart",
    "Aprel",
    "May",
    "İyun",
    "İyul",
    "Avqust",
    "Sentyabr",
    "Oktyabr",
    "Noyabr",
    "Dekabr"

]

us = UserAgent()
print(us.random)

def parsing(data_master_scan_in, data_time=(time.time())):

    url_list_output = []

    output_data = []


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

        print("BANNNN", url_list)
        # print(url_list[])

        dltjkgndl = []


        for e, url, caunt in url_list:

            with open(fr'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\azadliq_error.txt', 'a', encoding='utf-8') as file:
                for skngk in url_list:
                    file.write(f'{url} {caunt}')

            print(url[-5:])
            if url[-5:] != '.docx':
                resp = request_no_error(url, caunt=caunt).text

                soup = bs(resp, 'html.parser')

                titul = soup.find("title").text
                print(titul)

                # -----------------------------------------------------------------------------------
                # Достать статью в переменную txt

                tttt = ""
                tttt = soup.find(class_='wsw')
                txxt = ""
                txxt = bs(str(tttt), "html.parser").findAll("p")
                txt = ""
                for i in txxt:
                    txt += i.text + "\n"

                print(url, titul, txt)

                with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                    file.write(url + '\n\n' + titul + '\n\n' + txt)


    async def fetch_url_data(session, url, caunt, data_master_scan):
        print(url, caunt)
        headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                   'User-Agent': f'{us.random}',
                   'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}
        try:


            async with session.get(url, headers=headers) as response:
                resp = await response.text()
                # print(resp)
                soup = bs(resp, 'html.parser')

                titul = soup.find("title").text
                print(titul)

                # -----------------------------------------------------------------------------------
                # Достать статью в переменную txt

                tttt = ""
                tttt = soup.find(class_='wsw')
                txxt = ""
                txxt = bs(str(tttt),"html.parser").findAll("p")
                txt = ""
                for i in txxt:
                    txt+=i.text+"\n"

                print(url, titul, txt)

                with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                    file.write(url + '\n\n' + titul + '\n\n' + txt)

                # exit()

                # ---------------------------------------Обработчик, можно не трогать----------------------------------------------




        except Exception as e:
            print(e, url, caunt)
            dltjkgndl.append([123, url, caunt])
        else:
            return resp



    async def fetch_async(url_lists):
        tasks = []
        async with ClientSession() as session:
            for url, caint, data_master_scan_in in url_lists:
                # print(url)
                task = asyncio.ensure_future(fetch_url_data(session, url, caint, data_master_scan_in))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
        return responses






    def pars(data_master_scan_in, data_time=(time.time())):

        # ******************************************************************************************************************************************

        url_list_output = []
        output_data = []

        data_time = time.localtime(data_time)
        print(data_time)
        print(data_time[0])
        print(data_time)
        day = str(data_time[2])
        month = str(data_time[1])
        year = str(data_time[0])

        timer = time.time()
        urls_list = []
        caunt = 0

        os.mkdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\azadliq\{year}-{month}-{day}')

        os.chdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\azadliq\{year}-{month}-{day}')

        # ******************************************************************************************************************************************
        # Тут нормальный парсинг, нужно достать ссылки на новости

        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↓
        stop = 0
        page = 0
        while(not (stop)):
            headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                    'User-Agent': f'{us.random}',
                    'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}
            url = 'https://www.azadliq.org/azadl%C4%B1q_radiosu_m%C9%99qal%C9%99l%C9%99r?p=' + str(page) + '&d=' + day + '&m=' + month + '&y='+ year

            print(url)

            req = requests.get(url, headers=headers)

            src = req.text
            # print(src)
            soup = bs(src, 'html.parser')
            if len(soup.findAll(class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 fui-grid__inner")) > 0:
                for stat in soup.findAll(class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 fui-grid__inner"):
                    soap = bs(str(stat), 'html.parser')
                    asd = soap.find(class_="date date--mb date--size-3")
                    m = monthes.index(asd.text.split()[0])
                    d = asd.text.split()[1].replace(",","")
                    y = asd.text.split()[2]
                    if(int(d) == int(day)):
                        print(str(stat).find('a'))
                        if str(stat).find('a') != None:
                            print("[DEBUG] find <a>")
                            for url_n in soap.findAll('a'):
                                if urls_list.count(url_n.get('href')) == 0:
                                    urls_list.append(["https://www.azadliq.org"+url_n.get('href'), caunt, data_master_scan_in])
                                    caunt += 1  # Это нужно оставить, так как по нему создаются файлы txt
                                # break
                        else:
                            stop = 1
                            break
                    elif (int(d) < int(day)):
                        stop = 1
                        print("[DEBUG] ", page)
                        break
            else:
                stop = 1
                print("[DEBUG] ", page)
                break

            page+=1
        
        print(urls_list)
        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↑
    
        # time.sleep(2)
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(urls_list))
        loop.run_until_complete(future)

        print(time.time() - timer)

        url_rest = dltjkgndl
        restart_url_ban(url_rest)




    pars(data_master_scan_in, data_time)

    # return url_list_output, output_data

if __name__ == "__main__":
    start_pap = os.getcwd()
    try:
        ojr = [['məclis', 'milli'], ['Mehmet'], ['k']]
        start_pap = os.getcwd()

        max_n = 371
        # max_n = 2

        for skejb in range(371, 372):

            parsing(data_master_scan_in= ojr, data_time=int(time.time() - skejb * 24*60*60))

            print('\n\n\n\n\n\n\n\n\n exit \n\n\n\n\n\n')
            print(dltjkgndl)

            os.chdir(start_pap)

            with open('azadliq_error.txt', 'a', encoding='utf-8') as file:
                for i in dltjkgndl:
                    file.write(f'{i[1]}\n')
            print('Типа спим')

            time_sleeep = 30

            if skejb % 20 == 0:
                for temer_start in range(time_sleeep, 0, -1):
                    print(f'До запуска {temer_start} сек\nЭтап {skejb}/{max_n}')
                    time.sleep(1)
                dltjkgndl = []

        print("stop")
        song = pyglet.media.load('U-TOPIA_-_Behind_the_scene.mp3')
        song.play()
        pyglet.app.run()

    except Exception as e:
        print(e)
        os.chdir(start_pap)
        song = pyglet.media.load('Top Secret - Main theme(original).mp3')
        song.play()
        pyglet.app.run()

# Ну потом можно принты почистить, просто не очень прикольно смотреть на пустую консоль