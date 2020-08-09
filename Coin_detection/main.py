import cv2
import canny_detection

src_path = 'Coin_detection\picture.jpg'
src = cv2.imread(src_path, 0)

src = cv2.resize(src,(640,480))

dst = canny_detection.canny(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey(0)
