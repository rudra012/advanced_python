import cv2

image_path = "img.png"
img_grey = cv2.imread(image_path, 0)
print(img_grey)
print(len(img_grey))

cv2.imshow("Image1", img_grey)

img = cv2.imread(image_path, 1)

cv2.imshow("Image2", img)

img = cv2.imread(image_path, -1)

cv2.imshow("Image3", img)

# Wait for 5 Seconds
cv2.waitKey(5 * 1000)

cv2.imwrite("img_grey.png", img_grey)

# Destroy all the opened windows
cv2.destroyAllWindows()
