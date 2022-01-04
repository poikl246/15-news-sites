import random
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv
import os
from fake_useragent import UserAgent
st = 'rkjg'
print(' '.join(format(ord(x), 'b') for x in st))
ua = UserAgent()

url = 'https://urfu.ru/fileadmin/ratings/27_00212_1640059789.html'

headers = {"authority": "modern.az",
'method': 'GET',
'path': '/az/all/date/2021-12-19?page=2',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'utf-8',
'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie': 'PHPSESSID=o4tneik48tskdhkshhge2vk7i6',
'referer': 'https://modern.az/az/all/date/2021-12-19',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'}

# proxies = {
#     'https://':'198.27.74.6:9300'
# }




req = requests.get(url, headers=headers)


code_list = ['ascii',
 'big5',
 'big5hkscs',
 'cp037',
 'cp273',
 'cp424',
 'cp437',
 'cp500',
 'cp720',
 'cp737',
 'cp775',
 'cp850',
 'cp852',
 'cp855',
 'cp856',
 'cp857',
 'cp858',
 'cp860',
 'cp861',
 'cp862',
 'cp863',
 'cp864',
 'cp865',
 'cp866',
 'cp869',
 'cp874',
 'cp875',
 'cp932',
 'cp949',
 'cp950',
 'cp1006',
 'cp1026',
 'cp1125',
 'cp1140',
 'cp1250',
 'cp1251',
 'cp1252',
 'cp1253',
 'cp1254',
 'cp1255',
 'cp1256',
 'cp1257',
 'cp1258',
 'cp65001',
 'euc_jp',
 'euc_jis_2004',
 'euc_jisx0213',
 'euc_kr',
 'gb2312',
 'gbk',
 'gb18030',
 'hz',
 'iso2022_jp',
 'iso2022_jp_1',
 'iso2022_jp_2',
 'iso2022_jp_2004',
 'iso2022_jp_3',
 'iso2022_jp_ext',
 'iso2022_kr',
 'latin_1',
 'iso8859_2',
 'iso8859_3',
 'iso8859_4',
 'iso8859_5',
 'iso8859_6',
 'iso8859_7',
 'iso8859_8',
 'iso8859_9',
 'iso8859_10',
 'iso8859_11',
 'iso8859_13',
 'iso8859_14',
 'iso8859_15',
 'iso8859_16',
 'johab',
 'koi8_r',
 'koi8_t',
 'koi8_u',
 'kz1048',
 'mac_cyrillic',
 'mac_greek',
 'mac_iceland',
 'mac_latin2',
 'mac_roman',
 'mac_turkish',
 'ptcp154',
 'shift_jis',
 'shift_jis_2004',
 'shift_jisx0213',
 'utf_32',
 'utf_32_be',
 'utf_32_le',
 'utf_16',
 'utf_16_be',
 'utf_16_le',
 'utf_7',
 'utf_8',
 'utf_8_sig']





caunt = 40

req.encoding = 'utf-8'
print(req.text)
print("\n\n")
print(req.encoding)
print(f'{caunt}/{len(code_list)} \n\n')
time.sleep(2)

for i in code_list[40:45]:

    req.encoding = i
    print(req.text)
    print("\n\n")
    print(req.encoding)
    print(f'{caunt}/{len(code_list)} \n\n')
    time.sleep(2)
    caunt += 1
# print(req.content)
#
# with open("index.html", "wb") as file:
#     file.write(req.content)
# #
# # print(src)
#
# with open("index.html", encoding='utf-8') as file:
#     src = file.read()
#
# # print(src)
# soup = BeautifulSoup(src, 'html.parser')



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
# with open('exit_data.csv', 'w', encoding='utf-8', newline='') as file:   # cp1251
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
