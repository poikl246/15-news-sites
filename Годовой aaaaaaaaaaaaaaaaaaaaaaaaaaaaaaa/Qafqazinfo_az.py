import asyncio
import os
import random
from fuzzywuzzy import fuzz
import time
from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs
import requests
from fake_useragent import UserAgent

us = UserAgent()
print(us.random)

def parsing(data_master_scan_in, data_time=(time.time())):

    url_list_output = []

    output_data = []

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
                tttt = soup.find(class_='panel-body news_text')
                txxt = ""
                txxt = bs(str(tttt),"html.parser").findAll("p")
                txt = ""
                for i in txxt:
                    txt+=i.text+"\n"


                # ---------------------------------------Обработчик, можно не трогать----------------------------------------------


                text_list = txt.lower().split(' ')
                # print(text_list)
                # caunt_local = 0

                exit_data = []
                for one_line in data_master_scan:
                    caunt_local = 0
                    for twe in one_line:
                        for master_text in text_list:
                            if fuzz.ratio(master_text, twe) >= 65:
                                caunt_local += 1
                                break

                    if caunt_local == len(one_line):
                        exit_data.append(1)
                    else:
                        exit_data.append(0)

                print(exit_data, url)

                # ******************************************************************************************************************************************

                if exit_data.count(1) != 0:
                    if os.listdir('files/'+"Qafqazinfo.az") == []:
                        try:
                            with open(f'files/'+ "Qafqazinfo.az" +'/text_'+ str(caunt) +'.txt', 'w', encoding='utf-8') as file:
                                file.write(f'{url}\n\n{titul}\n\n{txt}')

                        except Exception as a:
                            print(a)
                        output_data.append([exit_data, url])

                    # ----------------------------------------------не трогать-------------------------------------------------------------


                    else:
                        for dir_site in os.listdir('files'):
                            for dir_page in os.listdir(f'files/{dir_site}'):
                                with open(f'files/{dir_site}/{dir_page}', 'r',encoding="utf-8") as file:
                                    file.readline()
                                    file.readline()
                                    file.readline()
                                    if fuzz.ratio(txt, file.read()) >= 50:
                                        return 0

                        # ******************************************************************************************************************************************

                        try:
                            with open(f'files/'+ "Qafqazinfo.az" +'/text_'+ str(caunt) +'.txt', 'w', encoding='utf-8') as file:
                                file.write(f'{url}\n\n{titul}\n\n{txt}')
                                output_data.append([exit_data, url])


                        except Exception as a:
                            print(a)

                    # ******************************************************************************************************************************************




                    print(output_data)


                    # типа проверка статьи






                # exit()





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

        if int(day) // 10 == 0:
            day = "0"+day
        if int(month) // 10 == 0:
            month = "0"+month

        timer = time.time()
        urls_list = []
        caunt = 0


        # ******************************************************************************************************************************************
        # Тут нормальный парсинг, нужно достать ссылки на новости

        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↓
        checked = 0
        pages = 1
        p = 1
        while pages >= p:
            headers = {'Accept': '*/*', 
            'Connection': 'keep-alive',
            'User-Agent': us.random,
            'Cache-Control': 'max-age=0', 'DNT': '1', 
            'Upgrade-Insecure-Requests': '1',
            }
            page = requests.get("https://qafqazinfo.az/news/arxiv/"+ year +"-" +month+ "-" +day+ "?page="+str(p),headers=headers)
            print("https://qafqazinfo.az/news/arxiv/"+ year +"-" +month+ "-" +day+ "?page="+str(p))
            soup = bs(page.text,"html.parser")
            all_news = soup.findAll(class_ = "row search")
            if(checked):
                pass
            else:
                try:
                    pages = int(soup.findAll(class_ = "page")[-1].text)
                except:
                    pass
                checked = 1
            for news in all_news:
                link = bs(str(news),"html.parser").findAll("a")[0]["href"]
                urls_list.append([link, caunt, data_master_scan_in])
                caunt+=1
            if(p <= pages):
                p+=1
        print("[URLS_LIST]",urls_list)
        
        # УСЛОВНО РАЗВЕКАТЬСЯ МОЖНО ВОТ ТУТ ↑
        # time.sleep(2)
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(urls_list))
        loop.run_until_complete(future)

        print(time.time() - timer)



    pars(data_master_scan_in, data_time)

    return url_list_output, output_data

if __name__ == "__main__":
    ojr = [['milli'], ['məclis'], ['k']]
    parsing(data_master_scan_in = ojr, data_time=int(time.time()))

# Ну потом можно принты почистить, просто не очень прикольно смотреть на пустую консоль

