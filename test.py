import random
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv
import os
from fake_useragent import UserAgent


ua = UserAgent()

url = 'https://yenisabah.az/calendar/2021-11-30'

headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52',
                   'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}

# proxies = {
#     'https://':'198.27.74.6:9300'
# }

req = requests.get(url, headers=headers)


src = req.text
# print(src)

with open("index.html", "w", encoding='utf-8') as file:
    file.write(src)
#
# # print(src)
#
# with open("index.html", encoding='utf-8') as file:
#     src = file.read()
#
# # print(src)
soup = BeautifulSoup(src, 'html.parser')
#
# print(soup.find(class_='full-post-title').text)
# print(soup.find(class_='full-post-article').text)


#
#
#
# def request_no_error(url, retry=5):
#
#     try:
#         response = requests.get(url=url, headers=headers)
#         print(f"[+] {url} {response.status_code}")
#     except Exception as ex:
#         time.sleep(3)
#         if retry:
#             print(f"[INFO] retry={retry} => {url}")
#             return request_no_error(url, retry=(retry - 1))
#         else:
#             raise
#     else:
#         return response
#
# with open("lesson12/result.json", "w") as file:
#     json.dump(result_list, file, indent=4, ensure_ascii=False)
#
#
# #
# with open('exit_data.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(file_list)
#
# with open("Input_data/url_list_start.json", "w") as file:
#     json.dump(out_list_json, file, indent=4, ensure_ascii=False)



# video_src_url = 'https://download.samplelib.com/mp4/sample-5s.mp4'
#
# get_video = requests.get(video_src_url, allow_redirects= True, stream=True)
# with open(f"video.mp4", "wb") as video_file:
#     for chunk in get_video.iter_content(chunk_size=1024 * 1024):
#         if chunk:
#             video_file.write(chunk)




# out_list_json = {}
# for i in range(100):
#     # out_list_json.append(i)
#     out_list_json[f'{i}'] = {
#         "квадрат" : i**2,
#         "куб": i**3,
#         "4 степень": i**4,
#     }
#
#
# with open("test.json", "w", encoding='utf-8') as file:
#     json.dump(out_list_json, file, indent=4, ensure_ascii=False)
#
#
#
#
#
# with open("test.json", 'r', encoding='utf-8') as f:
#     templates = json.load(f)
#
# print(templates['10']['куб'])



# with open('sw_data.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
#         print(row['hostname'], row['model'])pen('sw_data.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
#         print(row['hostname'], row['model'])


# with open("config/Suallar1.csv", 'r', encoding='utf-8') as r_file:
#        # Создаем объект DictReader, указываем символ-разделитель ","
#        file_reader = csv.DictReader(r_file, delimiter=";")
#        # Счетчик для подсчета количества строк и вывода заголовков столбцов
#        count = 1
#        # Считывание данных из CSV файла
#        for row in file_reader:
#            data[count] = {
#                'N': row['N'],
#                'Questions': row['Questions'],
#                'Type': row['Type'],
#                "Caunt": row['Caunt'],
#                'answer': f'{variant_otvet(row=row)}'

#            }
#            count += 1

# #    print(data)
# ips = data.keys()
# sorted_ips = sorted(ips, key=lambda ip: data[ip]['Doxodnost'], reverse=True)
# print(sorted_ips)
# knsepgk = [data[ip] for ip in sorted_ips]
# print(knsepgk)
