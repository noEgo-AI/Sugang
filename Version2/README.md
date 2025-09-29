# 전남대학교 수강신청 도우미

전남대학교 포털을 이용한 수강신청 및 시간표 관리 프로그램입니다.

## 🚀 빠른 시작

### 방법 1: Conda 환경 사용 (권장)

#### 1. 저장소 클론
```bash
git clone <repository-url>
cd registrationProject
```

#### 2. Conda 환경 생성 및 활성화
```bash
# 환경 생성
conda env create -f environment.yaml

# 환경 활성화
conda activate sugang
```

#### 3. 자동 브라우저 설정
```bash
python setup_browser.py
```

#### 4. 프로그램 실행
```bash
python main.py
```

### 방법 2: pip 사용

#### 1. 저장소 클론
```bash
git clone <repository-url>
cd registrationProject
```

#### 2. 가상환경 생성 (선택사항)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

#### 4. 자동 브라우저 설정
```bash
python setup_browser.py
```

#### 5. 프로그램 실행
```bash
python main.py
```

### 자동 설정 스크립트 기능
`python setup_browser.py` 스크립트는 자동으로:
- Playwright와 Chromium 브라우저를 설치합니다
- 운영체제에 맞는 브라우저 경로를 감지하고 설정합니다
- 필요한 의존성 패키지를 확인합니다

## 📋 시스템 요구사항

- **Python**: 3.12 (Conda 환경 기준) 또는 3.8 이상 (pip 환경)
- **운영체제**: Windows, macOS, Linux
- **패키지 관리자**: Conda (권장) 또는 pip
- **RAM**: 최소 4GB (권장 8GB)
- **디스크 공간**: 최소 1GB (브라우저 포함)
- **네트워크**: 인터넷 연결 (포털 접근 및 초기 설치)

## 🛠️ 주요 기능

### 1. 포털 로그인
- 전남대학교 통합 포털 자동 로그인
- 세션 관리 및 자동 재연결

### 2. 수강 데이터 관리
- **기초 수강 내역**: 전공별 개설 과목 정보 수집
- **수강 완료 내역**: 기수강한 과목 정보 가져오기
- **현재 수강 내역**: 현재 학기 수강 과목 확인
- **예상 과목 생성**: 선택한 과목의 분반 정보 수집

### 3. 시간표 관리
- 시각적 시간표 표시
- 시간 중복 검사
- 과목별 색상 구분
- 학점 계산 및 관리

### 4. 데이터 내보내기
- Excel 형식으로 데이터 저장
- 과목별 시트 분리
- 학기별 데이터 관리

## 📁 프로젝트 구조

```
registrationProject/
├── main.py                 # 메인 애플리케이션
├── webcrawling.py          # 웹 크롤링 모듈
├── WebThread.py            # 비동기 작업 스레드
├── setup_browser.py        # 브라우저 자동 설치
├── requirements.txt        # pip 의존성 목록
├── environment.yaml        # Conda 환경 설정 파일 (권장)
├── README.md               # 프로젝트 설명서
├── .gitignore              # Git 제외 파일 목록
├── emitcode.txt            # 코드 관련 설정
├── ui_component/           # UI 컴포넌트
├── ms-playwright/          # Playwright 브라우저 (자동 생성)
└── Documents/SuGang/       # 데이터 저장 폴더 (자동 생성)
    ├── excel/              # Excel 파일 저장
    └── syllabus/           # 강의계획서 저장
```

## 📦 의존성 관리

프로젝트는 두 가지 의존성 관리 방법을 지원합니다:

### Conda (권장)
- `environment.yaml`: 완전한 환경 재현 가능
- 모든 시스템 레벨 의존성 포함
- Python 3.12 및 최적화된 패키지 버전

### pip
- `requirements.txt`: 핵심 Python 패키지만 포함
- 가벼운 설치 옵션
- 기존 Python 환경에 추가 설치

## 🔧 설정 및 트러블슈팅

### 브라우저 경로 문제
프로그램이 브라우저를 찾지 못할 경우:

1. 자동 설정 재실행:
   ```bash
   python setup_browser.py
   ```

2. 수동 설정 (webcrawling.py 수정):
   ```python
   BROWSER_PATH = r"C:\your\browser\path\chrome.exe"
   ```

### 지원되는 브라우저 경로
- **Windows**:
  - Playwright Chromium: `ms-playwright/chromium/chrome.exe`
  - Google Chrome: `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - 사용자별 Chrome: `%USERPROFILE%\AppData\Local\Google\Chrome\Application\chrome.exe`

- **macOS**:
  - Playwright Chromium: `ms-playwright/chromium/Chromium.app/Contents/MacOS/Chromium`
  - Google Chrome: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

- **Linux**:
  - Playwright Chromium: `ms-playwright/chromium/chromium`
  - 시스템 브라우저: `chromium`, `chromium-browser`, `google-chrome`

### 일반적인 문제 해결

#### 1. "페이지가 닫힘" 오류
- 브라우저가 예상치 못하게 종료된 경우
- 프로그램을 재시작하세요

#### 2. 로그인 실패
- 포털 아이디와 비밀번호를 확인하세요
- 네트워크 연결을 확인하세요
- 전남대학교 포털 접속 상태를 확인하세요

#### 3. 데이터 로드 실패
- 먼저 포털 로그인을 완료하세요
- 각 단계를 순서대로 진행하세요:
  1. 기초 수강 내역 가져오기
  2. 내 수강 내역 가져오기
  3. 현재 수강 내역 가져오기

## 🔒 보안 및 개인정보

- **로그인 정보**: 프로그램 종료 시 자동 삭제됩니다
- **저장 데이터**: 로컬 컴퓨터에만 저장됩니다
- **네트워크**: 전남대학교 공식 포털에만 접근합니다

## 🤝 기여하기

1. Fork 프로젝트
2. Feature 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경사항 커밋 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

## 📞 지원

문제가 발생하거나 기능 제안이 있으시면:
- GitHub Issues를 통해 보고해 주세요
- 개발자에게 직접 연락하세요

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

---

**주의사항**:
- 이 프로그램은 개인 학습 및 편의를 위한 도구입니다
- 대학의 수강신청 정책을 준수하여 사용하세요
- 과도한 요청으로 서버에 부하를 주지 않도록 주의하세요