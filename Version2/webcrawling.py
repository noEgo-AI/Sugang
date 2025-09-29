# 인공지능학부 242149 이수용

import os
import platform
import shutil
from urllib.parse import urljoin
from playwright.async_api import async_playwright, Browser, Page, TimeoutError
import pandas as pd

def get_browser_path():
    """운영체제별 Chromium 브라우저 경로 자동 감지"""
    system = platform.system().lower()

    if system == "windows":
        # Playwright가 설치하는 Chromium 경로
        chromium_path = os.path.join(os.getcwd(), "ms-playwright", "chromium")

        possible_paths = [
            os.path.join(chromium_path, "chrome.exe"),
            os.path.join(chromium_path, "chromium.exe"),
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        # 사용자별 Chrome 경로
        username = os.getenv("USERNAME")
        if username:
            possible_paths.append(
                rf"C:\Users\{username}\AppData\Local\Google\Chrome\Application\chrome.exe"
            )

    elif system == "darwin":  # macOS
        chromium_path = os.path.join(os.getcwd(), "ms-playwright", "chromium")
        possible_paths = [
            os.path.join(chromium_path, "Chromium.app", "Contents", "MacOS", "Chromium"),
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]

    else:  # Linux
        chromium_path = os.path.join(os.getcwd(), "ms-playwright", "chromium")
        possible_paths = [
            os.path.join(chromium_path, "chromium"),
            os.path.join(chromium_path, "chrome"),
        ]

        # 시스템 경로에서 찾기
        system_commands = ["chromium", "chromium-browser", "google-chrome", "chrome"]
        for cmd in system_commands:
            path = shutil.which(cmd)
            if path:
                possible_paths.append(path)

    # 첫 번째로 존재하는 경로 반환
    for path in possible_paths:
        if os.path.exists(path):
            return path

    # 기본값 (이전 하드코딩된 경로)
    return os.path.abspath("ms-playwright/chromium/chrome.exe")

BROWSER_PATH = get_browser_path()

class Crawling:
    # 생성자
    def __init__(self):
        self.portal_id = None
        self.portal_pw = None
        self.playwright : async_playwright = None
        self.browser: Browser | None = None
        self.page: Page | None = None


        self.base_data = list()
        self.excel_save_location = None
        self.syllabus_save_location = None

    # 크롤링 준비를 위한 함수
    async def setup(self):
        try:
            # 페이지가 살아있고, 브라우저도 열린 상태인지 확인
            if self.page is None or self.page.is_closed():
                raise RuntimeError("페이지가 닫힘")
        except RuntimeError:
            # 브라우저 또는 페이지가 닫혔을 경우 새로 실행
            if self.playwright is None:
                self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=False, executable_path=BROWSER_PATH)
            self.page = await self.browser.new_page()


    # 내가 수강했던 내용을 가져오는 매서드
    async def bring_my_complete_data(self):
        await self.setup()
        new_page = await self.browser.new_page()
        await self.login(self.portal_id, self.portal_pw, new_page)
        await self.page.close()
        try:
            await self.page.close()
            await new_page.goto("https://hakstd.jnu.ac.kr/web/Sung/Sung010")

            await new_page.wait_for_selector('div.search-wrap.mar_t10', timeout=5000)
            await new_page.click("input[type=submit]")
            # WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, "ContentPlaceHolder_ContentPlaceHolderSub_ibtnSearch"))).click()

            await self.bring_data('#ContentPlaceHolder_ContentPlaceHolderSub_gvData', "mydata", "mycontent", new_page)
            await new_page.close()

            return f"SMDL0 [성공] 내가 수강 했던 데이터를 추출 했습니다."
        except Exception as e:
            await new_page.close()
            return f"FMDL0 [실패] 포털 로그인 버튼을 눌러 포털 로그인을 시도해 주세요.\n{e}"

    # 현재 수강 중인 데이터 가져오기
    async def bring_my_current_data(self):
        await self.setup()
        new_page = await self.browser.new_page()
        await self.login(self.portal_id, self.portal_pw, new_page)
        await self.page.close()
        try:
            await self.page.close()
            await new_page.goto("https://hakstd.jnu.ac.kr/web/Suup/Suup053")
            semester = await new_page.wait_for_selector('#ContentPlaceHolder_ContentPlaceHolderSub_ddlTerm', timeout=5000)
            options = await semester.query_selector_all('option')
            # options = (await semester.query_selector('option')).

            with open(rf"{self.excel_save_location}\semester.csv", "w", encoding="utf-8") as f:
                for option in options:
                    t = await option.inner_text()
                    if t != "선택하세요":
                        f.write(f"{t}\n")

            await new_page.goto("https://hakstd.jnu.ac.kr/web/Suup/Suup080")
            await new_page.wait_for_selector('div.top-tit', timeout=5000)
            # WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, "ContentPlaceHolder_ContentPlaceHolderSub_ibtnSearch"))).click()

            await self.bring_data('#ContentPlaceHolder_ContentPlaceHolderSub_gvData', "mycurrentdata", "mycontent", new_page)
            await new_page.close()
            return f"SMCDL [성공] 수강 중인 데이터를 추출 했습니다."
        except Exception as e:
            await new_page.close()
            return f"FMCDL [실패] 포털 로그인 버튼을 눌러 포털 로그인을 시도해 주세요.\n{e}"

    # 전공을 가져와서 dict 형태로 저장하는 함수
    async def basic_load(self):
        await self.setup()
        new_page = await self.browser.new_page()
        await self.page.close()
        try:
            await self.page.close()
            await new_page.goto("https://aisw.jnu.ac.kr/aisw/18201/subview.do")

            major_element = await new_page.wait_for_selector("ul.tab_k2wiz_GNB._wizOdr.ul_3", timeout = 10000)
            a_elements = await major_element.query_selector_all("a")
            years = await self.select_year(new_page)

            # text 값 가져오기
            for a in a_elements:
                text = await a.inner_text()
                href = await a.get_attribute("href")
                self.base_data.append({"text" : text, "href" : urljoin(new_page.url, href), "year" : years})

            for data in self.base_data:
                await new_page.goto(data["href"])
                for year in data["year"]:
                    await self.select_year(new_page,f"{year} {data['text']}")
            await new_page.close()
            return f"SBDL0 [성공] 기초 데이터 로드에 성공했습니다."
        except Exception:
            await new_page.close()
            return "FBDL0 [오류] 기초 데이터 수집 도중 문제가 발생했습니다.\n다시 작업해주세요."

    # 각 전공마다 select해서 데이터를 긁어 오는 함수
    async def select_year(self,page, switch = ""):
        year = []
        select_element = await page.wait_for_selector("#srchYr")

        if not switch:
            value_elements = await select_element.query_selector_all("option")

            for v in value_elements:
                year.append((await v.inner_text()).strip())

            return year
        else:
            # 2. Select 객체 생성 (콤보박스 요소를 다루기 위해)

            await page.wait_for_selector("#srchYr")
            await select_element.select_option(value=switch.split(" ")[0])
            submit_button = await page.wait_for_selector("input[type=submit]", state="attached")
            await submit_button.click()
            await self.bring_data('div[class="scroll-table"]', "basic", switch, page)

        return

    # 실제 table 데이터를 긁어서 엑셀 형태로 저장하는 함수
    async def bring_data(self,classname, filename, sheetname, page):
        for attempt in range(3):
            try:
                await page.wait_for_selector(classname)

                scroll_table = await page.query_selector(classname)
                rows = await scroll_table.query_selector_all("tr")

                # 행별로 데이터를 추출하여 리스트에 저장
                table_data = []
                for row in rows:
                    # 헤더 셀(th)와 일반 데이터 셀(td)을 모두 고려합니다.
                    cells = await row.query_selector_all("th")
                    if not cells:
                        cells = await row.query_selector_all("td")

                    # 각 셀의 텍스트를 가져와 리스트로 저장 (불필요한 공백 제거)
                    row_data = [(await cell.inner_text()).strip() for cell in cells]
                    if row_data:  # 빈 행은 제외
                        table_data.append(row_data)

                # pandas DataFrame 생성
                df = pd.DataFrame(table_data)

                if not df.empty:
                    df.columns = df.iloc[0]  # 첫 행을 컬럼명으로 사용
                    df = df[1:]  # 헤더 행은 데이터에서 제외

                if not os.path.exists(rf"{self.excel_save_location}\{filename}.xlsx"):
                    with pd.ExcelWriter(rf"{self.excel_save_location}\{filename}.xlsx", engine='openpyxl') as writer:
                        df.to_excel(writer, sheet_name=sheetname, index=False)
                else:
                    with pd.ExcelWriter(rf"{self.excel_save_location}\{filename}.xlsx", engine='openpyxl', mode='a',
                                        if_sheet_exists='replace') as writer:
                        df.to_excel(writer, sheet_name=sheetname, index=False)

            except Exception as e:
                continue
        return

    # 수강 예정인 과목의 분반들을 긁어 오는 함수.
    async def get_expected_courses(self, year, semester, contents):
        await self.setup()
        new_page = await self.browser.new_page()
        await self.login(self.portal_id, self.portal_pw, new_page)
        await self.page.close()
        table_data = []
        try:
            await new_page.goto("https://hakstd.jnu.ac.kr/web/Suup/Suup053")
            columns = ["수업장소","교과목명","교과목번호-분반","수업운영방식","학점","담당교수","강의시간","강의실","비고"]

            for course in contents:
                # 년도 선택
                year_element = await new_page.wait_for_selector("#ContentPlaceHolder_ContentPlaceHolderSub_ddlYY", timeout=5000)
                await year_element.select_option(value=year)
                # 학기 선택
                await new_page.select_option("#ContentPlaceHolder_ContentPlaceHolderSub_ddlTerm", value=semester)
                # 교과목 명 입력
                await new_page.fill("#ContentPlaceHolder_ContentPlaceHolderSub_txtSubj", value = course[0])
                # 조회 버튼 누르기
                await new_page.click("#ContentPlaceHolder_ContentPlaceHolderSub_btnSearch")

                scroll_table = await new_page.query_selector("#gvData")
                rows = await scroll_table.query_selector_all("tr")
                delete_value = [4, 5, 6, 8, 9, 14]
                # 행별로 데이터를 추출하여 리스트에 저장

                for row in rows:
                    # 헤더 셀(th)와 일반 데이터 셀(td)을 모두 고려합니다.
                    cells = await row.query_selector_all("th")
                    if not cells:
                        cells = await row.query_selector_all("td")

                    # 각 셀의 텍스트를 가져와 리스트로 저장 (불필요한 공백 제거)
                    row_data = [(await cell.inner_text()).strip() for i, cell in enumerate(cells) if
                                i not in delete_value]
                    if len(row_data) <= 1:
                        continue
                    elif row_data and row_data[2].split("-")[0] == course[1]:  # 빈 행은 제외
                        table_data.append(row_data)

            df = pd.DataFrame(table_data, columns = columns)
            await self.get_expected_data("expected","mycontent", df)

            await new_page.close()
            return f"SBEDL [성공] 예상 과목 데이터 로드를 완료했습니다."
        except Exception as e:
            await new_page.close()
            return f"FBEDL [오류] 예상 과목 데이터 수집 도중 문제가 발생했습니다.\n다시 작업해주세요.\n{e}"

    # 엑셀로 저장하기.
    async def get_expected_data(self, filename, sheetname, df):
        for attempt in range(3):
            try:
                if not os.path.exists(rf"{self.excel_save_location}\{filename}.xlsx"):
                    with pd.ExcelWriter(rf"{self.excel_save_location}\{filename}.xlsx", engine='openpyxl') as writer:
                        df.to_excel(writer, sheet_name=sheetname, index=False)
                else:
                    with pd.ExcelWriter(rf"{self.excel_save_location}\{filename}.xlsx", engine='openpyxl', mode='a',
                                        if_sheet_exists='replace') as writer:
                        df.to_excel(writer, sheet_name=sheetname, index=False)

            except Exception as e:
                continue
        return

    # 로그인 하는 함수
    async def login(self, portal_id, portal_pw, page = None):
        self.portal_id = portal_id
        self.portal_pw = portal_pw
        await self.setup()
        if page is None:
            page1 = self.page
        else:
            page1 = page
        await page1.goto("https://sso.jnu.ac.kr/Idp/Login.aspx")
        for attempt in range(10):
            try:
                await page1.wait_for_selector("text=로그인", timeout=3000)
                await page1.fill("#userId", portal_id)
                await page1.fill("#userPwd", portal_pw)
                await page1.click("#btnLoginButton")
                try:
                    await page1.wait_for_selector('a[title="로그아웃"]', timeout=5000)
                    return "LIS00 [성공] 포털 로그인에 성공했습니다."

                except TimeoutError:
                    await page1.close()
                    return "LIF00 [실패] 로그인 실패 또는 타임아웃."

            except TimeoutError:
                await page1.click('a[title="로그아웃"]')
            except Exception:
                await page1.close()
                return "LIF00 [오류] 로그인 도중 문제가 발생했습니다.\n다시 작업해주세요."
            finally:
                if page is None:
                    await page1.close()


    # page 제거 함수
    async def teardown(self):
        if self.browser:
            await self.browser.close()
        if hasattr(self, "playwright"):
            await self.playwright.stop()









