# Put back imports to function when going to github
def Ethnomed(img_str):
    
    import numpy as np
    from skimage import io
    from cv2 import cv2
    import io as io2
    import base64
    plant_cascade=cv2.CascadeClassifier(r'./localpackage/cascade.xml')
    # plant_cascade=cv2.CascadeClassifier(r'C:\Users\regdi\Documents\reg documents\Miscellaneous\Mark Desperation\ethnomed\localpackage\cascade.xml')

    im_bytes = base64.b64decode(img_str)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plants = plant_cascade.detectMultiScale(gray, 1.3, 5)

    if len(plants) !=0:
        return True
    else:
        return False

# Del
#with open(r"C:\Users\regdi\Documents\reg documents\Miscellaneous\Mark Desperation\raw_img.jpg", "rb") as f:
#    im_bytes = f.read()

#im_b64 = base64.b64encode(im_bytes).decode("utf8")
# Del

#with open("imageToSave.png", "wb") as fh:
#    fh.write(base64.decodebytes(Ethnomed(im_b64)))

    