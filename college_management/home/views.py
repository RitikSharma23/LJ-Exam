from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import pyrebase
from database_config import *



def get_uid_from_access_token(access_token):
    try:
        decoded_token = auth.verify_id_token(access_token)
        uid = decoded_token['uid']
        return uid
    except:
        print('Error verifying access token:')
        return None


def generate_accesstoken(email):
    try:
        user = auth.get_user_by_email(email)
        if user:
            auth_token = auth.create_custom_token(user.uid)
            return JsonResponse({'status':True,'access_token':str(auth_token)})
    except Exception as e:
        print(e)
        return JsonResponse({'status':False})

def home(request):
    return render(request,"home.html",{})


def cnv_json(x):
    try:
        json_data = json.loads(x.decode("utf-8"))
        return json_data
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON data in request body"})
    


@csrf_exempt
def login_with_email_password(request):
    if request.method == "POST":
        x=cnv_json(request.body)
        auth = firebase.auth()
        
        try:
            user = auth.sign_in_with_email_and_password(x['email'], x['password'])
            x=generate_accesstoken(x['email'])
            print(x)
            return x
        except Exception as e:
            print(type(e))
            if (str(e).find("TOO_MANY_ATTEMPTS_TRY_LATER"))!=-1:
                return JsonResponse({"message": "Too Many Login Attempts"})
            elif (str(e).find("INVALID_PASSWORD"))!=-1:
                return JsonResponse({"message": "Invalid Password"})
            else:
                return JsonResponse({"message": "Something went wrong"})


        
            print(str(e).find("INVALID_PASSWORD"))
            return JsonResponse({"message": "Too Many Login Attempts Or Invalid Password"})
            
            
    

