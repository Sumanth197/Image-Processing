#!/usr/bin/python

# Standard imports
import cv2
import math
import numpy as np;

# Read image
im = cv2.imread("org1.png", cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 150

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


points=[]
# Detect blobs.
keypoints = detector.detect(im)
for i in range(len(keypoints)):
	x=keypoints[i].pt[0]
	y=keypoints[i].pt[1]
	#x = math.floor(keypoints[i].pt[0])
	#y = math.floor(keypoints[i].pt[1])
	points.append(x)
	points.append(y)

result=[]
for i in range(0,len(points),2):
	result.append((points[i], points[i+1]))

#print result

#Assume center = (202,57)

contour_length = []

for i in range(0,len(points),2):
	l1 = (points[i]-202)**2
	l2 = (points[i+1]-57)**2
	length = math.sqrt(l1+l2)
	contour_length.append(length)
	
contour_length.sort()
print contour_length

#Six Nearest Neighbours

six_nearest = []
for i in range(0,6):
	six_nearest.append(contour_length[i])

print six_nearest


# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

