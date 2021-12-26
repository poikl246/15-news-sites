import csv

a = ([], [[[0, 0, 1], 'https://moderator.az/siyaset/400477/belarusun-kecmis-rehberi-moskva-ve-minsk-1991-ci-ilde-defn-etdiyimiz-imperiyani-dirildir/'], [[0, 0, 1], 'https://moderator.az/siyaset/400413/adas-dvrde-butv-azerbaycan-ideyasi-ve-butv-azerbaycan-ocaqlari/']])



ojr = [['adamlarınız', 'personalı'], ['pisləşməsi'], ['göstərir']]

def output_csv(parsing_data, input_data, name):
    data = parsing_data[1]
    # print(data)
    liner = [[name, ' ']]
    for in_data in input_data:
        liner[0].append(str(in_data).replace('"', '').replace(']', '').replace('[', '').replace("'", "").replace('\u0131', ''))
        print(str(in_data).replace('"', '').replace(']', '').replace('[', '').replace("'", "").replace('\u0131', ''))


    for line in data:
        liner.append([' '] + [line[1]] + line[0])

    print(liner)

    with open('exit_data.csv', 'a', encoding='cp1251', newline='') as file:   # cp1251
        writer = csv.writer(file, delimiter=';')
        writer.writerows(liner)


output_csv(parsing_data=a, input_data=ojr, name='parser')