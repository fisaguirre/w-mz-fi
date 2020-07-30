from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         ListField,
                         StringField,
                         EmailField,
                         BooleanField,
                         ReferenceField)

from flask_bcrypt import generate_password_hash, check_password_hash

class Access(EmbeddedDocument):
    user = BooleanField(default=True)
    admin = BooleanField(default=False)

class Users(Document):
    name = StringField(unique=False)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access = EmbeddedDocumentField(Access, default=Access(user=True, admin=False))

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')

    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)
        
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)
