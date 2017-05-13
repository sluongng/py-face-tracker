import cv2
import sys
import os

outPath = os.getcwd() + "\\out"

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# CONST_ScaleFactor Parameter specifying how much the image size is
# reduced at each image scale.
#
# The bigger the number: faster, less precise
#
# Should ALWAYS be greater than 1 (x > 1)
#
# i.e. :
# 1.05 --> each resizing reduce
# cascading window/rectangle size by 5%
#
# Recommended value is 1.05
CONST_ScaleFactor = 1.1

# CONST_MinNeighbors Parameter specifying how many neighbors each
# candidate rectangle should have to retain it.
#
# Recommended value is 3~6
CONST_MinNeighbors = 4

# CONST_MinSize Parameter specifying Minimum possible object size
#
# Recommended value is 30x30
CONST_MinSizeW = 50
CONST_MinSizeH = 50


def detect_face_func(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=CONST_ScaleFactor,
        minNeighbors=CONST_MinNeighbors,
        minSize=(CONST_MinSizeW, CONST_MinSizeH)
    )

    for index, (x, y, w, h) in enumerate(faces):

        # Draw rectangle around detected face
        #
        # cv2.rectangle(
        #     image,
        #     (x, y),
        #     (x + w, y + h),
        #     (0, 255, 0),
        #     2
        # )

        out_name = outPath + "\\face_" + repr(index) + ".jpg"

        # DEBUG
        # print "Writing to " + out_name

        cv2.imwrite(out_name, image[y: y+h, x: x+w])
    return


# Clean up the output folder
def clean_output_directory():
    for file in os.listdir(outPath):
        path = os.path.join(outPath, file)
        try:
            if os.path.isfile(path):
                os.unlink(path)

        except Exception as e:
            print (e)

clean_output_directory()
detect_face_func(sys.argv[1])
