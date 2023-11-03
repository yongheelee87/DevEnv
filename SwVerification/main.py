import sys
import os


class System:
    Ver = 'v1.0'  # SW Version
    Auto = False  # automatic execution by CLI

# os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


if __name__ == "__main__":
    for v in range(1, len(sys.argv)):
        if 'auto' in sys.argv[v] or 'Auto' in sys.argv[v]:
            System.Auto = True

    if System.Auto is False:
        from Qt.MainQt import *

        # Logging module 초기화
        logging_initialize()
        logging_print("The program is named SW TEST Automation {}. It provides the functions for the measurement and automation with various devices\n".format(System.Ver))

        # QApplication : 프로그램을 실행시켜주는 클래스
        app = QApplication()

        # 프로그램 화면을 보여주는 코드
        window = MainWindow()

        # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
        app.exec()

        # 프로그램 동작이 끌날시 시스템 종료 코드
        os._exit(0)
    else:
        from Lib.DataProcess.autoTest import *
        auto_test = AutoTest()
        auto_test.run()

        # 프로그램 동작이 끌날시 시스템 종료 코드
        os._exit(0)



