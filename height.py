'''

reference : http://www.pyimagesearch.com/2016/04/11/finding-extreme-points-in-contours-with-opencv/

'''
# USAGE
# python extreme_points.py
# import the necessary packages
import imutils
import cv2

def height(name, width=2):
    '''
    To find the height of the person in the image.
    Imputs:
        name: name of the file.
        width: real length of the reference object

    Outputs:
        (nothing yet, displays the topmost, bottom-most points of the body)

    '''
    # load the image, convert it to grayscale, and blur it slightly
    image = cv2.imread(name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold the image, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY_INV,21,8)
    #thresh = cv2.erode(thresh, None, iterations=2)
    #thresh = cv2.dilate(thresh, None, iterations=2)
    # find contours in thresholded image, then grab the largest
    # one
    cv2.imshow('adaptivethreshold',thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
    	cv2.CHAIN_APPROX_NONE)

    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    #removing the contours whose areas is smaller than 20 units
    #this will help in better computaiton.
    remove_smaller_contours = [i for i in cnts if cv2.contourArea(i) >= 20]
    contour = sorted(remove_smaller_contours, key=cv2.contourArea, reverse=True)
    c = contour[0]
    # determine the most extreme points along the contour
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    total_contours = 0

    for c in contour:
        print(cv2.contourArea(c))
        if extLeft > tuple(c[c[:, :, 0].argmin()][0]):
            extLeft = tuple(c[c[:, :, 0].argmin()][0])
        if extRight < tuple(c[c[:, :, 0].argmax()][0]):
            extRight = tuple(c[c[:, :, 0].argmax()][0])
        if extTop[1] > tuple(c[c[:, :, 1].argmin()][0])[1]:
            extTop = tuple(c[c[:, :, 1].argmin()][0])
        if extBot[1] < tuple(c[c[:, :, 1].argmax()][0])[1]:
            extBot = tuple(c[c[:, :, 1].argmax()][0])
        total_contours = total_contours + 1

    print('total contours = ',total_contours)
    # draw the outline of the object, then draw each of the
    # extreme points, where the left-most is red, right-most
    # is green, top-most is blue, and bottom-most is teal
    cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
    cv2.circle(image, extRight, 6, (0, 255, 0), -1)
    cv2.circle(image, extTop, 6, (255, 0, 0), -1)
    cv2.circle(image, extBot, 6, (255, 255, 0), -1)
    cv2.drawContours( image, contour, -1 , (255,0,0),1)

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
