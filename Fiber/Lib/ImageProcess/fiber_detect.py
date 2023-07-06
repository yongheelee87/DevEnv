import os

import pandas as pd

from Lib.Common.basicFunction import *
from Lib.ImageProcess.void_extraction import *
from Lib.ImageProcess.crop_hull import *

DRAWING_LINE_THICK = -1  # 외곽선 두께. thinkness < 0이면 내부를 채운다.
DRAWING_HULL_THICK = 3  # 외곽선 두께. thinkness < 0이면 내부를 채운다.
# DRAWING_BGR = (255, 255, 204)  # 외곽선 컬러 blue, green, red
DRAWING_BGR = (147, 249, 150)  # Fiber 컬러 blue, green, red
DRAWING_VOID_BGR = (0, 0, 255)  #  Void 컬러 blue, green, red
DRAWING_HULL_BGR = (51, 102, 51)  #  외곽선 컬러 blue, green, red

DF_COL = ['Fiber', 'Void']  # dataframe Column
DF_INDEX = ['Percentage of total area', 'colorThres', 'areaThres', 'dilate(x, y)', 'ksize(x, y)', 'white sense']


class FiberDetection:
    def __init__(self):
        self.img_names = None
        self.color_threshold = 250
        self.area_threshold = 10  # 이것보다 작은 AREA 필터
        self.void_color_threshold = 250  # Void Black 기준
        self.void_area_threshold = 10  # Void 이것보다 작은 AREA 필터
        self.bottom_crop = 7  # 밑부분 자르기
        self.dilate_x = 1
        self.dilate_y = 1
        self.ksize_x = 6
        self.ksize_y = 6
        self.white_sense = 90

        self.void = VoidExtract()  # Void Extraction 선언
        self.hull = CropHull()  # Crop Hull 선언

        isdir_and_make('./data/result')  # result 폴더 만들기
        self.result_path = './data/result'

    def update_params(self, percent, colorThres, areaThres, colorVoidThres, areaVoidThres, dilateX, dilateY, ksizeX, ksizeY, white):
        self.bottom_crop = percent
        self.color_threshold = colorThres
        self.area_threshold = areaThres
        self.void_color_threshold = colorVoidThres
        self.void_area_threshold = areaVoidThres
        self.dilate_x = dilateX
        self.dilate_y = dilateY
        self.ksize_x = ksizeX
        self.ksize_y = ksizeY
        self.white_sense = white

    def image_process(self):
        str_res = ''
        for img_name in self.img_names:
            img_base_name, img_file_name = self._get_img_name(img_name)

            im = cv2.imread(img_name)
            im = im[:int(im.shape[0] * ((100 - self.bottom_crop) / 100)), :]
            im_origin = im.copy()

            self.hull.update_params(im, self.color_threshold, self.area_threshold, (self.ksize_x, self.ksize_y), self.white_sense)
            im_crop, im_mask, hull, hull_area, hull_coor = self.hull.crop_image()

            self.void.update_params(im_crop, img_base_name, self.void_area_threshold, self.void_color_threshold)

            fiber_cnt, fiber_close_cnt, fiber_area = self._get_contours(im_mask, False)
            void_cnt, _, void_area = self._get_contours(self.void.get_image(self.result_path), True)

            result = {DF_COL[0]: [fiber_area / hull_area * 100, self.color_threshold, self.area_threshold, self.dilate_x, self.ksize_x, self.white_sense],
                      DF_COL[1]: [void_area / hull_area * 100, self.void_color_threshold, self.void_area_threshold, self.dilate_y, self.ksize_y, None]}
            df_res = pd.DataFrame(result, index=DF_INDEX).round(2)
            df_res.to_csv('{}/Fiber_{}.csv'.format(self.result_path, img_file_name))

            cv2.drawContours(im_crop, void_cnt, -1, DRAWING_VOID_BGR, DRAWING_LINE_THICK)  # Void 이미지 그리기

            im[hull_coor[0]:hull_coor[1], hull_coor[2]:hull_coor[3]] = im_crop  # Crop된 이미지 본래 이미지에 넣기

            cv2.drawContours(im, fiber_close_cnt, -1, DRAWING_BGR, DRAWING_LINE_THICK)  # Fiber 내부 채우기
            cv2.drawContours(im, fiber_close_cnt, -1, DRAWING_BGR, 2)  # Fiber 선 그리기
            cv2.drawContours(im, [hull], -1, DRAWING_HULL_BGR, DRAWING_HULL_THICK)  # Hull 이미지 그리기

            cv2.imwrite('{}/Origin_{}.jpg'.format(self.result_path, img_file_name), im_origin)
            cv2.imwrite('{}/Fiber_{}.jpg'.format(self.result_path, img_file_name), im)
            cv2.imwrite('{}/Mask_{}.jpg'.format(self.result_path, img_file_name), im_mask)
            # cv2.imshow('image_original', im_origin)
            # cv2.imshow('image', im)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            print("Success: Result Image File is located in {}\n".format(self.result_path))
            df_new = df_res.rename(index={'Percentage of total area': 'Percentage'})
            str_img_csv = '[{}]\n\tFiber   Void\n{}\n\n'.format(img_base_name, df_new.to_string(header=False))
            str_res += str_img_csv
        return str_res

    def _get_img_name(self, img_full_name):
        base_name = os.path.basename(img_full_name)
        file_name = base_name[:base_name.find('.')]
        self.result_path = './data/result/{}'.format(file_name)
        isdir_and_make(self.result_path)  # image process result 폴더 만들기
        return base_name, file_name

    def _get_contours(self, image, grayscale: bool):
        # convert to grayscale
        if grayscale is True:
            imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            imgray = image

        # convert img into binary
        thresh = cv2.threshold(imgray, self.color_threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 0)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.dilate_x, self.dilate_y))
        thresh = cv2.dilate(thresh, kernel)  #  객체가 커지는 연산

        # calculating Contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        closed_area = []
        closed_contours = []
        open_contours = []
        for i in contours:
            area = cv2.contourArea(i)
            perimeter = cv2.arcLength(i, True)

            if area > perimeter or area > self.area_threshold:
                closed_area.append(area)
                closed_contours.append(i)
            else:
                open_contours.append(perimeter)

        return contours, closed_contours, sum(closed_area)

