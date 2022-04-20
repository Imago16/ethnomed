import firebase_admin
from firebase_admin import credentials, firestore, storage
import datetime
from localpackage.PlantProgramRes import Ethnomed


def main(request):  

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'image' in request_json:
        image = request_json['image']
        img_str = Ethnomed(image)
        return img_str
    
    elif request_args and 'image' in request_args:
        image = request_args['image']
        img_str = Ethnomed(image)
        return img_str
    

    

if __name__ == "__main__":
    main();
    
    # Firebase Store 
    # cred=credentials.Certificate(r'firebasekey.json')
    # firebase_admin.initialize_app(cred, {
    #     'storageBucket': 'ethnomed-de562.appspot.com'
    # })
    # db = firestore.client()
    
    # bucket = storage.bucket()
    # blob = bucket.blob("raw_img.jpg")
    # image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    