import cv2 as cv

# ! Resizing Images
img = cv.imread('lenna.png')


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('evermore.mp4')  # parameter int webcam *usually 0
# To show a video we need a loop an show it frame by frame
while True:
    isTrue, frame = capture.read()  # frame + confirmation if frame was read or not

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):  # if letter d is pressed
        break

capture.release()
cv.destroyAllWindows()
