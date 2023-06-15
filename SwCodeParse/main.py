from Lib.DataProcess.file.fileLoad import *
from Lib.DataProcess.flow.drawFlow import *
from Lib.DataProcess.code.codeParse import *
from Lib.DataProcess.design.swDS import *
from Lib.DataProcess.design.swDD import *
from Lib.DataProcess.doc.wordWrap import *
from Lib.DataProcess.doc.excelWrap import *
from Lib.Common.basicFunction import *
import configparser

config = configparser.ConfigParser()
config.read('./config/config_sys.ini', encoding='utf-8')

if __name__ == "__main__":
    # Debug Start
    logging_initialize()
    logging_print(".... START: SwDS and SWDD Excel Generation .....\n")

    # Prerequisites: complete removal of occupied result
    remove_data_in_dir('./result')  # removal of occupied result
    remove_data_in_dir('./tool/tceetree/src')  # remove occupied tceetree source files

    PJfile = FileLoader(config=config)  # Load project files

    draw = DrawFlow(c_files=PJfile.c_lst, tcee_lib=PJfile.tcee_lib)  # Define draw class
    draw.run_flow()  # Run drawing a flow

    codeParser = CodeParser()  # Define Code Parser
    total_files = PJfile.c_lst + PJfile.h_lst  # Define files to be Parsed

    for file in total_files:
        codeParser.run(file)

    swDS = SwDsGenerator(PJfile.flash_usage, config['system']['doc_type'])
    swDD = SwDdGenerator(PJfile.global_h)

    if config['system']['doc_type'] == 'Word':
        word = WordWrapper()
        word.set_ds(swDS.component_dev, swDS.component_des)
        word.set_dd(swDD.dict_global_h, swDD.dict_component)
    else:
        excel = ExcelWrapper()
        excel.set_ds(swDS.component_dev, swDS.component_des)
        excel.set_dd(swDD.dict_global_h, swDD.dict_component)
# This is a new line that ends the file
