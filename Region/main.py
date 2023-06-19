import cv2

IMG_NAME = r'f_#3.tif'
THRESHOLD_COLOR = 0
BOTTOM_CROP = 0.07  # 밑부분 자르기
DRAWING_LINE_THICK = -1  # 외곽선 두께. thinkness < 0이면 내부를 채운다.
DRAWING_BGR = (0, 0, 255)  # 외곽선 컬러 blue, green, red

if __name__ == '__main__':
    im = cv2.imread('./data/' + IMG_NAME)
    im = im[:int(im.shape[0]*(1-BOTTOM_CROP)), :]

    # convert to grayscale
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # convert img into binary
    _, thresh = cv2.threshold(imgray, THRESHOLD_COLOR, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # calculating Contours
    # contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        contours_area += area

    print('>> Area of Filler: {:.5f}%'.format(contours_area / imgray.size * 100))
    cv2.drawContours(im, contours, -1, DRAWING_BGR, DRAWING_LINE_THICK)
    cv2.imwrite('./data/Result_{}.jpg'.format(IMG_NAME[:IMG_NAME.find('.')]), im)
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

