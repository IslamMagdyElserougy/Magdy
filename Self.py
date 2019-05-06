# This code detects and calculates how much money is in a turkish coins picture
import numpy as np
import cv2
# Loading the image
img = cv2.imread('coins8.jpg')
# Converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blurring the image
gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
# Applying Hough circle detection to detect circles in image
circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# Creating an array of the circles found and rounding their number
circles = np.uint16(np.around(circles))

# determining the type of the coin based on it's radius
largestRadius = 0
for i in circles[0, :]:
    if largestRadius < i[2]:
        largestRadius = i[2]
print(largestRadius)
change = 0
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    radius = i[2]
    ratio = ((radius * radius) / (largestRadius * largestRadius))

    # incrementing the variable change according to the type of coin detected
    if (ratio >= 0.85):
        change = change + 1
    elif ((ratio >= .68) and (ratio <= 0.85)):
        change = change + 0.5
    elif ((ratio >= 0.60) and (ratio < .68)):
        change = change + 0.25
    elif ((ratio >= 0.40) and (ratio < 0.60)):
        change = change + 0.1
    elif (ratio < 0.40):
        change = change + 0.05

# displaying the text on image
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Total value: " + str("%.2f" % round(change, 2)) + " Turkish Lira"
cv2.putText(img, text, (0, 400), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.imshow("Detected coins", img)
cv2.waitKey()
