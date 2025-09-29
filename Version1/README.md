# 강의 정보 자동 수집 시스템

강의계획서 및 과목 정보를 자동으로 수집하여 Excel 파일로 정리하는 Python 프로그램입니다.

## 🚀 주요 기능

- 강의 정보 자동 수집
- 선수과목 정보 PDF 분석
- 수집된 데이터를 Excel 파일로 자동 저장
- GUI 인터페이스 제공

## 📋 요구사항

### Python 버전
- Python 3.12 이상 권장

### 주요 라이브러리
- `selenium`: 웹 자동화
- `pandas`: 데이터 처리
- `openpyxl`: Excel 파일 처리
- `PySide6`: GUI 인터페이스
- `PyMuPDF`: PDF 파일 처리
- `beautifulsoup4`: HTML 파싱
- `pyautogui`: 자동화 지원

## 🛠️ 설치 방법

1. 저장소 클론 또는 다운로드
```bash
git clone [repository-url]
cd Version1
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. Microsoft Edge 브라우저 설치 (필수)
   - 프로그램이 Edge WebDriver를 사용합니다

## 📁 파일 구조

```
Version1/
├── main_controller.py      # 메인 컨트롤러 (GUI 포함)
├── only_code.py           # 핵심 스크래핑 로직
├── example.py             # 테스트 및 예제 코드
├── UI_initial_form.ui     # Qt Designer UI 파일
├── UI_initial_form.py     # UI 파이썬 코드
├── requirements.txt       # Python 의존성
├── environment.yaml       # Conda 환경 파일
└── README.md             # 이 파일
```

## 🖥️ 사용 방법

### 1. GUI 버전 실행
```bash
python main_controller.py
```

### 2. 콘솔 버전 실행
```bash
python only_code.py
```

## ⚙️ 설정

### 로그인 정보 수정
`only_code.py` 파일의 98-99번째 줄에서 로그인 정보를 수정하세요:
```python
Id_element.send_keys("your_username")    # 사용자명 입력
Pw_element.send_keys("your_password")    # 비밀번호 입력
```

### PDF 다운로드 경로 설정
212번째 줄에서 다운로드 경로를 수정하세요:
```python
path1 = r"C:\Users\your_username\Downloads"  # 다운로드 폴더 경로
```

### PDF 처리 활성화/비활성화
21번째 줄에서 PDF 처리 기능을 제어하세요:
```python
ppl = 1  # PDF 가져오기 끄기: 1, 켜기: 0
```

## 📊 출력 데이터

프로그램 실행 후 다음과 같은 Excel 파일이 생성됩니다:
- 파일명: `renewing_YYYYMMDDHHMMSS.xlsx`
- Sheet1: 수집된 강의 정보
- pre_subject: 선수과목 정보 (PDF에서 추출)

## 🔧 주요 함수 설명

### `only_code.py`
- `site_login()`: 전남대학교 SSO 로그인
- `select_btn()`: 연도 선택 및 검색
- `bring_the_data()`: 강의 데이터 수집
- `select_btn_bring()`: 상세 강의 정보 수집
- `open_pdf()`: PDF에서 선수과목 정보 추출

### `main_controller.py`
- `inital`: GUI 메인 윈도우 클래스
- `major_seletor()`: 전공 선택 기능
- `msgbox()`: 알림창 표시

## ⚠️ 주의사항

1. **로그인 정보 보안**: 코드에 실제 로그인 정보를 직접 입력하지 마세요
2. **웹사이트 정책**: 해당 웹사이트의 이용약관을 준수하세요
3. **과도한 요청 금지**: 서버에 과부하를 주지 않도록 적절한 간격으로 요청하세요
4. **Edge 브라우저**: Microsoft Edge가 설치되어 있어야 합니다

## 🐛 문제 해결

### 자주 발생하는 오류
1. **WebDriver 오류**: Edge 브라우저 최신 버전 설치 확인
2. **로그인 실패**: 아이디/비밀번호 확인
3. **요소 찾기 실패**: 웹사이트 구조 변경 시 코드 수정 필요

### 디버깅
- 콘솔 출력을 확인하여 오류 메시지 파악
- `time.sleep()` 값을 늘려 페이지 로딩 시간 확보
- 개발자 도구를 사용하여 웹 요소 확인

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다. 상업적 사용 시 해당 웹사이트의 이용약관을 확인하세요.

## 🤝 기여

버그 리포트나 기능 개선 제안은 이슈로 등록해 주세요.

---

**개발환경**: Windows 10/11, Python 3.12, Microsoft Edge
**최종 수정일**: 2025년 9월