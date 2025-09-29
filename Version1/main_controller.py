from datetime import datetime

import os
import UI_initial_form
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import threading
import requests
import time
import sys

def major_seletor():

    # edge_service = EdgeService(EdgeChromiumDriverManager().install())
    # driver = webdriver.Edge(service=edge_service)

    # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver = webdriver.Edge()

    url = "https://aisw.jnu.ac.kr/aisw/18201/subview.do"
    url1 = "https://hakstd.jnu.ac.kr/web/Suup/Suup053"
    driver.get(url)
    try:
        # 3. 요소가 로드될 때까지 최대 10초간 대기 (id가 "target-element"인 요소)
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "tab_k2wiz_GNB_16844"))
            # tab_k2wiz_GNB_18201 a_3 k2wiz_GNB_512 _active 인공지능
            # tab_k2wiz_GNB_16844 a_3 k2wiz_GNB_512 인공지능전공
            # tab_k2wiz_GNB_16845 a_3 k2wiz_GNB_512 소프트웨어전공
            # tab_k2wiz_GNB_20137 a_3 k2wiz_GNB_512 정보보안전공
        )

        # 4. 요소의 텍스트 값 가져오기
        value = element.text
        print("가져온 값:", value)

        # 만약, 요소가 input 태그라면 속성 'value'를 가져올 수 있습니다.
        # value = element.get_attribute("value")

    except Exception as e:
        print("오류 발생:", e)

    finally:
        # 5. 브라우저 종료
        driver.quit()


    return None

count = 0
print(3)

hello = "hello 입니다."
pri_info = []


def msgbox(title, detail):
    box = QMessageBox()
    box.setWindowTitle("알림창")
    box.setText(title)
    box.setInformativeText(detail)
    box.addButton("확인", QMessageBox.ButtonRole.YesRole)
    return box.exec()


# 로그인 화면
class inital(QMainWindow, UI_initial_form.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("basic setting")

        self.setFixedWidth(453)
        self.setFixedHeight(241)

        self.year_cmbo.setFixedHeight(45)

        current_year = datetime.now().year
        major_seletor()

        for year in range(current_year-20, current_year + 1):
            self.year_cmbo.addItem(str(year))

        sys.exit()

    def only_tab(self):
        pass


app = QApplication()
window = inital()
window.show()
app.exec()
sys.exit()
