import cv2 as cv

# ! Reading Images
img = cv.imread('c:/Users/juanc/Documents/PyProyects/Computer-Vision/First Contact/lenna.png')  # reads from this folder

cv.imshow('img', img)  # show the media

cv.waitKey(0)  # wait for a specific delay to press a key (0 is infinite)

# ! Reading Videos
capture = cv.VideoCapture('c:/Users/juanc/Documents/PyProyects/Computer-Vision/First Contact/evermore.mp4')  # parameter int webcam *usually 0
# To show a video we need a loop an show it frame by frame
while True:
    isTrue, frame = capture.read()  # frame + confirmation if frame was read or not
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF == ord('d'): # if letter d is pressed
        break

capture.release()
cv.destroyAllWindows()
