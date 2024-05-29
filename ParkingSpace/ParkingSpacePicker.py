# to locate and save the parking slots
import cv2
import pickle   # to save all the positions of parking spaces

width, height = 107, 48

# if position list is not starting
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)

# initializing position list from 0        
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    # left click to form a rectangle
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    # right click to remove a rectangle    
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:  # save the slot positions and create a pickel file 
        pickle.dump(posList, f)


while True:
    img = cv2.imread('carParkImg.png') #reading the initial image of the whole parking or field of interest
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)