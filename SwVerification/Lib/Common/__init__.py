# ///////////////////////////////////////////////////////////////
#
# BY: YONGHEE LEE
# PROJECT MADE WITH: measurement with script command
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# ///////////////////////////////////////////////////////////////
import yaml


# basic library
from . basicFunction import *


class SysConfig:
    def __init__(self, path: str):
        # 지정된 장소에 파일이 없을 경우 Remote에 설정된 파일 로드
        if os.path.isfile(path):
            self.path = path
        else:
            self.path = './data/config/remote/system_env.yaml'

        with open(self.path, encoding="utf-8-sig") as f:
            self.set = yaml.load(f, Loader=yaml.SafeLoader)

    def update(self):
        with open(self.path, encoding="utf-8-sig") as f:
            self.set = yaml.load(f, Loader=yaml.SafeLoader)


Configure = SysConfig(path='./data/config/system_env.yaml')  # Configuration 전역변수 선언
