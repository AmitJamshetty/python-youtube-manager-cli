import sqlite3

connection = sqlite3.connect('10_databse_sqlite3\youtube_videos.db')

cursor = connection.cursor()

# anything written inside ''' ''' will stay in same format
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * from videos") # cursor object hold result data
    print('\n')
    print('*' * 70)
    for row in cursor.fetchall():
        if row == () or []:
            print('Empty videos!')
        else:
            print(row)
    print('*' * 70)

def add_video():
    name = input('Enter video name: ')
    time = input('Enter video duration: ')
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    connection.commit()

def update_video():
    list_all_videos()
    index = int(input('Enter the index of video to be updated: '))
    name = input('Enter video name: ')
    time = input('Enter video duration: ')
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, index))
    connection.commit()

def delete_video():
    list_all_videos()
    index = int(input('Enter the index of video to be deleted: '))
    cursor.execute("DELETE FROM videos WHERE id = ?", (index,)) 
    # use , after index variable bcoz it will take as tuple else DB will not aceept.
    connection.commit()

def main():
    while True:
        print('\nYoutube mangaer app with DB')
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
    connection.close()

if __name__ == "__main__":
    main()