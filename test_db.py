from tinydb import TinyDB, where
from encrypted_json_storage import EncryptedJSONStorage

db = TinyDB(encryption_key="hello", path="./reflect.db", storage=EncryptedJSONStorage)
print(db.all())

db.insert({'type': 'fruit', 'count': 10})
