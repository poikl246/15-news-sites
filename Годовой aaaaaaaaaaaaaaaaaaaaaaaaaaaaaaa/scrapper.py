import os

os.chdir(r'F:\Parsing\Годовой АААААААААААААААААААААААА\apa\2022-1')

print(os.listdir())
list_data = os.listdir()

for i in range(0, len(list_data) + 10):
    if not f"{i}.txt" in list_data:
        print(i)