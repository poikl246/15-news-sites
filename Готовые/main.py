import sys  # sys нужен для передачи argv в QApplication
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import design  # Это наш конвертированный файл дизайна
import time
import shutil
import Qafqazinfo_az, Azadliq, Apa_az, Azertag_az, Meydan_tv, Moderator, Modern, Musavat, Report_az, Aztrend, Turan_az, Yenisabah
import datetime as DT

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindows):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.potoki = 0
        self.names = [

            "Abzas.net",
            "Apa.az",
            "Azadliq.org",
            "Azertag.az",
            "Meydan.tv",
            "Moderator.az",
            "Modern.az",
            "Musavat.com",
            "Qafqazinfo.az",
            "Report.az",
            "Aztrend.az",
            "Turan.az",
            "Yeniavaz.az",
            "Yenisabah.az"

        ]

        self.dickt = {

            "abzas.net":0,
            "apa.az":0,
            "azadliq.org":0,
            "azertag.az":0,
            "meydan.tv":0,
            "moderator.az":0,
            "modern.az":0,
            "musavat.com":0,
            "qafqazinfo.az":0,
            "report.az":0,
            "trend.az":0,
            "turan.az":0,
            "yeniavaz.az":0,
            "yenisabah.az":0

        }

        self.Btn.clicked.connect(self.btn)
        self.abzas.stateChanged.connect(self.Abzaz)
        self.apa.stateChanged.connect(self.Apa)
        self.azadliq.stateChanged.connect(self.Azadliq)
        self.azertag.stateChanged.connect(self.Azertag)
        self.meydan.stateChanged.connect(self.Meydan)
        self.moderator.stateChanged.connect(self.Moderator)
        self.modern.stateChanged.connect(self.Modern)
        self.musavat.stateChanged.connect(self.Musavat)
        self.qafqazinfo.stateChanged.connect(self.Qafqazinfo)
        self.report.stateChanged.connect(self.Report)
        self.trend.stateChanged.connect(self.Trend)
        self.turan.stateChanged.connect(self.Turan)
        self.yeniavaz.stateChanged.connect(self.Yeniavaz)
        self.yenisabah.stateChanged.connect(self.Yenisabah)
        self.show()

    def btn(self):
        self.hide()
        dt = DT.datetime.strptime(self.date.date().toString("dd MM yyyy"), '%d %m %Y')
        da = int(dt.timestamp())
        if not os.path.isdir("files"):
            print("Папка files создана")
            os.mkdir("files")
        else:
            print("Папка files уже существует")
        
        for name in self.names:
            if not os.path.isdir("files/"+name):
                print("Папка",name,"создана")
                os.mkdir("files/"+name)
            else:
                print("Папка",name,"уже существует")

        ojr = [['Kennedinin', 'əlaqədar'], ['Prezidenti'], ['istinadən']]
        ti = time.time()
        for key in self.dickt.keys():
            if(self.dickt[key] == 2):
                print("[",key,"]",self.dickt[key])
                self.hide()
                if(key == 'qafqazinfo.az'):
                    Qafqazinfo_az.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'azadliq.org'):
                    Azadliq.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'apa.az'):
                    Apa_az.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'azertag.az'):
                    Azertag_az.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'meydan.tv'):
                    Meydan_tv.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'moderator.az'):
                    Moderator.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'modern.az'):
                    Modern.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'report.az'):
                    Report_az.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'trend.az'):
                    Aztrend.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'turan.az'):
                    Turan_az.parsing(data_master_scan_in = ojr, data_time = da)
                if(key == 'yenisabah.az'):
                    Yenisabah.parsing(data_master_scan_in = ojr, data_time = da)
                
                    ######################### МЕДЛЕННЫЕ #############################
                if(key == 'musavat.com'):
                    Musavat.parsing(data_master_scan_in = ojr, data_time = da, process_count = 6)
                    #################################################################
        print(time.time() - ti)
        self.close()
        #shutil.rmtree("files")
        #print("Папка files удалена") 

    def Abzaz(self, state):
        self.dickt["abzas.net"] = state
    def Apa(self, state):
        self.dickt["apa.az"] = state
    def Azadliq(self, state): 
        self.dickt["azadliq.org"] = state
    def Azertag(self, state):
        self.dickt["azertag.az"] = state
    def Meydan(self, state):
        self.dickt["meydan.tv"] = state
    def Moderator(self, state):
        self.dickt["moderator.az"] = state
    def Modern(self, state):
        self.dickt["modern.az"] = state
    def Musavat(self, state):
        self.dickt["musavat.com"] = state
    def Qafqazinfo(self, state):
        self.dickt["qafqazinfo.az"] = state
    def Report(self, state):
        self.dickt["report.az"] = state
    def Trend(self, state):
        self.dickt["trend.az"] = state
    def Turan(self, state):
        self.dickt["turan.az"] = state
    def Yeniavaz(self, state):
        self.dickt["yeniavaz.az"] = state
    def Yenisabah(self, state):
        self.dickt["yenisabah.az"] = state

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    #window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()