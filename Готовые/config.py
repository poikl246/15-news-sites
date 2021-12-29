import csv
ojr = [['olunmuş', 'atəşfəşanlığı'], ['bilməməsi'], ['keçirilən']]

srkjb = [[], [[[0, 1, 0], 'https://www.yeniavaz.com/az/news/185588/meshur-sirket-abs-da-magazalarini-bagladi'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184248/bu-mehsullarin-idxalina-qadaga-qoyuldu'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184247/israil-sefiri-azerbaycana-bassagligi-verib'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/185597/abs-da-kecmis-bas-qerargah-reisinin-edam-olunmasi-teklif-edilib'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184240/bas-prokurorlugun-sorgusu-ile-bagli-konstitusiya-mehkemesi-qerar-verdi'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184238/polis-narkotik-emeliyyati-kecirdi-22-nefer-saxlanildi-video'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/185596/saatlida-qardas-qardasi-kureyinden-bicaqlayib-qetle-yetirdi'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184236/telegramda-vetendaslari-santaj-eden-adminler-saxlanildi-video'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184228/turkiyenin-4-herbcisi-sehid-olub'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184221/azerbaycanda-hebsde-iken-olen-yuksek-vezifeli-sexsler-siyahi'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184220/mingecevirde-sagirdler-narkomaniya-ile-bagli-maariflendirilibler-fotolar'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184217/amea-ve-bdu-nun-tenderlerinde-qalib-olan-kemale-rasimli-kimdir-direktor-muavini-tercumeci-yoxsa-sahibkar-fotolar'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184216/caycisini-sirket-direktoru-qoyub-oglunu-da-muavin-teyin-edib-mehkeme'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/185594/parlamentin-payiz-sessiyasinda-bu-qanun-layiheleri-qebul-edilmedi-siyahi'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184213/dasaltidaki-partlayisda-iki-mina-ust-uste-qoyulubmus-aciqlama'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184211/media-reyestrine-daxil-edilen-jurnalistlere-vahid-vesiqe-verilecek'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/185593/kerim-veliyev-komandolarla-gorusdu-fotolar'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184204/irandan-narkotik-kecirmek-isteyen-sexs-serhedcilere-bicaq-cekib-fotolar'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184203/rusiyada-islemeye-geden-101-nefere-saxta-covid-pasportu-veribler'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184202/ali-mehkeme-agdam-bandasinin-bascisi-ile-bagli-qerari-elan-edib'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184201/turmede-olen-polkovnike-xanlar-veliyevin-protestinden-sonra-omurluk-ceza-verilmisdi'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184200/nazirlikden-omikron-stami-ile-bagli-ehaliye-cagiris'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184197/rusiya-turkiyeye-elave-s-400-partiyasi-gondermeyi-planlasdirir'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184196/bu-gun-saakasvilinin-novbeti-mehkemesi-kecirilecek'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184176/bu-gun-metroda-olen-sexs-bdu-nun-bas-muellimi-imis-foto-yenilenib'], [[1, 1, 0], 'https://www.yeniavaz.com/az/news/184184/beraet-alan-elcin-qardasini-buna-gore-oldurubmus-teferruat'], [[0, 1, 0], 'https://www.yeniavaz.com/az/news/184178/agdasda-narkotik-istifade-eden-19-surucu-askarlanib']]]








def output_csv(parsing_data, input_data, name):
    data = parsing_data[1]
    liner = [[name, ' ']]
    for in_data in input_data:
        liner[0].append(str(in_data).replace('"', '').replace(']', '').replace('[', '').replace("'", "").replace('\u0131', ''))



    for line in data:
        liner.append([' '] + [line[1]] + line[0])

    caunt_list = [0] * int(len(data[0][0]))

    for dat in data:

        list_loc = []
        for caunt__ in range(len(dat[0])):
            caunt_list[caunt__] = (int(caunt_list[caunt__]) +  int(dat[0][caunt__]))


    out_list = [" ", " "]
    out_list.extend(caunt_list)


    liner.append([])
    liner.append(out_list)

    #
    with open('Data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(liner)

    return caunt_list


output_csv(srkjb, ojr, 'jrgnl')

def exit_code(caunt_list):
    out_list = [" ", " "]
    out_list.extend(caunt_list)
    liner = []
    liner.append([])
    liner.append([])
    liner.append([])
    liner.append([])
    liner.append(out_list)

    #
    with open('Data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(liner)

def input_data():
    with open("Input.csv", 'r', encoding='utf-8') as r_file:
        file = r_file.readlines()
    dat = []
    for f in file:
        local = []
        for w in f.replace('\n', '').split(';'):
            if w != '':
                local.append(w)
        dat.append(local)


    return dat

