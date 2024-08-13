import cv2

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
    print(f"Frame size: {cv2.CAP_PROP_FRAME_WIDTH} * {cv2.CAP_PROP_FRAME_HEIGHT}")
    if ret:
        # Convert video to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Gray Video Frame", gray)
        cv2.imshow("Video Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# Release resources acquired by opencv
cap.release()
cv2.destroyAllWindows()
