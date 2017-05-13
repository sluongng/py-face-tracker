import cv2
import sys
import os
import json


class ImgSize:
    def __init__(self, w=0, h=0):
        self.width = w
        self.height = h

OUT_PATH = os.path.join(os.getcwd(), "out")

CASC_PATH = "haarcascade_frontalface_default.xml"
FACE_CASCADE = cv2.CascadeClassifier(CASC_PATH)

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
SCALE_FACTOR = 1.1725

# CONST_MinNeighbors Parameter specifying how many neighbors each
# candidate rectangle should have to retain it.
#
# Recommended value is 3~6
MIN_NEIGHBORS = 3

# CONST_MinSize Parameter specifying Minimum possible object size
#
# Recommended value is 30x30
MIN_SIZE = ImgSize(100, 100)


def detect_face_func(image_path):
    out_json = {}

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=SCALE_FACTOR,
        minNeighbors=MIN_NEIGHBORS,
        minSize=(MIN_SIZE.width, MIN_SIZE.height)
    )

    out_json["name"] = os.path.basename(image_path)
    out_json["faces"] = []
    out_json["avg_face_size"] = {}

    face_count = len(faces)
    total_faces_size = ImgSize()

    if face_count > 0:

        for index, (x, y, w, h) in enumerate(faces):

            total_faces_size.width += w
            total_faces_size.height += h

            face_name = "face_" + repr(index) + ".jpg"

            face_json = {}
            face_json["name"] = face_name
            face_json["position"] = {}
            face_json["position"]["x"] = x
            face_json["position"]["y"] = y
            face_json["size"] = {}
            face_json["size"]["width"] = w
            face_json["size"]["height"] = h

            out_json["faces"].append(face_json)

            # Draw rectangle around detected face
            #
            # cv2.rectangle(
            #     image,
            #     (x, y),
            #     (x + w, y + h),
            #     (0, 255, 0),
            #     2
            # )

            out_name = os.path.join(OUT_PATH, face_name)

            # DEBUG
            # print "Writing to " + out_name

            cv2.imwrite(out_name, image[y: y+h, x: x+w])

        out_json["avg_face_size"]["width"] = total_faces_size.width / face_count
        out_json["avg_face_size"]["height"] = total_faces_size.height / face_count

    return json.dumps(out_json)


# Clean up the output folder
def clean_output_directory():
    for file_name in os.listdir(OUT_PATH):
        path = os.path.join(OUT_PATH, file_name)
        try:
            if os.path.isfile(path):
                os.unlink(path)

        except Exception as e:
            print (e)

clean_output_directory()
print detect_face_func(sys.argv[1])
