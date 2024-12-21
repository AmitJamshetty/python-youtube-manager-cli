import json

def load_data():
    try:
        with open('09_error_handling\youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('09_error_handling\youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('\n')
    print('*' * 70)

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video duration: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the index number to be updated: '))

    if 1<= index <= len(videos):
        name = input('Enter vidoe name: ')
        time = input('Enter video duration: ')
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print('Invalid index selected!')

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the index number to be delted: '))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid index selected!')

def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | Choose an option ')
        print('1. List a favourite video ')
        print('2. Add a youtube video ')
        print('3. Update a youtube video details ')
        print('4. Delete a youtube video ')
        print('5. Exit the app ')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _: # for other choice like 6, 7, 8
                print('invalid choice!')

if __name__ == "__main__": # if name of any function in this file is main then execute this instruction.
    main()