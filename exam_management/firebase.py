import firebase_admin
from firebase_admin import credentials,firestore,auth


cred = credentials.Certificate("config.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# email="test@gmail.com"
# password="test123"


# try:
#     user = auth.get_user_by_email(email)
#     print('Successfully signed in user: {0}'.format(user.uid))
# except firebase_admin.auth.UserNotFoundError:
#     print('User not found.')
# except firebase_admin.auth.InvalidPasswordError:
#     print('Invalid password.')



