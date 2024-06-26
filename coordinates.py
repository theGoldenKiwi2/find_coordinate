import cv2

# define a function to display the coordinates of
# the points clicked on the image

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x},{y})')

        # put coordinates as text on the image
        cv2.putText(img, f'({x},{y})', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # draw point on the image
        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)


# read the input image
img = cv2.imread('CO_023.jpg')

# create a window
cv2.namedWindow('Point Coordinates')

# bind the callback function to window
cv2.setMouseCallback('Point Coordinates', click_event)

# display the image
while True:
    cv2.imshow('Point Coordinates', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
