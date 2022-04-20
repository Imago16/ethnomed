def main(request):  
    import firebase_admin
    from firebase_admin import credentials, firestore, storage
    import datetime
    from localpackage.PlantProgramRes import Ethnomed

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'image' in request_json:
        image = request_json['image']
        status = Ethnomed(image)
        return str(status)
    
    elif request_args and 'image' in request_args:
        image = request_args['image']
        status = Ethnomed(image)
        return str(status)
        
    # Firebase Store 
    # cred=credentials.Certificate(r'firebasekey.json')
    # firebase_admin.initialize_app(cred, {
    #     'storageBucket': 'ethnomed-de562.appspot.com'
    # })
    # db = firestore.client()
    
    # bucket = storage.bucket()
    # blob = bucket.blob("raw_img.jpg")
    # image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    