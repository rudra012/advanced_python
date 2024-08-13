import cv2
import datetime
# Capture using default camera
# it should work with 0 for default and for multiple camera index may change
# Here inplace of 0 we can pass video file path as well
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter.fourcc(*'XVID')
fps = 20
dimension = (640, 480)
output = cv2.VideoWriter("Video.avi", fourcc, fps, dimension)

while cap.isOpened():
    ret, frame = cap.read()
    output.write(frame)
    if ret:
        # text = f"Frame size: {cv2.CAP_PROP_FRAME_WIDTH} * {cv2.CAP_PROP_FRAME_HEIGHT}"
        text = f"Frame size: {cap.get(3)} * {cap.get(4)}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, text, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        text = f"Datetime: {datetime.datetime.now()}"
        frame = cv2.putText(frame, text, (10, 60), font, 1, (0, 0, 255), 2, cv2.LINE_4)

        # Convert video to gray
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # cv2.imshow("Gray Video Frame", gray)
        cv2.imshow("Video Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# Release resources acquired by opencv
cap.release()
cv2.destroyAllWindows()
