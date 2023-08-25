from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from firebasedb import *

# doc_ref = db.collection("usersdbc").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
# user = auth.create_user(email='ritik@gmail.com', password='ritik123')



def get_uid_from_access_token(access_token):
    try:
        decoded_token = auth.verify_id_token(access_token)
        uid = decoded_token['uid']
        return uid
    except:
        print('Error verifying access token:')
        return None

# access_token = 'eyJhbGciOiAiUlMyNTYiLCAidHlwIjogIkpXVCIsICJraWQiOiAiMzE4NTE2MzVhNTZkNDNmYTNhZTg1NzhmNmE5YmM5ZTE1MTc2NTU4NSJ9.eyJpc3MiOiAiZmlyZWJhc2UtYWRtaW5zZGstcjhhNTFAY29sbGVnZS1tYW5hZ2VtZW50LWZmMzhjLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwgInN1YiI6ICJmaXJlYmFzZS1hZG1pbnNkay1yOGE1MUBjb2xsZWdlLW1hbmFnZW1lbnQtZmYzOGMuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCAiYXVkIjogImh0dHBzOi8vaWRlbnRpdHl0b29sa2l0Lmdvb2dsZWFwaXMuY29tL2dvb2dsZS5pZGVudGl0eS5pZGVudGl0eXRvb2xraXQudjEuSWRlbnRpdHlUb29sa2l0IiwgInVpZCI6ICJhTHBwRDN4Z3BqaFN1aWdNdEsyMU5WSEhLUnQxIiwgImlhdCI6IDE2OTI5MzU0MTksICJleHAiOiAxNjkyOTM5MDE5fQ.DDsxL2XoZsjKtj81xgb9nsaf5w-hJqlX0WALPDXK3Z9I2jqqHbdN0CISXoFD_qeYhFntM1ujoyZUn1nGQHbftSij0CV7XvxEu5sLEO82f1S-NAo4r--PYDd-HizmfaYTMejxwLXnsqj9Cnr7cK5z2Y3xYJ1_u2VV-qcDHsaTVDFU5AuyFqo9OiGxAqG1BpWi4iEBQnXyiMKBV5okDBlr470hNyq5fP4TQPWC-TgTilkcnDjyZCb5HCsK_uwg5fO65-qI4ZANM6JSR526AzTXeZKo05H5MeADKagOmsO_oRIVztLSV3b9ZTXyVphAiiubNAkZbfZZYDAOQm6Bvb7amQ'
# uid = get_uid_from_access_token(access_token)


def generate_accesstoken(email):
    try:
        user = auth.get_user_by_email(email)
        access_token = auth.create_custom_token(user.uid)
        

        return access_token
    except:
        print('Error generating access token:')
        return None

email = 'test@gmail.com'



print(generate_accesstoken(email))



# decoded_token = auth.verify_id_token("b'eyJhbGciOiAiUlMyNTYiLCAidHlwIjogIkpXVCIsICJraWQiOiAiMzE4NTE2MzVhNTZkNDNmYTNhZTg1NzhmNmE5YmM5ZTE1MTc2NTU4NSJ9.eyJpc3MiOiAiZmlyZWJhc2UtYWRtaW5zZGstcjhhNTFAY29sbGVnZS1tYW5hZ2VtZW50LWZmMzhjLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwgInN1YiI6ICJmaXJlYmFzZS1hZG1pbnNkay1yOGE1MUBjb2xsZWdlLW1hbmFnZW1lbnQtZmYzOGMuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCAiYXVkIjogImh0dHBzOi8vaWRlbnRpdHl0b29sa2l0Lmdvb2dsZWFwaXMuY29tL2dvb2dsZS5pZGVudGl0eS5pZGVudGl0eXRvb2xraXQudjEuSWRlbnRpdHlUb29sa2l0IiwgInVpZCI6ICJhTHBwRDN4Z3BqaFN1aWdNdEsyMU5WSEhLUnQxIiwgImlhdCI6IDE2OTI5MzU4MjIsICJleHAiOiAxNjkyOTM5NDIyfQ.FSXnzgKHZywuygwdNXq8xUc-Omw0RCjX5Y2wWnQA0uS-F0GyZvbvf1a0CrYLtwJiSgzIzp_i3f4LJ5_qoAJzHPSeDB-xV1R6lXkVWE3VFL02mO55CS6Zxq8eyZsaqYGkzpyLwvx3qUD3lJnLyONTbdyW6T0IgW9aaRr5LCoj5Tnufi_Sgvi8FmSyaa8HomtWm4Se5JNzKDbG52dI4w-9xQPde2o_fW6Yf_lld5NYcHKKldBbj5j_LGZ5EGcx4Zj8XB7TW_H9CwV0yEJG6K6IOl25fK5kKrLQaxV1cAdbf9CKDQ4549R2GPUjaowIPV7hfb8Q1Y_KYgv3BEPEdhL9Wg")
# uid = decoded_token['uid']

# print(decoded_token)


def home(request):
    return render(request,"home.html",{})

def login(request):
    return render(request,"login.html",{})

def post_login(request):
    data=request.GET
    data_str = next(iter(data.keys()))
    data_dict = json.loads(data_str)
    
    email = data_dict.get('email')
    password = data_dict.get('password')
    
    
    mydata={
        'name':'ritik'
    }
    
    return JsonResponse(mydata)









