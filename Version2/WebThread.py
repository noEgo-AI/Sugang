# WebThread.py
# 인공지능학부 242149 이수용

import asyncio
from typing import Callable, Any

from PySide6.QtCore import QThread, Signal

import webcrawling


class AsyncWorkerThread(QThread):
    result_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.loop = None
        self.crawler = webcrawling.Crawling()

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def stop(self):
        if self.loop and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)

    def submit(self, coro: Callable[..., Any], *args, **kwargs):
        if not self.loop or not self.loop.is_running():
            raise RuntimeError("이벤트 루프가 실행 중이 아님")

        coroutine = coro(*args, **kwargs)
        future = asyncio.run_coroutine_threadsafe(coroutine, self.loop)
        future.add_done_callback(lambda f: self.result_signal.emit(str(f.result())))

    def resend(self, message: str):
        self.result_signal.emit(message)