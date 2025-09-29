#!/usr/bin/env python3
"""
Chromium 자동 설치 및 브라우저 경로 설정 스크립트
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path

def is_chromium_installed():
    """Chromium이 이미 설치되어 있는지 확인"""
    browser_path = get_browser_path()
    return browser_path and os.path.exists(browser_path)

def get_browser_path():
    """운영체제별 Chromium 브라우저 경로 반환"""
    system = platform.system().lower()

    if system == "windows":
        # Playwright가 설치하는 Chromium 경로
        chromium_path = os.path.join(os.getcwd(), "ms-playwright", "chromium")

        # 가능한 실행 파일 경로들
        possible_paths = [
            os.path.join(chromium_path, "chrome.exe"),
            os.path.join(chromium_path, "chromium.exe"),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        # 시스템에 설치된 Chrome/Chromium 찾기
        system_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Users\{}\AppData\Local\Google\Chrome\Application\chrome.exe".format(os.getenv("USERNAME")),
        ]

        for path in system_paths:
            if os.path.exists(path):
                return path

    elif system == "darwin":  # macOS
        chromium_path = os.path.join(os.getcwd(), "ms-playwright", "chromium")
        possible_paths = [
            os.path.join(chromium_path, "Chromium.app", "Contents", "MacOS", "Chromium"),
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

    else:  # Linux
        chromium_path = os.path.join(os.getcwd(), "ms-playwright", "chromium")
        possible_paths = [
            os.path.join(chromium_path, "chromium"),
            os.path.join(chromium_path, "chrome"),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        # 시스템 경로에서 찾기
        system_commands = ["chromium", "chromium-browser", "google-chrome", "chrome"]
        for cmd in system_commands:
            if shutil.which(cmd):
                return shutil.which(cmd)

    return None

def install_playwright_browsers():
    """Playwright를 통해 Chromium 설치"""
    print("Playwright를 통해 Chromium을 설치하고 있습니다...")

    try:
        # Playwright 설치 확인
        subprocess.run([sys.executable, "-c", "import playwright"],
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Playwright가 설치되어 있지 않습니다. 설치 중...")
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)

    try:
        # Chromium 브라우저 설치
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"],
                      check=True)
        print("✅ Chromium 설치가 완료되었습니다.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Chromium 설치 중 오류가 발생했습니다: {e}")
        return False

def update_browser_path_in_code():
    """webcrawling.py 파일의 브라우저 경로를 자동으로 업데이트"""
    browser_path = get_browser_path()

    if not browser_path:
        print("❌ 브라우저 경로를 찾을 수 없습니다.")
        return False

    # 경로를 상대 경로로 변환 (현재 디렉토리 기준)
    try:
        rel_path = os.path.relpath(browser_path)
    except ValueError:
        # 다른 드라이브에 있는 경우 절대 경로 사용
        rel_path = browser_path

    webcrawling_file = "webcrawling.py"

    if not os.path.exists(webcrawling_file):
        print(f"❌ {webcrawling_file} 파일을 찾을 수 없습니다.")
        return False

    # 파일 읽기
    with open(webcrawling_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # BROWSER_PATH 라인 찾기 및 업데이트
    lines = content.split('\n')
    updated = False

    for i, line in enumerate(lines):
        if line.strip().startswith('BROWSER_PATH'):
            old_line = line
            # 새로운 경로로 업데이트
            lines[i] = f'BROWSER_PATH = r"{rel_path}"'
            print(f"브라우저 경로 업데이트:")
            print(f"  이전: {old_line}")
            print(f"  이후: {lines[i]}")
            updated = True
            break

    if updated:
        # 파일 쓰기
        with open(webcrawling_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print("✅ webcrawling.py 파일이 업데이트되었습니다.")
        return True
    else:
        print("❌ BROWSER_PATH를 찾을 수 없습니다.")
        return False

def main():
    """메인 실행 함수"""
    print("=== Chromium 자동 설치 및 설정 ===")
    print(f"운영체제: {platform.system()}")
    print(f"현재 디렉토리: {os.getcwd()}")

    # 이미 설치되어 있는지 확인
    if is_chromium_installed():
        print("✅ Chromium이 이미 설치되어 있습니다.")
        browser_path = get_browser_path()
        print(f"브라우저 경로: {browser_path}")
    else:
        print("Chromium이 설치되어 있지 않습니다. 설치를 시작합니다...")

        if not install_playwright_browsers():
            print("❌ Chromium 설치에 실패했습니다.")
            return False

    # 브라우저 경로 업데이트
    if update_browser_path_in_code():
        print("✅ 설정이 완료되었습니다!")
        return True
    else:
        print("❌ 설정 중 오류가 발생했습니다.")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)