from time import sleep



class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, hash(password), age)
            self.users.append(user)
            self.current_user = user

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[self.users.index(nickname)].password == hash(password):
                print(f"Здравствуйте {nickname}!\n")
                self.current_user = self.users[self.users.index(nickname)]
            else:
                print("Пароль не подходит.\n")
        else:
            print(f"Пользователя {nickname} не существует\n")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if isinstance(video, Video):
                if video.title in self.videos:
                    print(f'Видео {video.title} уже было добавлено')
                else:
                    self.videos.append(video)
            else:
                print(f'{video} не видео!')

    def get_videos(self, keyword):
        result = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_name):
        if video_name in self.videos:
            if self.current_user:
                if self.current_user.age >= 18:
                    current_video = self.videos[self.videos.index(video_name)]
                    for i in range(1, current_video.duration+1):
                        print(i, end=' ')
                        sleep(1)
                    print("Конец видео")
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                print("Войдите в аккаунт, чтобы смотреть видео")
        # else:
        #     print(f"Видео {video_name} не найдено.")


class Video:
    def __init__(self,  title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other

    def __str__(self):
        return self.nickname



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
