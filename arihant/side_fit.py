import cv2
import numpy as np
from parts_divide import parts_divide
from matplotlib import pyplot as plt
from cvt_small import cvt_small
from outer import encContour

def give_all_contours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    can=cv2.Canny(gray,120,200)
    closing=cv2.morphologyEx(can,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8),iterations=1)
    contours,hei=cv2.findContours(closing.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    return contours


def horizontal_scale(test, reference):
    test_contours = give_all_contours(test)
    reference_contours = give_all_contours(reference)
    test_contour = test_contours[0]
    reference_contour = reference_contours[0]
    t_l=tuple(test_contour[test_contour[:,:,0].argmin()][0])
    t_r=tuple(test_contour[test_contour[:,:,0].argmax()][0])
    r_l=tuple(reference_contour[reference_contour[:,:,0].argmin()][0])
    r_r=tuple(reference_contour[reference_contour[:,:,0].argmax()][0])

    for test_contour in test_contours:
        if t_l[0] > tuple(test_contour[test_contour[:,:,0].argmin()][0])[0]:
            t_l = tuple(test_contour[test_contour[:,:,0].argmin()][0])
        if t_r[0] < tuple(test_contour[test_contour[:,:,0].argmax()][0])[0]:
            t_r = tuple(test_contour[test_contour[:,:,0].argmax()][0])

    for reference_contour in reference_contours:
        if r_l[0] > tuple(reference_contour[reference_contour[:,:,0].argmin()][0])[0]:
            r_l = tuple(reference_contour[reference_contour[:,:,0].argmin()][0])
        if t_r[0] < tuple(reference_contour[reference_contour[:,:,0].argmax()][0])[0]:
            r_r=tuple(reference_contour[reference_contour[:,:,0].argmax()][0])

    test_size = float(t_r[0] - t_l[0])
    reference_size = float(r_r[0] - r_l[0])
    '''
    print('total test_contour = ',len(test_contours))
    print('total reference = ',len(reference_contours))
    print('test size = ', test_size)
    print('reference size = ', reference_size)
    print('horizontal scale = ',(test_size/reference_size))
    '''
    return (test_size/reference_size)


def side_fit(test, reference):
    '''
    Under process

    Inputs:
        test: side view of test image (without head)
        reference: side view of reference image (without head)

    Output:
        test: cropped and resized test image
        reference: final reference image having same height as the test image
    '''
    test_contour = encContour(test)
    reference_contour = encContour(reference)
    test = (np.zeros((test.shape[0],test.shape[1],3), np.uint8)).copy()
    reference = (np.zeros((reference.shape[0],reference.shape[1],3), np.uint8)).copy()

    cv2.drawContours(test, test_contour, -1 ,(255,255,255),1)
    cv2.drawContours(reference, reference_contour, -1 ,(255,255,255),1)

    t_l=tuple(test_contour[test_contour[:,:,0].argmin()][0])
    t_r=tuple(test_contour[test_contour[:,:,0].argmax()][0])
    t_t=tuple(test_contour[test_contour[:,:,1].argmin()][0])
    t_b=tuple(test_contour[test_contour[:,:,1].argmax()][0])
    error = (t_b[1] - t_t[1]) / 100
    test = test[t_t[1] + error :t_b[1], t_l[0]:t_r[0]]

    r_l=tuple(reference_contour[reference_contour[:,:,0].argmin()][0])
    r_r=tuple(reference_contour[reference_contour[:,:,0].argmax()][0])
    r_t=tuple(reference_contour[reference_contour[:,:,1].argmin()][0])
    r_b=tuple(reference_contour[reference_contour[:,:,1].argmax()][0])
    error = (r_b[1] - r_t[1]) / 100
    reference = reference[r_t[1] + error :r_b[1], r_l[0]:r_r[0]]

    height = 700
    test = cvt_small(test, height)
    reference = cvt_small(reference, height)

    '''
    Now divide body in 13 parts
    Reference : http://www.drawinghowtodraw.com/drawing-lessons/drawing-faces-lessons/cc-figure-drawing-anatomy-caricatures.html
    '''

    scaling = horizontal_scale(test[0:(t_b[1] - t_t[1])*1/13, 0: r_b[1] - r_t[1]],
                reference[0:(t_b[1] - t_t[1])*1/13, 0: r_b[1] - r_t[1]])

    reference = cv2.resize(reference,(int(round(reference.shape[1]*scaling)), height))
    '''
    cv2.imshow('reference',reference)
    cv2.imshow('test',test)
    cv2.waitKey(0)
    '''
    return test, reference
