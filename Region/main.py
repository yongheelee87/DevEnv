import cv2
import numpy as np

from void_extraction import *

IMG_NAME = r'F_0_w_m003.tif'
THRESHOLD_COLOR = 250
THRESHOLD_AREA = 10  # 이것보다 작은 AREA 필터
BOTTOM_CROP = 0.07  # 밑부분 자르기
DRAWING_LINE_THICK = -1  # 외곽선 두께. thinkness < 0이면 내부를 채운다.
# DRAWING_BGR = (255, 255, 204)  # 외곽선 컬러 blue, green, red
DRAWING_BGR = (147, 249, 150)  # 외곽선 컬러 blue, green, red
DRAWING_VOID_BGR = (0, 0, 255)  # 외곽선 Void 컬러 blue, green, red
VOID_THRESHOLD_AREA = 10  # Void 이것보다 작은 AREA 필터
BLACK_THRESHOLD_AREA = 210  # Void Black 기준

def get_contours(image):
    # convert to grayscale
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # convert img into binary
    _, thresh = cv2.threshold(imgray, THRESHOLD_COLOR, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 0)

    # calculating Contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    closed_area = []
    closed_contours = []
    open_contours = []
    for i in contours:
        area = cv2.contourArea(i)
        perimeter = cv2.arcLength(i, True)

        if area > perimeter or area > THRESHOLD_AREA:
            closed_area.append(area)
            closed_contours.append(i)
        else:
            open_contours.append(perimeter)

    return contours, closed_contours, sum(closed_area) / imgray.size * 100


if __name__ == '__main__':
    im = cv2.imread('./data/' + IMG_NAME)
    im = im[:int(im.shape[0]*(1-BOTTOM_CROP)), :]
    im_origin = im.copy()

    void = VoidExtract(im, IMG_NAME, VOID_THRESHOLD_AREA, BLACK_THRESHOLD_AREA)

    bubble_cnt, bubble_close_cnt, bubble_area = get_contours(im)
    void_cnt, _, void_area = get_contours(void.get_image())

    print('Percentage of total area :\n- Area of Bubble: {:.5f}%\n- Area of Void: {:.5f}%\n'.format(bubble_area, void_area))

    cv2.drawContours(im, bubble_close_cnt, -1, DRAWING_BGR, DRAWING_LINE_THICK)
    cv2.drawContours(im, bubble_close_cnt, -1, DRAWING_BGR, 2)
    # cv2.drawContours(im, void_cnt, -1, DRAWING_VOID_BGR, 2)
    cv2.drawContours(im, void_cnt, -1, DRAWING_VOID_BGR, DRAWING_LINE_THICK)
    cv2.imwrite('./data/Result_{}.jpg'.format(IMG_NAME[:IMG_NAME.find('.')]), im)
    cv2.imshow('image_original', im_origin)
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

