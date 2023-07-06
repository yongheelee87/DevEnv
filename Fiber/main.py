import sys
import os
import platform
from Qt.MainQt import *

VERSION = 'v1.0'
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # 프로그램 화면을 보여주는 코드
    window = MainWindow()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드 및 프로그램 동작이 끌날시 시스템 종료 코드
    sys.exit(app.exec())
