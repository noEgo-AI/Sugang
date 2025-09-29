# 인공지능학부 242149 이수용

import sys
import os
from datetime import datetime, timedelta

from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox

from Version2.ui_component import Custom, UI_portalscreen as UI_portalscreen, UI_mainscreen as UI_mainscreen

import WebThread
import pandas as pd


class Main(QMainWindow, UI_mainscreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.course_color_map = {}
        self.setupUi(self)

        self.worker = worker
        self.worker.result_signal.connect(self.show_log)
        self.worker.start()

        self.showMaximized()

        self.switch = False
        self.change_screen_info()
        self.l10.hide()

        self.current_print = []

        self.total_credit = 0
        self.minus_credit = 0

        self.basic_color = "#F2F2F2"

        self.colors = [
            "#FFB3BA",  # 파스텔 핑크
            "#BAE1FF",  # 연청
            "#FFFFBA",  # 레몬 옐로우
            "#BAFFC9",  # 민트
            "#D5BAFF",  # 라벤더
            "#FFCCE5",  # 라이트 핑크
            "#C7E0FF",  # 베이비 블루
            "#FFD6D6",  # 라이트 살몬
            "#C2F0C2",  # 연녹색
            "#FFF5BA",  # 라이트 옐로우
            "#B8F3FF",  # 스카이블루
            "#E3CFFF",  # 연보라
            "#F5FFC2",  # 라이트 그린옐로우
            "#FFEDBA",  # 크림 오렌지
            "#E0BAFF",  # 중간 톤 보라
            "#FFDEDE",  # 붉은 기운 있는 핑크
            "#B5EAD7",  # 청량한 민트 계열
            "#D6E0FF",  # 은은한 회색빛 하늘
            "#FFF2CC",  # 부드러운 베이지 옐로우
            "#B2EBF2"  # 부드러운 시안 계열
        ]

        # self.lname.setFixedWidth(200)

        self.credit.textChanged.connect(self.change_credit_value)

        self.Button_portal.clicked.connect(self.open_portal_screen)
        self.credit.setValidator(QIntValidator(0,30))  # 정수만 허용됨

        self.l10.setFixedWidth(70)
        self.l10.setText("수강계획서")

        # 기본 데이터 저장하기
        ## 내가 대학 생활 동안 들어야 하는 코스
        self.Button_bring_basic.clicked.connect(self.call_bring_basic)
        self.basic_time = None
        ## 내가 대학 생활 동안 들었던 내용
        self.Button_my_content.clicked.connect(self.call_bring_mine)
        self.past_time = None
        ## 내가 현재 수강 중인 목록
        self.Button_current_content.clicked.connect(self.call_bring_current)
        self.current_time = None
        ## 예상 과목 생성하기
        self.Button_generate.clicked.connect(self.call_bring_expect)
        self.expect_time = None


        # sheet 함수 가져오기
        self.datas_category = []
        self.data_seperator = {"year":set(), "major":set(), "grade":set(), "semester":set()}
        self.datas = None
        self.datas_mine = None
        self.datas_current = None
        self.datas_expect = None

        # 파일 안에 데이터가 있는지 확인
        self.is_exist_excel_file()

        # 검색하기
        self.Button_search.clicked.connect(self.search_basic_info)

        # 선택된 데이터 모음
        self.datas_select = []

        # 화면 스위치 만들기.
        self.Button_switch.clicked.connect(self.change_screen_info)

    # portal ID를 받는 매서드
    @Slot(str)
    def show_log(self, result):
        sorting_code, output = result[:5], result[6:]
        if sorting_code == "FMDL0":
            self.past_time = None

        if sorting_code == "LIS00":
            win.show()
            win.raise_()
            win.activateWindow()
            win.setFocus()
            win1.hide()
            win1.login_time = None
        if sorting_code == "LIF00":
            win1.raise_()
            win1.activateWindow()
            win1.setFocus()
            win1.login_time = None

        if sorting_code == "SWE00":
            win1.raise_()
            win1.activateWindow()
            win1.setFocus()
            win1.login_time = None

        if sorting_code == "SMDL0":
            win.raise_()
            win.activateWindow()
            win.setFocus()
            self.past_time = None
            self.Button_my_content.setStyleSheet("""
                                                        background-color: rgb(255,255,255);
                                                        color: black;
                                                        font-weight: bold;
                                                        border-radius: 6px;
                                                    """)
            # if not self.datas_category:
            #     self.is_exist_excel_file()


        if sorting_code == "FMCDL":
            self.current_time = None

        if sorting_code == "SMCDL":
            win.raise_()
            win.activateWindow()
            win.setFocus()
            self.current_time = None
            self.Button_current_content.setStyleSheet("""
                                                        background-color: rgb(255,255,255);
                                                        color: black;
                                                        font-weight: bold;
                                                        border-radius: 6px;
                                                    """)
        if sorting_code == "SBDL0":
            win.raise_()
            win.activateWindow()
            win.setFocus()
            self.basic_time = None
            self.Button_current_content.setStyleSheet("""
                                                        background-color: rgb(255,255,255);
                                                        color: black;
                                                        font-weight: bold;
                                                        border-radius: 6px;
                                                    """)

        if sorting_code == "FBDL0":
            self.basic_time = None

        if sorting_code == "FBEDL":
            self.expect_time = None

        if sorting_code == "SBEDL":
            win.raise_()
            win.activateWindow()
            win.setFocus()
            self.expect_time = None
            self.Button_generate.setStyleSheet("""
                                                    background-color: rgb(255,255,255);
                                                    color: black;
                                                    font-weight: bold;
                                                    border-radius: 6px;
                                                """)
        self.print_log(f"{sorting_code} {output}")

    # 로그인 화면 윈도위 출력
    @staticmethod
    def open_portal_screen():
        win1.show()

    # 기초 call
    def call_bring_basic(self):
        now = datetime.now()

        if self.basic_time is not None:
            self.print_log("[알림] 이미 요청되었습니다. 실행이 끝난 후 다시 실행해주세요.")
            return

        self.basic_time = now

        self.worker.resend("PCSS0 [진행] 기초 내역 가져오는 중")
        self.worker.submit(self.worker.crawler.basic_load)

    # 수강완료 call
    def call_bring_mine(self):
        now = datetime.now()

        if self.past_time is not None:
            self.print_log("[알림] 이미 요청되었습니다. 실행이 끝난 후 다시 실행해주세요.")
            return

        self.past_time = now

        self.worker.resend("PCSS0 [진행] 내가 수강했던 내용 가져오는 중")
        self.worker.submit(self.worker.crawler.bring_my_complete_data)

    # 수강 중 call
    def call_bring_current(self):
        now = datetime.now()

        if self.current_time is not None:
            self.print_log("[알림] 이미 요청되었습니다. 실행이 끝난 후 다시 실행해주세요.")
            return

        self.current_time = now

        self.worker.resend("PCSS0 [진행] 내가 수강 중인 내용 가져오는 중")
        self.worker.submit(self.worker.crawler.bring_my_current_data)

    # 파일이 있나요?
    def is_exist_excel_file(self):
        self.print_log(f"[진행] 엑셀 파일에서 데이터를 불러오는 중.")
        try:
            self.print_log(f"[진행] 기초 수강 내역 가져오는 중..")
            self.datas = None

            excel_files = pd.ExcelFile(rf"{excel_location}\basic.xlsx")

            self.datas_category = excel_files.sheet_names
            self.data_seperator["grade"].add("전체")
            self.data_seperator["major"].add("전체")
            for i in self.datas_category:
                temp = [i[:4], i[5:]]
                self.data_seperator["year"].add(temp[0])
                self.data_seperator["major"].add(temp[1])

                df = pd.read_excel(rf"{excel_location}\basic.xlsx", sheet_name=i)
                df["year"] = temp[0]
                df["major"] = temp[1]
                df.columns = df.columns.str.strip()
                self.datas = pd.concat([self.datas, df], ignore_index=True)

            self.data_seperator["grade"].add("1학년")
            self.data_seperator["grade"].add("2학년")
            self.data_seperator["grade"].add("3학년")
            self.data_seperator["grade"].add("4학년")

            if self.cb_year.count() <= 0:
                self.cb_year.addItems(sorted(self.data_seperator["year"], reverse=True))
                self.cb_major.addItems(sorted(self.data_seperator["major"]))
                self.cb_grade.addItems(sorted(self.data_seperator["grade"]))
                self.cb_gyear.addItems(sorted(self.data_seperator["year"], reverse=True))
                with open(rf"{excel_location}\semester.csv", "r", encoding="utf-8") as f:
                    p = f.read().splitlines()
                    for i in p:
                        self.cb_semester.addItem(i)


        except Exception as e:
            self.print_log(f"[오류] '기초 수강 가져오기' 버튼을 누르세요.\n{e}")
            self.Button_bring_basic.setStyleSheet("""
                                                    background-color: #2A9D8F;
                                                    color: black;
                                                    font-weight: bold;
                                                    border-radius: 6px;
                                                """)

        try:
            self.print_log(f"[진행] 내 수강 했던 내역을 가져 오는 중..")
            df = pd.read_excel(rf"{excel_location}\mydata.xlsx")
            df = df[["교과목번호"]].dropna()
            self.datas_mine = df

        except Exception as e:
            self.print_log(f"[오류] '내 수강 내역 가져오기' 버튼을 누르세요.\n{e}")
            self.Button_my_content.setStyleSheet("""
                                                    background-color: #2A9D8F;
                                                    color: black;
                                                    font-weight: bold;
                                                    border-radius: 6px;
                                                """)

        try:
            self.print_log(f"[진행] 내가 현재 수강 하고 있는 내역을 가져 오는 중..")
            df = pd.read_excel(rf"{excel_location}\mycurrentdata.xlsx")
            df = df[["교과목번호"]].dropna()

            df["교과목번호"] = df["교과목번호"].str.split("-").str[0]
            self.datas_current = df

        except Exception as e:
            self.print_log(f"[오류] '내 현재 수강 가져오기' 버튼을 누르세요.\n{e}")
            self.Button_current_content.setStyleSheet("""
                                                        background-color: #2A9D8F;
                                                        color: black;
                                                        font-weight: bold;
                                                        border-radius: 6px;
                                                    """)

        try:
            self.print_log(f"[진행] 내가 다음 학기에 수강 해야 할 목록을 가져 오는 중..")
            self.datas_expect = None

            df = pd.read_excel(rf"{excel_location}\expected.xlsx")

            self.datas_expect = pd.concat([self.datas_expect, df], ignore_index=True)

        except Exception as e:
            self.print_log(f"[오류] '생성 하기' 버튼을 누르세요.\n{e}")
            self.Button_generate.setStyleSheet("""
                                                background-color: #F4B183;
                                                color: black;
                                                font-weight: bold;
                                                border-radius: 6px;
                                            """)

    # 안에 값 초기화
    def clear_scroll_area(self):
        # scrollArea 안에 현재 설정된 위젯 가져오기
        container = self.scrollArea.widget()

        if container is not None:
            layout = container.layout()
            if layout is not None:
                # 레이아웃 안의 모든 위젯 제거
                while layout.count():
                    child = layout.takeAt(0)
                    widget = child.widget()
                    if widget is not None:
                        widget.deleteLater()  # 안전하게 메모리 해제

    # 검색 화면
    def search_basic_info(self):
        if self.basic_time is not None or self.current_time is not None or self.past_time is not None:
            self.print_log("[알림] 기초 자료를 수집 중 입니다. 수집을 완료한 뒤 다시 눌러 주세요.")
            return

        self.is_exist_excel_file()
        self.clear_scroll_area()
        container = QWidget()

        self.course_color_map = {}  # 색 초기화

        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        if self.switch:
            try:
                data = self.datas[(self.datas["year"]==self.cb_year.currentText()) &
                                  ((self.datas["major"]==self.cb_major.currentText()) if self.cb_major.currentText() != "전체" else (self.datas["major"]!=self.cb_major.currentText())) &
                                  ((self.datas["학년"]==self.cb_grade.currentText()) if self.cb_grade.currentText() != "전체" else (self.datas["학년"]!=self.cb_grade.currentText())) &
                                  ((self.datas["교과목명"].str.contains(self.textEdit_search.toPlainText(), na=False)) if self.textEdit_search.toPlainText() else True)]

                for _, row in data.iterrows():
                    is_selected = [str(row["교과목명"]), str(row["교과목코드"])] in self.datas_select

                    if str(row["교과목코드"]) in self.datas_current.values:
                        status = "수강중"
                    elif str(row["교과목코드"]) in self.datas_mine.values:
                        status = "수강 완료"
                    else:
                        status = "미수강"
                    course_row = Custom.CourseRow(
                        code=str(row["교과목코드"]),
                        grade=str(row["학년"]),
                        major=str(row["major"]),
                        year=str(row["year"]),
                        semester=str(row["학기"]),
                        category=str(row["과목구분"]),
                        name=str(row["교과목명"]),
                        credit=str(row["학점"]),  # ✅ float → str
                        status= status
                    )
                    if is_selected:
                        course_row.checkbox.setChecked(True)  # ✅ 체크 상태 복원

                    course_row.checked.connect(self.control_select_datas)
                    vbox.addWidget(course_row)

                vbox.setSpacing(0)
                vbox.setContentsMargins(0, 0, 0, 0)
                container.setLayout(vbox)
                container.setContentsMargins(0,0,0,0)

                self.scrollArea.setWidget(container)

                self.scrollArea.setWidgetResizable(True)
                content_width = self.scrollArea.widget().sizeHint().width()+ self.scrollArea.verticalScrollBar().sizeHint().width()+ 10
                self.scrollArea.setMinimumWidth(content_width)
                self.scrollArea.resize(content_width, self.scrollArea.height())
                parent_widget = self.scrollArea.parentWidget()
                parent_widget.setMinimumWidth(content_width + 10)
                parent_widget.resize(content_width + 10, parent_widget.height())
                self.print_log("[성공] 데이터 로드 성공 했습니다.")

            except Exception as e:
                self.print_log(f"[실패] 내 수강 내역 및 기초 수강 버튼으로 먼저 눌러 주세요.\n{e}")
        else:
            try:
                if self.textEdit_search.toPlainText():
                    data = self.datas_expect[
                        self.datas_expect["교과목명"].str.contains(self.textEdit_search.toPlainText(), na=False)
                    ]
                else:
                    data = self.datas_expect

                for _, row in data.iterrows():
                    is_selected = str(row["교과목번호-분반"]) in {p for i in self.datas_select for p in i }
                    expect_row = Custom.ExpectRow(
                        locate=str(row["수업장소"]),
                        code=str(row["교과목번호-분반"]),
                        name=str(row["교과목명"]),
                        manage=str(row["수업운영방식"]),
                        credit=str(row["학점"]),
                        professor=str(row["담당교수"]),
                        time=str(row["강의시간"]),
                        classroom=str(row["강의실"]),
                        memo=str(row["비고"])
                    )

                    expect_row.checked.connect(self.control_select_datas)
                    if is_selected:
                        expect_row.checkbox.setChecked(True)
                        expect_row.checkbox.click()
                        expect_row.checkbox.click()

                    vbox.addWidget(expect_row)

                vbox.setSpacing(0)
                vbox.setContentsMargins(0, 0, 0, 0)
                container.setLayout(vbox)
                container.setContentsMargins(0, 0, 0, 0)

                self.scrollArea.setWidget(container)

                self.scrollArea.setWidgetResizable(True)
                content_width = self.scrollArea.widget().sizeHint().width() + self.scrollArea.verticalScrollBar().sizeHint().width() + 10
                self.scrollArea.setMinimumWidth(content_width)
                self.scrollArea.resize(content_width, self.scrollArea.height())
                parent_widget = self.scrollArea.parentWidget()
                parent_widget.setMinimumWidth(content_width + 10)
                parent_widget.resize(content_width + 10, parent_widget.height())

                self.print_log("[성공] 데이터 로드 성공 했습니다.")
            except Exception as e:
                self.print_log(f"[실패] 내 수강 내역 및 기초 수강 버튼으로 먼저 눌러 주세요.\n{e}")
            # 여기에 두번째 화면

    # 체크 1 화면
    def control_select_datas(self, selected):
        if self.switch:
            if selected[0] == 0:
                self.datas_select.remove(selected[1:])
            else:
                self.datas_select.append(selected[1:])
        else:
            if not selected[0]:
                try:
                    self.minus_credit -= int(selected[4])
                    self.change_value()
                    self.datas_select.remove(selected[1:-1])
                    self.print_calendar(selected[2],selected[3], True, selected[-1])
                except ValueError as e:
                    self.print_log(f"[오류] 예상치 못한 오류가 발생했습니다.\n{e}")

            else:
                self.minus_credit += int(selected[4])
                self.change_value()
                k = self.print_calendar(selected[2], selected[3], False, selected[-1])
                if k == 1: return
                self.datas_select.append(selected[1:-1])


    def change_value(self):
        k = self.total_credit - self.minus_credit
        if k < 0:
            self.lb_credit.setStyleSheet("background-color: red")
            self.print_log("[오류] 학점이 초과됩니다. 학점을 확인하세요.")
        else:
            self.lb_credit.setStyleSheet("background-color: green")
        self.lb_credit.setText(str(self.total_credit - self.minus_credit))


    # 예상 과목 가져오기
    def call_bring_expect(self):
        now = datetime.now()

        if len(self.datas_select) <= 0:
            self.print_log("[알림] 선택한 데이터가 없어 생성이 불가능 합니다.")
            return

        if self.basic_time is not None or self.current_time is not None or self.past_time is not None:
            self.print_log("[알림] 기초 자료를 수집 중 입니다. 수집을 완료한 뒤 다시 눌러 주세요.")
            return

        if self.expect_time is not None:
            self.print_log("[알림] 이미 요청되었습니다. 실행이 끝난 후 다시 실행해주세요.")
            return

        self.expect_time = now

        self.worker.resend("PCSS0 [진행] 내가 원하는 수강 내용 가져오는 중")
        self.worker.submit(
            self.worker.crawler.get_expected_courses,
            self.cb_gyear.currentText(),
            self.cb_semester.currentText(),
            self.datas_select
        )

    def change_screen_info(self):
        self.switch = not self.switch
        self.clear_scroll_area()
        self.datas_select = []
        if self.switch:
            self.widget_hide1.show()
            self.widget_4.setStyleSheet("background-color:rgb(173, 216, 230);")

            self.w_hide1.show()
            self.w_hide2.hide()


            self.l1.setFixedWidth(100)
            self.l1.setText("과목코드")
            self.l2.setFixedWidth(60)
            self.l2.setText("입학년도")
            self.l3.setFixedWidth(80)
            self.l3.setText("전공")
            self.l4.setFixedWidth(60)
            self.l4.setText("학년")
            self.l5.setFixedWidth(60)
            self.l5.setText("학기")
            self.l6.setFixedWidth(80)
            self.l6.setText("교과구분")
            self.l7.setFixedWidth(200)
            self.l7.setText("교과목명")
            self.l8.setFixedWidth(50)
            self.l8.setText("학점")
            self.l9.setFixedWidth(80)
            self.l9.setText("수강여부")
            self.l10.hide()
        else:
            self.widget_hide1.hide()
            # self.widget_hide2.hide()
            self.widget_4.setStyleSheet("background-color:rgb(210, 180, 230)")

            self.w_hide2.show()
            self.w_hide1.hide()


            self.l1.setFixedWidth(50)
            self.l1.setText("수업장소")
            self.l2.setFixedWidth(90)
            self.l2.setText("교과목번호-분반")
            self.l3.setFixedWidth(100)
            self.l3.setText("교과목명")
            self.l4.setFixedWidth(80)
            self.l4.setText("수업운영방식")
            self.l5.setFixedWidth(80)
            self.l5.setText("학점")
            self.l6.setFixedWidth(50)
            self.l6.setText("담당교수")
            self.l7.setFixedWidth(100)
            self.l7.setText("강의시간")
            self.l8.setFixedWidth(100)
            self.l8.setText("강의실")
            self.l9.setFixedWidth(100)
            self.l9.setText("비고")
            self.l10.show()

    def change_credit_value(self):
        self.total_credit = int(self.credit.text())
        self.change_value()

    def print_calendar(self, code, times, s, checkbox):
        t = [times[i*2:i*2+2] for i in range(len(times)//2)]

        if s:
            self.current_print.remove(t)
            self.real_print(t, s, code.split("-")[0])
        else:
            flat_total = {item for sublist in self.current_print for item in sublist}
            code_total = {sublist[1].split("-")[0] for sublist in self.datas_select}
            if code.split("-")[0] in code_total:
                checkbox.checkbox.click()
                QMessageBox.warning(self, "과목 중복 경고", "이미 동일한 과목을 선택하였습니다.")
                return 1

            if any(x in flat_total for x in t):
                checkbox.checkbox.click()
                QMessageBox.warning(self, "시간 중복 경고", "이미 선택된 과목과 시간표가 겹칩니다.")
                return 1

            self.current_print.append(t)
            self.real_print(t, s, code.split("-")[0])

    def real_print(self, p, s, course_code=None):
        if s:
            text = f"background-color:{self.basic_color}"
        else:
            # ✅ 과목마다 고유한 색 매핑
            if course_code not in self.course_color_map:
                color_index = len(self.course_color_map) % len(self.colors)
                self.course_color_map[course_code] = self.colors[color_index]
            text = f"background-color:{self.course_color_map[course_code]}"
        for i in p:
            if i == "월1":
                self.m1t.setStyleSheet(text)
                self.m1b.setStyleSheet(text)
            elif i == "월2":
                self.m2t.setStyleSheet(text)
                self.m2b.setStyleSheet(text)
            elif i == "월3":
                self.m3b.setStyleSheet(text)
                self.m3t.setStyleSheet(text)
            elif i == "월4":
                self.m4b.setStyleSheet(text)
                self.m4t.setStyleSheet(text)
            elif i == "월5":
                self.m5t.setStyleSheet(text)
                self.m5b.setStyleSheet(text)
            elif i == "월6":
                self.m6b.setStyleSheet(text)
                self.m6t.setStyleSheet(text)
            elif i == "월7":
                self.m7b.setStyleSheet(text)
                self.m7t.setStyleSheet(text)
            elif i == "월8":
                self.m8b.setStyleSheet(text)
                self.m8t.setStyleSheet(text)
            elif i == "월9":
                self.m9b.setStyleSheet(text)
                self.m9t.setStyleSheet(text)
            elif i == "월10":
                self.m10b.setStyleSheet(text)
                self.m10t.setStyleSheet(text)
            elif i == "화1":
                self.tu1t.setStyleSheet(text)
                self.tu1b.setStyleSheet(text)
                self.tu1m.setStyleSheet(text)
            elif i == "화2":
                self.tu2t.setStyleSheet(text)
                self.tu2b.setStyleSheet(text)
                self.tu2m.setStyleSheet(text)
            elif i =="화3":
                self.tu3t.setStyleSheet(text)
                self.tu3m.setStyleSheet(text)
                self.tu3b.setStyleSheet(text)
            elif i == "화4":
                self.tu4t.setStyleSheet(text)
                self.tu4b.setStyleSheet(text)
                self.tu4m.setStyleSheet(text)
            elif i == "화5":
                self.tu5b.setStyleSheet(text)
                self.tu5t.setStyleSheet(text)
                self.tu5m.setStyleSheet(text)
            elif i == "화6":
                self.tu6t.setStyleSheet(text)
                self.tu6m.setStyleSheet(text)
                self.tu6b.setStyleSheet(text)
            elif i == "화7":
                self.tu7m.setStyleSheet(text)
                self.tu7t.setStyleSheet(text)
            elif i == "수1":
                self.w1t.setStyleSheet(text)
                self.w1b.setStyleSheet(text)
            elif i == "수2":
                self.w2t.setStyleSheet(text)
                self.w2b.setStyleSheet(text)
            elif i == "수3":
                self.w3b.setStyleSheet(text)
                self.w3t.setStyleSheet(text)
            elif i == "수4":
                self.w4b.setStyleSheet(text)
                self.w4t.setStyleSheet(text)
            elif i == "수5":
                self.w5t.setStyleSheet(text)
                self.w5b.setStyleSheet(text)
            elif i == "수6":
                self.w6b.setStyleSheet(text)
                self.w6t.setStyleSheet(text)
            elif i == "수7":
                self.w7b.setStyleSheet(text)
                self.w7t.setStyleSheet(text)
            elif i == "수8":
                self.w8b.setStyleSheet(text)
                self.w8t.setStyleSheet(text)
            elif i == "수9":
                self.w9b.setStyleSheet(text)
                self.w9t.setStyleSheet(text)
            elif i == "수10":
                self.w10b.setStyleSheet(text)
                self.w10t.setStyleSheet(text)
            elif i == "목1":
                self.th1t.setStyleSheet(text)
                self.th1b.setStyleSheet(text)
                self.th1m.setStyleSheet(text)
            elif i == "목2":
                self.th2t.setStyleSheet(text)
                self.th2b.setStyleSheet(text)
                self.th2m.setStyleSheet(text)
            elif i =="목3":
                self.th3t.setStyleSheet(text)
                self.th3m.setStyleSheet(text)
                self.th3b.setStyleSheet(text)
            elif i == "목4":
                self.th4t.setStyleSheet(text)
                self.th4b.setStyleSheet(text)
                self.th4m.setStyleSheet(text)
            elif i == "목5":
                self.th5b.setStyleSheet(text)
                self.th5t.setStyleSheet(text)
                self.th5m.setStyleSheet(text)
            elif i == "목6":
                self.th6t.setStyleSheet(text)
                self.th6m.setStyleSheet(text)
                self.th6b.setStyleSheet(text)
            elif i == "목7":
                self.th7m.setStyleSheet(text)
                self.th7t.setStyleSheet(text)
            elif i == "금1":
                self.f1t.setStyleSheet(text)
                self.f1b.setStyleSheet(text)
            elif i == "금2":
                self.f2t.setStyleSheet(text)
                self.f2b.setStyleSheet(text)
            elif i == "금3":
                self.f3b.setStyleSheet(text)
                self.f3t.setStyleSheet(text)
            elif i == "금4":
                self.f4b.setStyleSheet(text)
                self.f4t.setStyleSheet(text)
            elif i == "금5":
                self.f5t.setStyleSheet(text)
                self.f5b.setStyleSheet(text)
            elif i == "금6":
                self.f6b.setStyleSheet(text)
                self.f6t.setStyleSheet(text)
            elif i == "금7":
                self.f7b.setStyleSheet(text)
                self.f7t.setStyleSheet(text)
            elif i == "금8":
                self.f8b.setStyleSheet(text)
                self.f8t.setStyleSheet(text)
            elif i == "금9":
                self.f9b.setStyleSheet(text)
                self.f9t.setStyleSheet(text)
            elif i == "금10":
                self.f10b.setStyleSheet(text)
                self.f10t.setStyleSheet(text)

    def print_log(self, text):
        now = datetime.now()
        self.logedit.setPlainText(f"[{now.hour}:{now.minute}:{now.second}] {text}\n{self.logedit.toPlainText()}")

class Portal(QMainWindow, UI_portalscreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = worker

        self.login_time = None
        # 포털 아이디 pw 받기
        self.portalID = ""
        self.portalPW = ""

        self.lineEditPW.next_widget = self.lineEditID
        self.lineEditID.next_widget = self.lineEditPW
        self.lineEditPW.button = self.Button_login
        self.lineEditID.button = self.Button_login

        self.lineEditPW.setEchoMode(self.lineEditPW.EchoMode.Password)

        self.lineEditID.textChanged.connect(self.id_changed)
        self.lineEditPW.textChanged.connect(self.pw_changed)
        self.Button_login.clicked.connect(self.login)

    def id_changed(self):
        # QTextEdit에서 현재 텍스트 추출
        self.portalID = self.lineEditID.text()

    # portal PW를 받는 매서드
    def pw_changed(self):
        self.portalPW = self.lineEditPW.text()
    # 전남대학교 포털로 로그인 하는 매서드
    def login(self):
        now = datetime.now()

        if self.login_time is not None and (now - self.login_time < timedelta(seconds=30)):
            self.worker.resend("ALRET [알림] 이미 요청되었습니다. 30초 후에 다시 시도해 주세요.")
            return

        self.login_time = now

        self.worker.resend(f"PCSS0 [진행] 로그인 시도 중...")
        self.worker.submit(self.worker.crawler.login,self.portalID, self.portalPW)

def get_documents_path():
    return os.path.join(os.path.expanduser("~"), "Documents", "SuGang")

def load_location():
    base_path = get_documents_path()

    # 폴더가 없으면 생성
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(rf"{base_path}\excel", exist_ok=True)
    os.makedirs(rf"{base_path}\syllabus", exist_ok=True)



if __name__ == "__main__":
    load_location()
    excel_location = rf"{get_documents_path()}\excel"
    syllabus_location = rf"{get_documents_path()}\syllabus"

    # crawling = webcrawling.Crawling()
    worker = WebThread.AsyncWorkerThread()
    worker.crawler.excel_save_location = excel_location
    worker.crawler.syllabus_save_location = syllabus_location
    # asyncio.run(webcrawling.main())
    # crawling.excel_save_location = excel_location
    # crawling.syllabus_save_location = syllabus_location

    app = QApplication(sys.argv)
    win = Main()
    win1 = Portal()
    win.hide()

    win1.show()
    app.exec()