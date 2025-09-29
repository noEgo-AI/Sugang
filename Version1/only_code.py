import datetime
import sys
import time
import traceback
import os
import fitz

import pyautogui
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
import re


ppl = 1 # pdf 가져오기 끄기 1, 켜기 0

def like_pattern(value, pattern):
    # SQL 패턴을 정규식으로 변환
    pattern = pattern.replace('%', '.*').replace('_', '.')
    return bool(re.fullmatch(pattern, value))

def select_btn():
    # 1. WebDriverWait을 사용하여 콤보박스(Select 태그) 요소가 페이지에 로드될 때까지 대기
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "srchYr"))
    )

    # 2. Select 객체 생성 (콤보박스 요소를 다루기 위해)
    combo_box = Select(select_element)

    # 3. 콤보박스에서 원하는 값을 선택
    # 방법 1: option의 visible text(화면에 표시되는 텍스트)로 선택하기
    combo_box.select_by_visible_text("2024")

    # 방법 2: option의 value 속성으로 선택하기
    # combo_box.select_by_value("원하는_value")

    # 4. WebDriverWait을 사용하여 버튼 요소가 클릭 가능한 상태가 될 때까지 대기
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=submit]"))
    )

    # 5. 버튼 클릭
    button.click()

def bring_the_data():
    scroll_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "scroll-table"))
    )

    rows = scroll_table.find_elements(By.TAG_NAME, "tr")

    # 행별로 데이터를 추출하여 리스트에 저장
    table_data = []
    for row in rows:
        # 헤더 셀(th)와 일반 데이터 셀(td)을 모두 고려합니다.
        cells = row.find_elements(By.TAG_NAME, "th")
        if not cells:
            cells = row.find_elements(By.TAG_NAME, "td")

        # 각 셀의 텍스트를 가져와 리스트로 저장 (불필요한 공백 제거)
        row_data = [cell.text.strip() for cell in cells]
        if row_data:  # 빈 행은 제외
            table_data.append(row_data)

    # pandas DataFrame 생성
    df = pd.DataFrame(table_data)

    # 만약 첫 번째 행이 컬럼명(헤더)이라면, 이를 컬럼명으로 지정합니다.
    if not df.empty:
        df.columns = df.iloc[0]  # 첫 행을 컬럼명으로 사용
        df = df[1:]  # 헤더 행은 데이터에서 제외

    return df

def fitter_the_df(df):
    f_df = df[~((df["학년"] == "1학년") & (df["학기"] == "2학기"))]
    first_row = f_df.iloc[[0]]
    f_df = pd.concat([first_row, f_df], ignore_index=True)
    return f_df[["교과목명","교과목코드"]]

def site_login():
    driver.get("https://sso.jnu.ac.kr/Idp/Login.aspx")

    Id_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userId"))
    )
    Pw_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userPwd"))
    )
    
    # 본인 id pw로 로그인
    Id_element.send_keys("")
    Pw_element.send_keys("")

    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnLoginButton"))
    )
    btn.click()
    # time.sleep(10)

    driver.get("https://hakstd.jnu.ac.kr/web/Suup/Suup053")


def select_btn_bring(dff):
    driver.get("https://hakstd.jnu.ac.kr/web/Suup/Suup053")
    table_data = []
    for k,i in enumerate(dff.itertuples(index=False)):
        subject_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder_ContentPlaceHolderSub_txtSubj"))
        )

        subject_name.clear()
        subject_name.send_keys(i.교과목명)
        # time.sleep(3)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ContentPlaceHolder_ContentPlaceHolderSub_btnSearch"))
        )
        # 5. 버튼 클릭
        driver.execute_script("arguments[0].click();", button)

        brings = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gvData"))
        )
        rows = brings.find_elements(By.TAG_NAME, "tr")

        # 행별로 데이터를 추출하여 리스트에 저장

        for row in rows:
            # 헤더 셀(th)와 일반 데이터 셀(td)을 모두 고려합니다.
            if k == 0:
                cells = row.find_elements(By.TAG_NAME, "th")

            else:
                cells = row.find_elements(By.TAG_NAME, "td")

            # 각 셀의 텍스트를 가져와 리스트로 저장 (불필요한 공백 제거)
            row_data = [cell.text.strip() for cell in cells]
            # print(row_data)

            if len(row_data) > 1 and row_data[0] == "광주" and like_pattern(row_data[2], f"{i.교과목코드}%"):
                if ppl == 0:
                    auto(cells)
                if row_data:  # 빈 행은 제외
                    table_data.append(row_data)
            if k == 0 and row_data:
                table_data.append(row_data)
    df1 = pd.DataFrame(table_data)

    # 만약 첫 번째 행이 컬럼명(헤더)이라면, 이를 컬럼명으로 지정합니다.
    if not df1.empty:
        df1.columns = df1.iloc[0]  # 첫 행을 컬럼명으로 사용
        df1 = df1[1:]  # 헤더 행은 데이터에서 제외
    return df1

def auto(cells):
    for cell in cells:
        try:
            # 셀 내에 <i> 태그를 찾음
            i_element = cell.find_element(By.TAG_NAME, "a")
            # 원하는 클래스 이름이 i 요소의 class 속성에 포함되어 있는지 확인
            if "Hyperdown" in i_element.get_attribute("id"):
                # 클릭 전에 현재 창 핸들을 저장
                main_window = driver.current_window_handle

                # 버튼 클릭 (새 창이 열림)
                i_element.click()

                # 새 창이 열릴 때까지 대기 (기본 창 핸들 개수보다 커지는지 확인)
                WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

                # 새 창의 핸들을 찾기 (현재 창과 다른 핸들)
                new_window = [handle for handle in driver.window_handles if handle != main_window][0]

                # 새 창으로 전환
                # driver.switch_to.window(new_window)

                # 새 창에서 저장 또는 값을 추출하는 작업 수행
                # 예를 들어, 저장 버튼 클릭 또는 텍스트 추출
                # 아래는 예시로, 새 창에서 특정 요소(ID가 "saveButton"인 버튼)를 클릭하는 코드입니다.
                try:
                    time.sleep(3)
                    target_x = 100
                    target_y = 171

                    # 마우스 커서를 지정한 좌표로 이동 (duration은 이동 시간)
                    pyautogui.moveTo(target_x, target_y, duration=1)

                    # 해당 위치에서 마우스 왼쪽 버튼 클릭
                    pyautogui.click()

                    time.sleep(3)
                except Exception as inner_e:
                    print("새 창에서 작업 수행 중 오류:", inner_e)

                # 필요한 작업 완료 후 새 창을 닫거나, 원래 창으로 전환
                # driver.close()  # 새 창 닫기

                # 원래 창으로 전환
                driver.switch_to.window(main_window)
        except Exception as e:
            # 해당 셀에 <i> 태그가 없거나 조건에 맞지 않으면 pass
            pass


def pdf_location():
    path1 = r"C:\Users\bluem\Downloads"
    files_and_dirs = os.listdir(path1)
    return bring_my_pdf(files_and_dirs)

def bring_my_pdf(f):
    pdfs = list()
    for i in f:
        if i.endswith(".pdf"):
            pdfs.append(i.split(".pdf")[0])
    return pdfs


def open_pdf(f):
    pdf_path = rf"C:\Users\bluem\Downloads\{f}.pdf"  # PDF 파일 경로 지정
    doc = fitz.open(pdf_path)

    page = doc[0]
    page = page.get_text().split("\n")

    keywords = ["선수과목", "Prerequisite(s)"]
    idx = next((page.index(kw) for kw in keywords if kw in page))

    if idx:
        print(page[idx + 1])  # 다음 요소 출력
        if not page[idx + 1] == "교과요목" or page[idx + 1] == "CourseDescription":
            doc.close()
            return page[0].split("(")[0], page[idx + 1]
    doc.close()
    return False

# Edge 드라이버 실행 (실제 msedgedriver.exe 경로로 수정)
# edge_service = EdgeService(executable_path="D:\python\excel\msedgedriver.exe")
# driver = webdriver.Edge(service=edge_service)
driver = webdriver.Edge()
driver.maximize_window()
# 원하는 웹 페이지로 이동
driver.get("https://aisw.jnu.ac.kr/aisw/18201/subview.do")

try:
    select_btn()
    df = bring_the_data()
    df_filtered = fitter_the_df(df)
    # print(df_filtered)

    site_login()
    all_df = select_btn_bring(df_filtered)

    all_df = all_df[(all_df["수업장소"] == "광주")]
    # print(list(df_filtered["교과목명"]))
    # all_df = all_df.where(all_df.isin(df_filtered["교과목명"].tolist()))
    print("="*10)
    cmsize = 0
    pre_subject = dict()
    files = pdf_location()
    # print(files)
    switch = 0
    if switch:
        for f in files:
            if like_pattern(f"{f}",f"report%"):
                o = open_pdf(f)
                print(f)
                if o:
                    if o[1] not in pre_subject.setdefault(o[0], []):
                        pre_subject.setdefault(o[0], []).append(o[1])
                        if cmsize < pre_subject.setdefault(o[0], []).__len__():
                            cmsize = pre_subject.setdefault(o[0], []).__len__()
        print("=" * 10)
    print(pre_subject)
    now = datetime.datetime.now()
    filename = f"renewing_{datetime.datetime.strftime(now, '%Y%m%d%H%M%S')}.xlsx"

    normalized_dict = {key: values + [None] * (cmsize - len(values)) for key, values in pre_subject.items()}
    dict_df = pd.DataFrame(normalized_dict)

    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        all_df.to_excel(writer, sheet_name='Sheet1', index=False)

        for sheet_name, values in pre_subject.items():
            df = pd.DataFrame({sheet_name: values})
            dict_df.to_excel(writer, sheet_name="pre_subject", index=False)  # dict 데이터 시트 저장
    # all_df.to_excel(f"renewing_{datetime.datetime.strftime(now, '%Y%m%d%H%M%S')}.xlsx", index=False)
    # print(f"Excel 파일로 저장되었습니다: renewing_{datetime.datetime.strftime(now, '%Y%m%d%H%M%S')}.xlsx")

    # 필요한 경우, 버튼 클릭 후 추가 작업 수행...

except Exception as e:
    print("오류 발생:", e)
    # traceback.print_exc()

finally:
    driver.quit()
    pass
