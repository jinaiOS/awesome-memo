from pymongo import MongoClient
from bson import ObjectId

# MongoDB 클라이언트 설정
client = MongoClient('mongodb://localhost:27017/')
db = client['memo_database']
collection = db['memos']

def create_memo(memo):
    result = collection.insert_one(memo)
    return str(result.inserted_id)

def read_memos():
    memos_list = list(collection.find())
    for memo in memos_list:
        memo['_id'] = str(memo['_id'])  # ObjectId를 문자열로 변환
    return memos_list

def update_memo(memo_id, new_content):
    result = collection.update_one({"_id": ObjectId(memo_id)}, {"$set": {"content": new_content}})
    return result.matched_count > 0

def delete_memo(memo_id):
    result = collection.delete_one({"_id": ObjectId(memo_id)})
    return result.deleted_count > 0