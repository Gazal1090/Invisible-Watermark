import imwatermark.watermark as water
import cv2

bgr = cv2.imread('D:/Downloads/lena.png')
wm = 'ritwikreddyphotography'

bgr_encoded2 = water.encoder(bgr, wm)
cv2.imwrite('D:/Downloads/test_wm.png', bgr_encoded2)

bgr2 = cv2.imread('D:/Downloads/test_wm.png')
watermark = water.decoder(bgr2, 22)
print(watermark)
