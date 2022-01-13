from bs4 import BeautifulSoup
import asyncio
import os
import random
from typing import MappingView
from fuzzywuzzy import fuzz
import time
from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs
import requests
from fake_useragent import UserAgent
import pyglet

us = UserAgent()
print(us.random)

dltjkgndl = []


def request_no_error(url, caunt = 000000, retry=5):

    headers = {'Accept': '*/*', 'Connection': 'keep-alive',
               'User-Agent': f'{us.random}',
               'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}
    try:
        response = requests.get(url=url, headers=headers)
        print(f"[+] {url} {response.status_code}")
        print(type(response.status_code))
        if response.status_code == 429:
            os.startfile(r'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\Top Secret - Main theme(original).mp3')
            input('Меняй vpn')
            return request_no_error(url, retry=(retry))
        elif response.status_code != 200:
            lsrgknjosrbg = 100 / 0
    except Exception as ex:
        time.sleep(15)
        if retry > 0:
            print(f"[INFO] retry={retry} => {url}")
            return request_no_error(url, retry=(retry - 1))
        if retry == 0:
            os.startfile(r'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\Top Secret - Main theme(original).mp3')
            input('Меняй vpn')
            return request_no_error(url, retry=(retry))
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

        try:

            with open(fr'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\Report_error.txt', 'a', encoding='utf-8') as file:
                for skngk in url_list:
                    file.write(f'{url} {caunt}')

            print(url[-5:])
            if url[-5:] != '.docx':
                resp = request_no_error(url, caunt=caunt).text

                soup = bs(resp, 'html.parser')

                titul = soup.find("title").text

                # -----------------------------------------------------------------------------------
                # Достать статью в переменную txt

                tttt = ""
                tttt = soup.find(class_='editor-body')
                txxt = ""
                txxt = bs(str(tttt), "html.parser").findAll("p")
                txt = ""
                for i in txxt:
                    txt += i.text + "\n"
                print(url, titul, txt)

                with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                    file.write(url + '\n\n' + titul + '\n\n' + txt)
        except:
            print("NO DATA BANN!!!", url)


async def fetch_url_data(session, url, caunt, data_master_scan):
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
            soup = bs(resp, 'html.parser')

            titul = soup.find("title").text

            # -----------------------------------------------------------------------------------
            # Достать статью в переменную txt


            tttt = ""
            tttt = soup.find(class_='editor-body')
            txxt = ""
            txxt = bs(str(tttt),"html.parser").findAll("p")
            txt = ""
            for i in txxt:
                txt+=i.text+"\n"
            print(url, titul, txt)

            with open(f'{caunt}.txt', 'w', encoding='utf-8') as file:
                file.write(url + '\n\n' + titul + '\n\n' + txt)



            # ---------------------------------------Обработчик, можно не трогать----------------------------------------------






    except Exception as e:
        print(e, url, caunt)
    else:
        return resp
    return


async def fetch_async(url_lists):
    tasks = []
    async with ClientSession() as session:
        for url, caint, data_master_scan_in in url_lists:
            # print(url)
            task = asyncio.ensure_future(fetch_url_data(session, url, caint, data_master_scan_in))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses





start_pap = '2021-8-16'
os.mkdir(fr'{start_pap}')

with open(f'парсинг/2021-08-16.html', 'r', encoding='utf-8') as file:
    src = file.read()

# start_pap = os.getcwd()

os.chdir(start_pap)

soup = BeautifulSoup(src, 'html.parser')

urls_list = []
caunt = 0
for data in soup.find_all(class_='news-block'):
    # print(data.find('a').get("href"))
    urls_list.append([data.find('a').get("href"), caunt, []])
    caunt += 1

print(urls_list)
# print(soup.find_all(class_='news-block'))

url_rest = dltjkgndl
restart_url_ban(url_rest)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(fetch_async(urls_list))
loop.run_until_complete(future)