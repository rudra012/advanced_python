import cv2

events = [attr for attr in dir(cv2) if "EVENT" in attr]

# ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON',
#  'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK',
#  'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL',
#  'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
# print(events)

window_name = "Image View"
image_path = "IMG/white_page.png"
img = cv2.imread(image_path, 1)
cv2.imshow(window_name, img)


def mouse_events(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = f"Left Mouse Button: {x}, {y}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (0, 255, 0), 2)
        cv2.imshow(window_name, img)
    if event == cv2.EVENT_RBUTTONDOWN:
        text = f"Right Mouse Button: {x}, {y}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 255), 2)
        cv2.imshow(window_name, img)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        text = f"Mouse Button Double Click: {x}, {y}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow(window_name, img)


cv2.setMouseCallback(window_name, mouse_events)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
