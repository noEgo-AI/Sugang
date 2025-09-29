import pyautogui
import re


def like_pattern(value, pattern):
    # SQL 패턴을 정규식으로 변환
    print(value)
    print(pattern)
    pattern = pattern.replace('%', '.*').replace('_', '.')
    return bool(re.fullmatch(pattern, value))

print(like_pattern('공학수학1', '수학1%'))
print("현재 마우스 위치:", pyautogui.position())

page = ["선수과목","hello"]
keywords = ["선수과목", "Prerequisite"]
idx = next((page.index(kw) for kw in keywords if kw in page))

if idx != -1:
    print(page[idx + 1])  # 다음 요소 출력
else:
    print("해당 키워드 없음")