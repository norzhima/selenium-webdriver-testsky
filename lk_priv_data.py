main_url = 'https://cab-test7.skyway.capital'
#main_url = 'https://nnew.skyway.capital'
'''
list_username = [
                 ['nikimik741@gmail.com', 'aa1bb2cc', 'Анна Арапова'],
                 ['philipp.d.1988@gmail.com', 'aa1bb2cc', 'Филипп Данкерт'],
                 ['podolskaya.tr@gmail.com', 'aa1bb2cc', 'Яна Подольская'],
                 ['prodplast@yandex.ru', 'aa1bb2cc', 'Виктор Смирнов'],
                 ['ermolova-ol@mail.ru', 'aa1bb2cc', 'Ольга Ермолова'],
                 ['art.dudukchan@yandex.ru', 'aa1bb2cc', 'Артем Дудукчан'],
                 ['york_hsc@inbox.ru', 'aa1bb2cc', 'Александр Цозик'],
                 ['la.soroko@yandex.ru', 'aa1bb2cc', 'Лидия Сороко'],
                 ['zriachew.vlad@yandex.ru', 'aa1bb2cc', 'Владимир Зрячев'],
                 ['Marina_shpaner@mail.ru', 'aa1bb2cc', 'Марина Шпанер'],
                 ['89178645359@mail.ru', 'aa1bb2cc', 'Альбина Ахмадиева'],
                 ['lukoyanov13@mail.ru', 'aa1bb2cc', 'Виктор Лукоянов']
                 ]
'''
login_auth = "n.chagdurova@skyway.capital"

list_ver_user = [
    {'login': 'sanyabc@mail.ru', 'password': 'aa1bb2cc', 'full_name': 'Александр Хухрянский'},
    {'login': 'globalmoney777@gmail.com','password':'aa1bb2cc', 'full_name': 'Алексей Суходоев'},
    {'login': 'n.chagdurova@skyway.capital', 'password': "Xfulehjdf!1", 'full_name': 'Norzhima Чагдурова'},
    {'login': 'ruketkhashieva@gmail.com', 'password': 'aa1bb2cc', 'full_name': 'Рукет Хашиева'},
    {'login': '47maksimova@gmail.com', 'password': 'aa1bb2cc', 'full_name': 'Галина Максимова'},
]

def get_rolled_user():
    while True:
        for user in list_ver_user:
            yield user

user_gen = get_rolled_user()
def get_user():
    return next(user_gen)

reg_password = 'aa1bb2cc'
mail_url = 'https://mail.google.com/mail/u/1/#inbox'
login_for_gmail = "skywaytest2@gmail.com"
password_for_gmail = "testuser2"

#list_for_bd
all_user_id = [207302, 91, 163672, 258454, 258414, 111757, 208320, 243133, 258027, 220610, 257498, 256034, 242815, 257553, 157325, 257394, 257323]

#Верификация
login_for_verif = "chagdurova1992@mail.ru"
passw_for_verif = "aa1bb2cc"
full_name_for_verif = "Norzhima Chagdurova"







