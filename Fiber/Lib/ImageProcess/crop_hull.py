import cv2
import numpy as np


class CropHull:
    def __init__(self):
        self.im = None
        self.color_threshold = None
        self.area_threshold = None
        self.kernel_threshold = None
        self.white_sensitivity = None

    def update_params(self, image, colorThres, areaThres, kernelThres, sensitivity):
        self.im = image  # read image
        self.color_threshold = colorThres
        self.area_threshold = areaThres
        self.kernel_threshold = kernelThres
        self.white_sensitivity = sensitivity

    def crop_image(self):
        # convert to grayscale
        imgray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)

        # threshold to binary
        thresh = cv2.threshold(imgray, self.color_threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # apply morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, self.kernel_threshold)
        kernel = cv2.dilate(kernel, None)

        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

        # invert morph
        # morph = 255 - morph

        # get external contours
        contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        # draw white contour on black background
        cntr_img = np.zeros_like(morph)
        for c in contours:
            area = cv2.contourArea(c)
            if area > self.area_threshold + 10:
                cv2.drawContours(cntr_img, [c], 0, 255, 1)

        # get all non-zero points
        points = np.column_stack(np.where(cntr_img.transpose() > 0))
        hull = cv2.convexHull(points)
        hull_area = cv2.contourArea(hull)

        mask = np.zeros_like(imgray)
        cv2.drawContours(mask, [hull], -1, (255, 255, 255), -1)
        img_mask = cv2.bitwise_and(imgray, imgray, mask=mask)
        img_mask = self.maks_white_color(img_mask)

        leftmost = tuple(hull[hull[:, :, 0].argmin()][0])[0]
        rightmost = tuple(hull[hull[:, :, 0].argmax()][0])[0]
        topmost = tuple(hull[hull[:, :, 1].argmin()][0])[1]
        bottommost = tuple(hull[hull[:, :, 1].argmax()][0])[1]

        img_coordiate = [topmost, bottommost, leftmost, rightmost]

        img_crop = self.im[topmost:bottommost, leftmost:rightmost]

        return img_crop, img_mask, hull, hull_area, img_coordiate

    def maks_white_color(self, img):
        im_mask = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        hsv = cv2.cvtColor(im_mask, cv2.COLOR_BGR2HSV)

        # define range of yellow color in HSV
        lower_white = np.array([0, 0, 255 - self.white_sensitivity])
        upper_white = np.array([255, self.white_sensitivity, 255])

        # Threshold the HSV image to get only blue colors
        mask_white = cv2.inRange(hsv, lower_white, upper_white)
        return mask_white
