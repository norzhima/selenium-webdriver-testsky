main_url = 'https://app02-newlk02.skyway.capital'
#main_url = "https://stage-newlk.skyway.capital/"

list_ver_user_additional = [
    {'login': 'prodplast@yandex.ru', 'password': 'aa1bb2cc', 'full_name': 'Виктор Смирнов'},
    {'login': 'globalmoney777@gmail.com', 'password': 'aa1bb2cc', 'full_name': 'Алексей Суходоев'}
]

login_auth = "n.chagdurova@skyway.capital"

list_ver_user = [
    {'login': 'sanyabc@mail.ru', 'password': 'aa1bb2cc', 'full_name': 'Александр Хухрянский'},
    {'login': 'nikimik741@gmail.com','password':'aa1bb2cc', 'full_name': 'Анна Арапова'},
    {'login': 'lukoyanov13@mail.ru', 'password':'aa1bb2cc', 'full_name': 'Виктор Лукоянов'},
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
password_for_gmail = "96v8mdgw5jyco9w5ask"

#list_for_bd
users_for_password = (163672, 111757, 257323, 258414, 258454, 91, 258027)
users_for_accounts = (207302, 209424, 163672, 111757, 257323, 258414, 258454, 91, 258027)

#Верификация
login_for_verif = "user_for_verif@mail.ru"
passw_for_verif = "aa1bb2cc"
full_name_for_verif = "Testfirstname Testlastname"

login_for_test = "chagdurova1992@mail.ru"
passw_for_test = "y/xfulehjdf903skyway"
full_name_for_test = "Norzhima Chagdurova"

email_recipient = "n.chagdurova@skyway.capital"
full_recipient = "Norzhima Чагдурова (n.chagdurova@skyway.capital)"

#запрос на вывод. Добавлние реквизитов
req_number_visa = "4572857489562584"


'''
Подготовка бд к тестам:)
UPDATE `user`
SET user.`auth_key` = 'hHh_hpSzRKqfL-KXn7yC3l6omOns3i9Z'
WHERE id
IN (163672, 111757, 257323, 258414, 258454, 91, 258027);

UPDATE `user`
SET user.`password_hash` = '$2y$13$TLZLb9L9aQbAaZ9T9br/RuxD4JAyRB44OoSh0zyLfGFJ6aDjlWiC.'
WHERE id
IN (163672, 111757, 257323, 258414, 258454, 91, 258027);

update accounts
set sum ='100000.0000'
where user_id in
(207302, 209424, 163672, 111757, 257323, 258414, 258454, 91, 258027)
and type in ('A', 'B', 'C');

INSERT INTO auth_assignment (item_name, user_id) VALUES ('admin', 209424);
INSERT INTO auth_assignment (item_name, user_id) VALUES ('languages', 91);
INSERT INTO auth_assignment (item_name, user_id) VALUES ('languages', 258027);

DELETE FROM user WHERE id = 400000;
DELETE FROM user_to_usertype WHERE id = 500000;

#Создание нового пользователя
INSERT INTO user (id, username, auth_key, password_hash, email, role, status, created_at, updated_at, firstname, lastname, is_entity, phone, partner_id, citizenship_country_id, country_id, 
personal_investments, change_status_notification, mark_delete, verified_phone, verified_register, verified_email, verified_notification, city, special, sw_key, agreement_signed, agent_user, 
is_ba_manager, from_ba_rk, phone_verify_messages_count, allow_sms_about_bonus, allow_info_support, language, name)                                                
VALUES (400000, 'user_for_verif@mail.ru', 'hHh_hpSzRKqfL-KXn7yC3l6omOns3i9Z', '$2y$13$TLZLb9L9aQbAaZ9T9br/RuxD4JAyRB44OoSh0zyLfGFJ6aDjlWiC.', 'user_for_verif@mail.ru', 10, 10, UNIX_TIMESTAMP(), 
UNIX_TIMESTAMP(), 'Testfirstname', 'Testlastname', 0, 799777567425, 1, 1, 1, 0.0000, 0, 0, 0, 1, 1, 0, 'Москва', 0, 0, 0, 0, 0, 0, 1, 1, 1, 13, '');
#Указание статуса пользователя
INSERT INTO user_to_usertype (id, user_id, usertype_id, created_at, accessible_to, current)                                                
VALUES (500000, 400000, 13, UNIX_TIMESTAMP(), 0, 1);

#Удаление верификационных данных пользователя
delete from user_personal_data where user_id = 400000
'''



