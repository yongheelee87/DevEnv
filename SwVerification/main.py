import sys
import os


class System:
    Ver = 'v1.0'  # SW Version
    Exe = 'UI'  # what kind of execution by CLI
    Yaml = False  # Test Yaml Changes by CLI

# os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


if __name__ == "__main__":
    for v in range(1, len(sys.argv)):
        if 'auto' in sys.argv[v] or 'Auto' in sys.argv[v]:
            System.Exe = 'auto'
        elif 'check' in sys.argv[v]:
            System.Exe = 'check'
        elif 'yaml' in sys.argv[v]:
            System.Yaml = True

    print("Preparing equipment for initialization, please wait while loading......\n")

    if 'UI' in System.Exe:
        from PySide6.QtWidgets import QApplication, QSplashScreen
        from PySide6.QtGui import QPixmap

        # QApplication : 프로그램을 실행시켜주는 클래스
        app = QApplication()
        splash = QSplashScreen(QPixmap('./static/images/loading.png'))
        splash.show()

        from Qt import *
        from Lib.Common import logging_initialize, logging_print

        # Logging module 초기화
        logging_initialize()
        logging_print(f"The program is named SW TEST Automation {System.Ver}. It provides the functions for the measurement and automation with various devices\n")

        # 프로그램 화면을 보여주는 코드
        window = MainWindow()
        splash.finish(window)

        # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
        app.exec()
    elif 'check' in System.Exe:
        from prereq.check_env import CheckEnv
        
        # Class for Check Environment
        check_env = CheckEnv()
        check_env.run()  # Check Environment 실행
    else:
        from Lib.Common import Configure
        from Lib.TestProcess import AutoTest
        print(f"The program is named SW TEST Automation {System.Ver}. It provides the functions for the measurement and automation with various devices\n")

        # 테스트 자동화 시행 클래스
        yaml_path = os.path.join(Configure.set['system']['git_path'].replace('mcu_rgw_project', ''), 'test_map.yaml')
        auto_test = AutoTest(test_yaml='./data/config/test_map.yaml') if System.Yaml is False else AutoTest(test_yaml=yaml_path)
        
        print(f"Current Test Environment\n{auto_test.df_inst}\n")
        auto_test.run()  # 테스트 자동화 실행

    # 프로그램 동작이 끌날시 시스템 종료 코드
    os._exit(0)
