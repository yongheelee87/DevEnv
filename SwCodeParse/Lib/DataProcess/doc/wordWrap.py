import time
from PIL import Image
from docx import Document
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from docx.shared import Inches, RGBColor, Pt
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT

from Lib.Common.basicFunction import *

WIDTH_MARGIN = 0.7
HEIGHT_MARGIN = 0.5
WIDTH = 8.5 - (WIDTH_MARGIN * 2)

UNIT_COL = ['Unit ID', 'Unit Name', 'Prototype', 'Parameters', 'Return Value', 'Description', 'Risk', 'Related Task ID',
            'Related ID']


class WordWrapper:
    def __init__(self):
        super().__init__()
        isdir_and_make('./result/doc')

        self.ds_dev_width = {0: 0.1, 1: 0.25, 2: 0.2, 3: 0.15, 4: 0.3}
        self.ds_des_width = {0: 0.25, 1: 0.75}
        self.dd_info_width = {0: 0.25, 1: 0.25, 2: 0.50}
        self.dd_global_width = {0: 0.3, 1: 0.1, 2: 0.2, 3: 0.4}
        self.dd_unit_width = {0: 0.25, 1: 0.75}
        self.dd_def_width = {0: 0.5, 1: 0.5}

    def set_ds(self, component_dev, component_des):
        # Create a new Word document\
        doc_ds = Document()

        self._font_size(doc_ds, 'Normal', 10)
        self._font_size(doc_ds, 'Heading 1', 14)
        self._font_size(doc_ds, 'Heading 2', 13)
        self._font_size(doc_ds, 'Heading 3', 12)

        self._margin_page(doc=doc_ds, height=HEIGHT_MARGIN, width=WIDTH_MARGIN)

        # Heading 1: Introduction
        doc_ds.add_heading('1  Introduction', level=1)
        doc_ds.add_heading('1.1  Purpose', level=2)
        doc_ds.add_paragraph(
            'The purpose of the software design specification is to define the software architecture using the software requirements specification, to develop the specification for the software component, and to provide the software design engineer and the software integration test engineers. If a risk is identified during the process, risk is registered and managed in ALM.')
        doc_ds.add_heading('1.2  Scope', level=2)
        doc_ds.add_paragraph(
            'This software design specification was developed for the project. This document contains the following contents.\n  •  Software static structure\n  •  Software dynamic behavior\n  •  Task design')
        doc_ds.add_heading('1.3  Terms, Abbreviations and Definitions', level=2)
        doc_ds.add_paragraph('Refer to')
        doc_ds.add_heading('1.4  Reference', level=2)
        doc_ds.add_heading('1.5  Information', level=2)
        doc_ds.add_paragraph('The Requirement ID rule follows the LGIT ID Naming Rule.\nRefer to Naming Rule.xlsx.')

        # Heading 2: Software Architecture
        doc_ds.add_heading('2  Software Architecture Design', level=1)
        doc_ds.add_heading('2.1  Software Architecture', level=2)
        doc_ds.add_heading('2.1.1  Component Development Type', level=3)
        self._convert_df_tbl(doc_ds, component_dev, self.ds_dev_width)
        doc_ds.add_heading('2.1.2  Partitioning Information', level=3)
        doc_ds.add_heading('2.2  Architecture Design Criteria', level=2)
        doc_ds.add_heading('2.2.1  Design Method', level=3)
        doc_ds.add_paragraph('The system was designed with modular design method considering the following points.\n'
                             '  •  Hierarchical design\n'
                             '  •  Precisely defined interfaces\n'
                             '  •  Avoid unnecessary complexity of hardware and software components\n'
                             '  •  Avoid unnecessary complexity of the interface\n'
                             '  •  Maintainability during operation\n'
                             '  •  Ease of testing during development and operation\n'
                             'For more information, refer to <Software Architecture Design Guidelines>.')
        doc_ds.add_heading('2.2.2  Evaluation Criteria', level=3)
        doc_ds.add_paragraph(
            'When designing the software architecture, the quality attributes are designed considering the following criteria.\n'
            '  •  Modularity\n  •  Maintainability\n  •  Expandability\n  •  Scalability\n  •  Reliability\n  •  Security\n  •  Usability\n'
            'For detailed information on evaluation criteria, refer to <System Architecture Design Guidelines>.')
        doc_ds.add_heading('2.2.3  Software Interface Error Handling', level=3)
        doc_ds.add_heading('2.3  Software Component Description', level=2)
        self._sw_com_descript(doc_ds, component_des)

        # Heading 3: Software Dynamic Behavior
        doc_ds.add_heading('3  Software Dynamic Behavior', level=1)

        time_var = time.strftime('%Y%m%d', time.localtime(time.time()))
        doc_ds.save('./result/doc/Confidential_SwDS_{}.docx'.format(time_var))

    def set_dd(self, header_dict, component_dict):
        # Create a new Word document\
        doc_dd = Document()

        self._font_size(doc_dd, 'Normal', 10)
        self._font_size(doc_dd, 'Heading 1', 14)
        self._font_size(doc_dd, 'Heading 2', 13)
        self._font_size(doc_dd, 'Heading 3', 12)
        self._font_size(doc_dd, 'Heading 4', 11)
        self._font_size(doc_dd, 'Heading 5', 10)

        self._margin_page(doc=doc_dd, height=HEIGHT_MARGIN, width=WIDTH_MARGIN)

        # Heading 1: Introduction
        doc_dd.add_heading('1  Introduction', level=1)
        doc_dd.add_heading('1.1  Purpose', level=2)
        doc_dd.add_paragraph(
            'The purpose of developing the software detailed design specification is to perform the software detailed design based on the software design specification. In this step, we identify the internal variables that make up the global variables and software components that make up each component, and design the internal logic of each function. This document is used as the development reference document for the software developers and software tester. If a risk is identified during the process, risk is registered and managed in ALM.')
        doc_dd.add_heading('1.2  Scope', level=2)
        doc_dd.add_paragraph(
            'This software unit design specification was developed for the project. This document contains the following contents.\n  •  Software global variable control strategy\n  •  Software common header information\n  •  For each component\n\t-  Header information\n\t-  Unit interaction\n\t-  Global variable\n\t-  Unit information')
        doc_dd.add_heading('1.3  Terms, Abbreviations and Definitions', level=2)
        doc_dd.add_paragraph('Refer to')
        doc_dd.add_heading('1.4  Reference', level=2)
        doc_dd.add_heading('1.5  Information', level=2)
        doc_dd.add_paragraph('The Requirement ID rule follows the LGIT ID Naming Rule.\nRefer to Naming Rule.xlsx.')

        # Heading 2: Software Detailed Design
        doc_dd.add_heading('2  Software Detailed Design', level=1)
        doc_dd.add_heading('2.1  Non Functional Requirements', level=2)
        doc_dd.add_heading('2.2  Global Variable Handling Strategy', level=2)
        doc_dd.add_heading('2.3  Global Header', level=2)

        number = 1
        for head, head_data in header_dict.items():
            doc_dd.add_heading('2.3.{}  {}'.format(number, head), level=3)
            self._convert_df_tbl(doc=doc_dd, df=head_data, width_ratio=self.dd_def_width, col_center=False)
            number += 1

        doc_dd.add_heading('2.4  Component', level=2)
        number = 1
        for comp, comp_data in component_dict.items():
            doc_dd.add_heading('2.4.{}  {}'.format(number, comp), level=3)

            self._convert_df_tbl(doc=doc_dd, df=comp_data[0], width_ratio=self.dd_info_width)

            doc_dd.add_heading('2.4.{}.1  Header Variable'.format(number), level=4)
            if not comp_data[1].empty:
                doc_dd.add_heading('2.4.{}.1.1  {}.h'.format(number, comp), level=5)
                self._convert_df_tbl(doc=doc_dd, df=comp_data[1], width_ratio=self.dd_def_width)

            doc_dd.add_heading('2.4.{}.2  Global Variable'.format(number), level=4)
            self._convert_df_tbl(doc=doc_dd, df=comp_data[2], width_ratio=self.dd_global_width, col_center=False)

            doc_dd.add_heading('2.4.{}.3  Interface / Internal Unit List'.format(number), level=4)
            self._convert_df_tbl(doc=doc_dd, df=comp_data[3], width_ratio=self.dd_unit_width, col_sh=True)

            doc_dd.add_heading('2.4.{}.4  Interaction between units'.format(number), level=4)
            doc_dd.add_heading('2.4.{}.5  Interface unit'.format(number), level=4)
            self._unit_contents(doc=doc_dd, df=comp_data[4], comp=comp)
            doc_dd.add_heading('2.4.{}.6  Internal unit'.format(number), level=4)
            self._unit_contents(doc=doc_dd, df=comp_data[5], comp=comp)

            number += 1

        time_var = time.strftime('%Y%m%d', time.localtime(time.time()))
        doc_dd.save('./result/doc/Confidential_SwDD_{}.docx'.format(time_var))

    def _sw_com_descript(self, doc, dict_des):
        number = 1
        for comp, comp_des in dict_des.items():
            doc.add_heading('2.3.{}  {}'.format(number, comp), level=3)
            table = self._convert_df_tbl(doc=doc, df=comp_des, width_ratio=self.ds_des_width, col_sh=True)
            png_file = './result/pngTceeTree/{component}.ext.out.png'.format(component=comp)
            if os.path.exists(png_file):
                self._insert_image_table(table, 3, 1, png_file)
            number += 1

    def _unit_contents(self, doc, df, comp):
        for i in range(len(df)):
            data = [''] + list(df.iloc[i].values) + ['Low', '', '']
            data[5] += '\n\n'  # Description 띄어쓰기 넣기
            table = self._convert_df_tbl(doc=doc, df=pd.DataFrame({'Attribute': UNIT_COL, 'Contents': data}),
                                         width_ratio=self.dd_unit_width, col_sh=True)
            png_file = './result/pngValve/{component}/{name}.png'.format(component=comp, name=data[1])
            if os.path.exists(png_file):
                self._insert_image_table(table, 6, 1, png_file)
            doc.add_paragraph()

    # noinspection PyMethodMayBeStatic
    def _convert_df_tbl(self, doc, df, width_ratio, col_center: bool = True, col_sh: bool = False):
        # doc_ds.add_paragraph()

        # Add a table to the document
        table = doc.add_table(rows=len(df) + 1, cols=len(df.columns), style='Table Grid')
        table.autofit = False

        # Add the column names to the first row of the table
        for j in range(len(df.columns)):
            table.cell(0, j).text = df.columns[j]
            table.cell(0, j)._tc.get_or_add_tcPr().append(
                parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w'))))  # Cell Color
            table.cell(0, j).width = Inches(WIDTH * width_ratio[j])
            table.cell(0, j).vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            table.cell(0, j).paragraphs[0].alignment = WD_TABLE_ALIGNMENT.CENTER

        # Add the data to the table
        for i in range(len(df)):
            for j in range(len(df.columns)):
                table.cell(i + 1, j).text = str(df.values[i, j])
                table.cell(i + 1, j).width = Inches(WIDTH * width_ratio[j])
                if j == 0:
                    if col_center:
                        table.cell(i + 1, j).paragraphs[0].alignment = WD_TABLE_ALIGNMENT.CENTER
                        table.cell(i + 1, j).vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                    if col_sh:
                        table.cell(i + 1, j)._tc.get_or_add_tcPr().append(
                            parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w'))))  # Cell Color

        self._make_rows_bold(table.rows[0])
        return table

    # noinspection PyMethodMayBeStatic
    def _font_size(self, doc, area, point):
        font = doc.styles[area].font
        font.color.rgb = RGBColor(0, 0, 0)
        font.size = Pt(point)
        font.name = 'Arial'

    # noinspection PyMethodMayBeStatic
    def _margin_page(self, doc, height, width):
        sections = doc.sections

        for section in sections:
            section.top_margin = Inches(height)
            section.bottom_margin = Inches(height)
            section.left_margin = Inches(width)
            section.right_margin = Inches(width)

    # noinspection PyMethodMayBeStatic
    def _make_rows_bold(self, *rows):
        for row in rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.bold = True

    # noinspection PyMethodMayBeStatic
    def _insert_image_table(self, table, row_idx, col_idx, png_file):
        run = table.rows[row_idx].cells[col_idx].paragraphs[0].add_run()
        w, h = Image.open(png_file).size
        width = to_inch_pixel(w)
        height = to_inch_pixel(h)
        portion = width / height

        if width > 5.0:
            run.add_picture(png_file, width=Inches(5.0), height=Inches(5.0 / portion))
        elif height > 6.8:
            run.add_picture(png_file, width=Inches(6.8 * portion), height=Inches(6.8))
        else:
            run.add_picture(png_file, width=Inches(width), height=Inches(portion))

