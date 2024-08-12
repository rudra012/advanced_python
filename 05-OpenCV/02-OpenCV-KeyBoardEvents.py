import cv2

image_path = "IMG/img.png"
img_grey = cv2.imread(image_path, 0)
cv2.imshow("Image1", img_grey)

# Wa
key = cv2.waitKey(0)

if key == 27:
    # If we press esc key on keyboard close the image window
    cv2.destroyAllWindows()
elif key in [ord("s"), ord("S")]:
    cv2.imwrite("img_grey.png", img_grey)
    cv2.destroyAllWindows()
