import cv2

image_path = "IMG/white_page.png"
img = cv2.imread(image_path, -1)

# Add line to image
img = cv2.line(img, (1, 1), (255, 255), (0, 255, 0), 5)
img = cv2.line(img, (1, 1), (1, 255), (255, 0, 0), 6)
img = cv2.line(img, (1, 255), (255, 255), (0, 0, 255), 7)

# Add arrow to image
img = cv2.arrowedLine(img, (256, 256), (355, 400), (0, 0, 255), 7)

# Add rectangle
img = cv2.rectangle(img, (300, 300), (500, 500), (255, 23, 100), 6)

img2 = cv2.imread(image_path, -1)

# Add filled rectangle
img2 = cv2.rectangle(img2, (300, 300), (500, 500), (255, 23, 100), -1)

# Add circle
img2 = cv2.circle(img2, (200, 200), 40, (255, 1, 1), 10)

font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.putText(img2, "Shailesh Rudra", (100, 100), font, 4,
                   (0, 0, 255), 10, cv2.LINE_AA)

cv2.imshow("Image1", img)
cv2.imshow("Image2", img2)
cv2.waitKey(0)

# Destroy all the opened windows
cv2.destroyAllWindows()
