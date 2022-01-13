import asyncio
import os
import random
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

                with open(fr'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\meydan_tv_error.txt', 'a', encoding='utf-8') as file:
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
                    tttt = soup.find(class_='entry-content')
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
            "Cookies":"cmplz_consent_status:allow"
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
                tttt = soup.find(class_='entry-content')
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
            dltjkgndl.append([123, url, caunt])
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

        if(int(day) // 10 == 0):
            day = "0" + day
        if(int(month) // 10 == 0):
            month = "0" + month

        timer = time.time()
        urls_list = []
        caunt = 0

        os.mkdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\meydan_tv\{year}-{month}-{day}')

        os.chdir(fr'F:\Parsing\Годовой АААААААААААААААААААААААА\meydan_tv\{year}-{month}-{day}')

        # ******************************************************************************************************************************************
        # Тут нормальный парсинг, нужно достать ссылки на новости

        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↓
        stop = 0
        page = 1
        urls=[]
        while(not(stop)):

            try:
                print("https://www.meydan.tv/az/?sfid=2268&post_date="+day+month+year+"+"+day+month+year+"1&sf_paged="+str(page))
                r = request_no_error("https://www.meydan.tv/az/?sfid=2268&post_date="+day+month+year+"+"+day+month+year+"1&sf_paged="+str(page))
                soup = bs(r.text,"html.parser")

                if len(soup.findAll("article")) == 0:
                    stop = 1
                    print("[STOPPED]")
                    break
                else:
                    for links in soup.findAll("article"):
                        link = bs(str(links),"html.parser").find("a")["href"]
                        try:
                            urls.index(link)
                        except:
                            urls_list.append([link, caunt, data_master_scan_in])
                            urls.append(link)
                            caunt+=1
                page+=1
            except Exception as ex:
                print('\n\n', ex, '\nПроблема при парсинге блоков', "https://www.meydan.tv/az/?sfid=2268&post_date="+day+month+year+"+"+day+month+year+"1&sf_paged="+str(page), '\n\n')


        print("[URLS_LIST]",urls_list)
        
        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↑
    
        # time.sleep(2)
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(urls_list))
        loop.run_until_complete(future)

        print(time.time() - timer)

        url_rest = dltjkgndl
        restart_url_ban(url_rest)




    pars(data_master_scan_in, data_time)

    return url_list_output, output_data

if __name__ == "__main__":
    start_pap = os.getcwd()
    try:
        ojr = [['məclis', 'milli'], ['Mehmet'], ['k']]
        start_pap = os.getcwd()

        max_n = 373
        # max_n = 2

        for skejb in range(372, max_n+1):

            parsing(data_master_scan_in=ojr, data_time=int(time.time() - skejb * 24 * 60 * 60))

            print('\n exit \n\n')
            print(dltjkgndl)

            os.chdir(start_pap)

            with open('azadliq_error.txt', 'a', encoding='utf-8') as file:
                for i in dltjkgndl:
                    file.write(f'{i[1]}\n')
            print('Типа спим')

            time_sleeep = 30

            if skejb % 10 == 0:
                for temer_start in range(time_sleeep, 0, -1):
                    print(f'До запуска {temer_start} сек\nЭтап {skejb}/{max_n}')
                    time.sleep(1)
                dltjkgndl = []

            if skejb % 30 == 0:
                os.startfile(r'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\Top Secret - Main theme(original).mp3')
                input('Меняй ip \n тестовый url https://www.meydan.tv/az/?sfid=2268&post_date=01012021+010120211&sf_paged=1')

        print("stop")
        song = pyglet.media.load('U-TOPIA_-_Behind_the_scene.mp3')
        song.play()
        pyglet.app.run()

    except Exception as e:
        print(e)
        os.chdir(start_pap)
        song = pyglet.media.load(r'F:\Документы\GitHub\15-news-sites\Годовой aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\Top Secret - Main theme(original).mp3')
        song.play()
        pyglet.app.run()

# Ну потом можно принты почистить, просто не очень прикольно смотреть на пустую консоль

