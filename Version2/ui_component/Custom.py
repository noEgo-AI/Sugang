# Custom.py
# 인공지능학부 242149 이수용

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import *


class CourseRow(QWidget):
    checked = Signal(list)
    def __init__(self, code, year, major, grade, semester, category, name, credit, status):
        super().__init__()


        self.checkbox = QCheckBox()
        self.checkbox.checkStateChanged.connect(self.on_checked)
        # self.setFixedHeight(40)


        self.throw = [0, name, code]  # ✅ 식별용 코드

        column_widths = {
            # "blanck": 30,
            "code": 100,
            "year": 60,
            "major": 80,
            "grade": 60,
            "semester": 60,
            "category": 80,
            "name": 200,
            "credit": 50,
            "status": 80
        }

        layout = QHBoxLayout()
        widget = QWidget()

        layout.addWidget(CustomQLabel(code, column_widths["code"]))
        layout.addWidget(CustomQLabel(year, column_widths["year"]))
        layout.addWidget(CustomQLabel(major, column_widths["major"]))
        layout.addWidget(CustomQLabel(grade, column_widths["grade"]))
        layout.addWidget(CustomQLabel(semester, column_widths["semester"]))
        layout.addWidget(CustomQLabel(category, column_widths["category"]))
        layout.addWidget(CustomQLabel(name, column_widths["name"]))
        layout.addWidget(CustomQLabel(credit, column_widths["credit"]))
        layout.addWidget(CustomQLabel(status, column_widths["status"]))
        if status == "수강 완료":
            blank = QLabel("      ")
            # blank.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.setStyleSheet("background-color: rgb(255, 102, 102);")
            layout.addWidget(blank)
        elif status == "수강중":
            blank = QLabel("      ")
            # blank.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.setStyleSheet("background-color: rgb(208, 240, 192);")
            layout.addWidget(blank)
        else:
            layout.addWidget(self.checkbox)

        widget.setLayout(layout)
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(widget)
        layout.setContentsMargins(0, 1, 0, 1)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setContentsMargins(9, 0, 9, 0)

    def on_checked(self):
        if self.checkbox.isChecked():
            self.throw[0] = 1
            self.setStyleSheet("background-color: rgb(255, 215, 0);")
            self.checked.emit(self.throw)
        else:
            self.throw[0] = 0
            self.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.checked.emit(self.throw)
    def off_checked(self):
        self.throw[0] = 0
        self.setStyleSheet("background-color: rgb(220, 220, 220);")

class CustomQLabel(QLabel):
    def __init__(self, text, width=100):
        super().__init__()
        wrapped_text = '\u200b'.join(text)  # zero-width space로 글자 사이 줄바꿈 허용
        self.setText(wrapped_text)
        self.setFixedWidth(width)  # 열 너비 고정
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setAlignment(Qt.AlignCenter)  # 선택: 가운데 정렬
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        self.setWordWrap(True)


class ExpectRow(QWidget):
    checked = Signal(list)
    def __init__(self, locate, code, name, manage, credit, professor, time, classroom, memo):
        super().__init__()

        self.name = name
        self.code = code
        self.time = time
        self.credit = credit
        
        self.checkbox = QCheckBox()
        self.checkbox.clicked.connect(self.on_checked)
        # self.setMinimumHeight(80)

        
        
          # ✅ 식별용 코드
        self.setStyleSheet("background-color: rgb(220, 220, 220);")
        column_widths = {
            "수업장소": 50,  # "광주", "여수" → 짧은 텍스트
            "교과목명": 100,  # "JAVA프로그래밍및실습", "공학설계입문" 등 → 중간 길이
            "교과목번호-분반": 90,  # "CIS2004-2", "CLT0894-5" → 고정된 포맷
            "수업운영방식": 80,  # "대면수업", "원격(비대면)수업"
            "학점": 80,  # "3.0(3.0/0.0)" → 숫자 + 괄호 구조
            "담당교수": 50,  # 이름 두세 글자 → 평균 2~3자
            "강의시간": 100,  # "월3월4수3수4" 등 6~8자리 조합
            "강의실": 100,  # "전산-106 전산-106 ..." 중복 길고 반복적
            "비고": 100  # "전산-106", "진리관102" 등 반복 내용
        }

        layout = QHBoxLayout()
        widget = QWidget()

        layout.addWidget(CustomQLabel(locate, column_widths["수업장소"]))
        layout.addWidget(CustomQLabel(code, column_widths["교과목번호-분반"]))
        layout.addWidget(CustomQLabel(name, column_widths["교과목명"]))
        layout.addWidget(CustomQLabel(manage, column_widths["수업운영방식"]))
        layout.addWidget(CustomQLabel(credit, column_widths["학점"]))
        layout.addWidget(CustomQLabel(professor, column_widths["담당교수"]))
        layout.addWidget(CustomQLabel(time, column_widths["강의시간"]))
        layout.addWidget(CustomQLabel(classroom, column_widths["강의실"]))
        layout.addWidget(CustomQLabel(memo, column_widths["비고"]))
        layout.addWidget(QPushButton(text= "수강계획서"))
        layout.addWidget(self.checkbox)

        widget.setLayout(layout)
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(widget)
        layout.setContentsMargins(0, 1, 0, 1)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setContentsMargins(9, 0, 9, 0)

    def on_checked(self):

        if self.checkbox.isChecked():
            self.setStyleSheet("background-color: rgb(255, 215, 0);")
        else:
            self.setStyleSheet("background-color: rgb(220, 220, 220);")

        self.checked.emit([self.checkbox.isChecked(), self.name, self.code, self.time, self.credit.split(".")[0],
                           self])  # 리스트 복사본을 emit


class MyLineEdit(QLineEdit):
    def __init__(self, next_widget=None, button=None):
        super().__init__()
        self.next_widget = next_widget
        self.button = button

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Tab and self.next_widget:
            self.next_widget.setFocus()
            return  # 이건 필요
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter) and self.button:
            self.button.setFocus()
            self.button.click()
            return
        super().keyPressEvent(event)

    # ✅ Qt 내부 Tab 순서를 완전히 막음
    def focusNextPrevChild(self, next: bool) -> bool:
        # Tab을 누르더라도 다음 포커스 위젯으로 이동하지 않음
        return False
