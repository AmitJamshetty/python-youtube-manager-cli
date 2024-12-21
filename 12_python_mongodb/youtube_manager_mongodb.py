from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://amitjamshetty:GPwgMeXd3KvIdFte@youtubemanager.8v0rz.mongodb.net/youtubemanager", tlsallowinvalidcertificates=True)
db = client["youtubemanager"]
video_collection = db["videos"]

def list_all_videos():
    print('\n')
    print('*' * 70)
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    print('*' * 70)

def add_video():
    name = input('Enter video name: ')
    time = input('Enter videos duration: ')
    video_collection.insert_one({"name": name, "time": time})

def update_video():
    list_all_videos()
    index = input('Enter index of video to be updated: ')
    name = input('Enter the updated video name: ')
    time = input('Enter the updated videos duration: ')
    video_collection.update_one(
        {'_id': ObjectId(index)},  # Ensure the index is a valid ObjectId
        {'$set': {'name': name, 'time': time}}  # Correct '$set' syntax
    )

def delete_video():
    list_all_videos()
    index = input('Enter index of to be deleted: ')
    video_collection.delete_one({"_id": ObjectId(index)})

def main():
    while True:
        print('\nYoutube manager app')
        print('1. List all videos')
        print('2. Add video')
        print('3. Update video')
        print('4. Delete video')
        print('5. Exit')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break

if __name__ == "__main__":
    main()