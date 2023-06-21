import cv2
import numpy as np


class VoidExtract:
    def __init__(self, image, img_name, min_area, thresh):
        self.im = image
        self.im_name = img_name
        self.minArea = min_area
        self.black_thresh = thresh  # Black Thresh

    def get_image(self):
        # Threshold image:
        _, binaryImage = cv2.threshold(self._convert_kChannel(), self.black_thresh, 255, cv2.THRESH_BINARY)

        # Filter small blobs:
        binaryImage = self._areaFilter(binaryImage)

        # Use a little bit of morphology to clean the mask:
        # Set kernel (structuring element) size:
        kernelSize = 3
        # Set morph operation iterations:
        opIterations = 2
        # Get the structuring element:
        morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelSize, kernelSize))
        # Perform closing:
        binaryImage = cv2.morphologyEx(binaryImage, cv2.MORPH_CLOSE, morphKernel, None, None, opIterations, cv2.BORDER_REFLECT101)

        img_name = './data/Black_{}.png'.format(self.im_name[:self.im_name.find('.')])
        cv2.imwrite(img_name, binaryImage)

        return cv2.imread(img_name)

    def _convert_kChannel(self):
        # Convert to float and divide by 255:
        imgFloat = self.im.astype(np.float64) / 255.

        # Calculate channel K:
        kChannel = 1 - np.max(imgFloat, axis=2)

        # Convert back to uint 8:
        kChannel = (255 * kChannel).astype(np.uint8)

        return kChannel

    def _areaFilter(self, binaryImage):
        # Perform an area filter on the binary blobs:
        componentsNumber, labeledImage, componentStats, componentCentroids = cv2.connectedComponentsWithStats(binaryImage, connectivity=4)

        # Get the indices/labels of the remaining components based on the area stat
        # (skip the background component at index 0)
        remainingComponentLabels = [i for i in range(1, componentsNumber) if componentStats[i][4] >= self.minArea]

        # Filter the labeled pixels based on the remaining labels,
        # assign pixel intensity to 255 (uint8) for the remaining pixels
        filteredImage = np.where(np.isin(labeledImage, remainingComponentLabels) == True, 255, 0).astype('uint8')

        return filteredImage
