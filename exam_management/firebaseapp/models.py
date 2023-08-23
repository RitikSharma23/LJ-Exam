from django.db import models
from firebase_admin import firestore

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    numb = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        db = firestore.client()
        doc_ref = db.collection('test').document(str(self.pk))
        try:
            doc_ref.set({'name': self.name, 'roll': self.roll, 'numb': self.numb})
        except Exception as e:
            print(f"Error saving data to Firestore: {e}")

