import lk_priv_data
import random

delay = 20
default_browser = 'Chrome'
#default_browser = 'Firefox'

short_company_name = "SkyWay"
full_company_name = "SkyWay Capital"


sum_cashin_small = 50
sum_cashin_large = 2500

#Смена языка в ЛК
language_search_xpath = "//DIV[@class='login__header-ul']//SPAN[@href='#']"
switching_to_ru_xpath = "//DIV[@class='login__header-ul']//A[@href='#'][text()='RU']"
enter_the_systeme_xpath = "//h3[contains(text(), 'Вход в систему')]"

#Сворачиваниие дебагпанели
debug_toolbar_id = "yii-debug-toolbar"
debug_minimize_xpath = "//span[@class='yii-debug-toolbar-toggler']"

#Пополнение через биткоин
bitcoin_xpath = "//div[@data-code='bitcoin']"
popup_bitcoin = "//div[@id='modal-bitcoin']/div/div/div[2]/img"
header_bitcoin = "//div[@id ='myModalLabel']"

#сайт advcash (exmo, ecoin)
site_advcash = "https://wallet.advcash.com/sci/paymentRequest.jsf"
wait_checkout_advcash = "//a[@href='https://advcash.com/']"
#Пополнение через Exmo
ps_exmo_xpath = "//div[@id='payment-adv-exmo']"
#Пополнение через ECOIN
ps_ecoin_xpath = "//div[@id='payment-adv-ecoin']/label/div[1]"

#Пополнение через Fasapay
ps_fasapay_xpath = "//div[@id='payment-fasa']"
site_fasapay = "https://sandbox.fasapay.com/sci/"
wait_checkout_fasapay = "//div[@class='lbar1']"

#Пополнение через impexepay
ps_impexepay_xpath = "//div[@data-code='impexepay']"
instruction_impexepay_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impexepay_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impexepay_success_xpath = "//button[@id='impex-tutor-success']"

#Пополнение через Impaya_world (Все страны)
ps_impaya_world_xpath = "//div[@data-code='impeximpaya']"
instruction_impaya_world_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impaya_world_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impaya_world_success_xpath = "//button[@id='impex-tutor-success']"

#Пополнение через MasterCard (impex)
ps_mc_impex_xpath = "//div[@data-code='impex']"
instruction_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[2]/div"
popup_accept_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[3]/label"
mc_impex_success_xpath = "//button[@id='impex-success']"

#Пополнение через impex_orange
ps_impexorange_xpath = "//div[@data-code='impexorange']"
instruction_impexorange_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impexorange_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impexorange_success_xpath = "//button[@id='impex-tutor-success']"

#Пополнение через impex_visa
ps_impexvisa_xpath = "//div[@data-code='impexvisa']"
instruction_impexvisa_xpath = "//div[@id='impexvisa-alert']//div[contains(text(), 'Инструкция по оплате')]"#"//div[@id='impexvisa-alert']/div/div/div[2]/div"
popup_accept_impexvisa_xpath = "//div[@id='impexvisa-alert']/div/div/div[3]/label"
impexvisa_success_xpath = "//button[@id='impexvisa-success']"

#Пополнение через payboutique
ps_impexpayboutique_xpath = "//div[@data-code='impexpayboutique']"
instruction_impexpayboutique_xpath = "//div[@id='impexvisa-alert']//div[contains(text(), 'Инструкция по оплате')]"#"//div[@id='impexvisa-alert']/div/div/div[2]/div"
popup_accept_impexpayboutique_xpath = "//div[@id='impexvisa-alert']/div/div/div[3]/label"
impexpayboutique_success_xpath = "//button[@id='impexvisa-success']"

#Пополнение через Мегаполис
popup_megapolis = "//div[@id='agreemodal']"
button_megapolis = "//a[contains(text(), 'Перейти на сайт для подтверждения')]"
enter_to_megapolis = "//h1[contains(text(), 'Вход на сайт')]"
site_megapolis = "http://xn----7sbbjhcxbcqidfvkebk5be4i5i.xn--p1ai/login"
megapolis_for_swift_xpath = "//div[@data-href~='Megapolis']"
ps_megapolis_xpath = "//div[@data-payid='44']"
choose_the_curr_for_payment = "//div[@id='content']/div[3]/div[2]/h4"

#Пополнение через MERA (Россия, СНГ, Прибалтика)
ps_mera_xpath = "//div[@id='payment-mera']"
popup_checkbox_accept_xpath = "//div[@class='swc-modal-content']/div[3]/label"
mera_success_xpath = "//button[@id='mera-success']"
#сайт cool-pay (mera)
site_mera = "https://lk.cool-pay.com/"
wait_checkout_mera = "//img[@alt='CoolPay']"

#Пополнение через PERFECT MONEY
ps_perfect_money_xpath = "//div[@id='payment-perfect']"
site_perfect_money = "https://perfectmoney.is/api/step1.asp"
wait_checkout_pm = "//a[@href='https://perfectmoney.is']"

#Пополнение через swift
ps_web_swift_xpath = "//div[@data-payid='4']"
#"//div[@data-code='web-swift']"
#<2500
popup_web_swift_small_xpath = "//div[@id='modalSwiftStep1']/div/div/div/div[2]"
swift_modal_title = "Банковский перевод"
link_in_modal_body = "www.advcash.com"
#Страница заполнения инфойса (swift >=2500, megapolis, ttswift)
transition_to_payment_swift_xpath = "//h4[@id='currency-choice']"
download_from_verification_swift_xpath = "//a[@id='fill-from-vd']"
accept_swift_xpath = "//input[@id='agree']/.."
submit_swift_xpath = "//button[@type='submit']"
wait_checkout_swift_page = "//span[@class='label label-danger']"
url_swift_invoices =  lk_priv_data.main_url + "/swift/"

#Пополнение через tt_swift
ps_tt_swift_xpath = "//div[@id='payment-tt']"

#Выбор валюты для формы свифта
choose_val_gbp_xpath = "//div[@data-val='1']"
choose_val_ru_xpath = "//div[@data-val='2']"
choose_val_eur_xpath = "//div[@data-val='4']"

#Пополнение через tt_swift
ps_ameria_swift_xpath = "//div[@data-code='armenia-swift']"

header_page = "//h3[contains(text(), 'Пополнить счет')]"

#Пополнение через webmoney
webmoney_xpath = "//div[@id='payment-webmoney']"
popup_webmoney = "//div[@id='modal-web-money']"

#Пополнение через cryptonator
cryptonator_xpath = "//div[@id='payment-cryptonator-cryptonator']"
wait_checkout_cryptonator = "//h1[contains(text(), 'First Skyway Invest Group Limited')]"
site_cryptonator = "https://www.cryptonator.com/merchant/invoice"

#Покупка пакета именное дерево
packet_tree_xpath = "//div[@data-id='450']/div[3]/div/a"
url_checkout_tree = lk_priv_data.main_url + "/investment/programs?packet=450"
price_tree = 5000
count_shares_tree_xpath = "//strong[contains(text(), '600 000')]"

#Покупка пакета рассрочка 500
packet_instalment_500_xpath = "//div[@data-id='435']/div[3]/div/a"
url_checkout_instalment_500 = lk_priv_data.main_url + "/investment/instalment?packet=435"
price_instalment_500 = 500
count_shares_instalment_500_xpath = "//strong[contains(text(), '575 000')]"
count_month = 9
price_instalment_500_all = 5000

#Регистрация
sign_up_xpath = "//a[contains(text(), 'Зарегистрироваться')]"
simple_reg_email = 'simple_reg'
domain_name = "@mail.ru"
field_email_xpath = "//input[@name='email']"
for_phisical_xpath = "//label[@for='register-physical']"
button_sign_up_xpath = "//input[@value='Зарегистрироваться']"
partner_sky_xpath = "//input[@value='SkyWay Capital']"
field_phone_xpath = "//input[@id='signupform-phone']"
phone_code = 7
region_code = 977
field_regname_xpath = "//input[@name='SignupForm[firstname]']"
regname = "name"
field_reglastname_xpath = "//input[@name='SignupForm[lastname]']"
reglastname = "lastname"
field_reg_password = "//input[@name='SignupForm[password]']"
field_reg_confirmpassword = "//input[@name='SignupForm[confirmpassword]']"
button_reg_signup_xpath = "//input[@value='Зарегистрироваться']"
auth_link_xpath = "//a[contains(text(), 'Авторизоваться')]"
confirm_email_xpath = "//h3[contains(text(), 'Подтвердите свой email')]"

login_for_gmail_xpath = "//input[@id='identifierId']"
confirm_auth_button_xpath = "//span[contains(text(), 'Далее')]"
password_for_gmail_xpath = "//input[@name='password']"
check_new_email_xpath = "//tr[@class='zA zE']"
link_reg = lk_priv_data.main_url + '/auth/verify-register?code='
reg_link_xpath = "//a[contains(@href, '%s')]" % link_reg
registration_completed_xpath = "//a[contains(text(), 'Регистрация завершена')]"


choose_country_modal_xpath = "//select[@id='choose-citizenship-country']"
header_model_citizenshin_xpath = "//div[contains(text(), 'Выберите страну и укажите город')]"
field_citizenship_country_xpath = "//DIV[@id='choose-citizenship-country-modal']//SELECT[@id='choose-citizenship-country']"
ru_citizenship_country_xpath = "//select[@id='choose-citizenship-country']/option[contains(text(), 'Россия')]"
field_country_xpath = "//select[@id='choose-country']"
ru_country_xpath = "//select[@id='choose-country']/option[contains(text(), 'Россия')]"
field_city_xpath = "//input[@id='choose-city']"
reg_city = "Moscow"
button_save_xpath = "//button[@id='save-citizenship']"


#Авторизация в ЛК
login_field_xpath = "//input[@name='LoginForm[email]']"
passw_field_xpath = "//input[@name='LoginForm[password]']"
login_button_xpath = "//input[@id='buttonLoginSubmit']"

username_verif_data_xpath = "//h3[@class='personal-card__name js-tooltipster personal-card__name_verified tooltipstered']"
username_non_verified_xpath = "//h3[@class='personal-card__name js-tooltipster personal-card__name_nonVerified tooltipstered']"
#проверка авторизации
auth = lk_priv_data.main_url + "/auth/login"
enter_email_address = "//span[contains(text(), 'Нужно ввести email')]"
enter_password = "//span[contains(text(), 'Нужно ввести пароль')]"
username_or_password_incorrect = "//span[contains(text(), 'Неверное имя пользователя или пароль. ')]"
email_valid = "//span[contains(text(), 'Значение «Email» не является правильным email адресом.')]"

#Пополнение счета
dep_acc_title_xpath = "//h3[contains(text(), 'Пополнить счет')]"
check_url_cashin = lk_priv_data.main_url + "/account/cashin"
field_cashin_xpath = "//input[@id='req1']"
deposit_button_xpath = "//button[@id='buttonPay']"

#Получение списка всех включенных ПС
last_ps_xpath = "//div[last()][@data-code]"
all_ps_xpath = "//div[@data-code]"
name_attribute = 'data-code'
#list of payment systems
name_bitcoin = 'bitcoin'
name_cryptonator = 'cryptonator'
name_pm = 'perfect-money'
name_mera = 'mera'
name_ecoin = 'adv-cash'
name_exmo = 'adv-cash'
name_mc = 'impex'
name_fasa = 'fasa'
name_impaya = 'impeximpaya'
name_visa = 'impexvisa'
name_payboutique = 'impexvisa'
name_orange = 'impexorange'
name_webmoney = 'web-money'
name_litecoin = 'litecoin'
name_advcash = 'adv-cash'
name_payeer = 'adv-cash'
name_mega = 'impexmega'
name_epay = 'impexepay'
name_swift = 'swift'
name_megapolis = 'web-swift'
name_ttswift = 'tt-swift'
name_ameria = 'armenia-swift'

#сайт devcab.trading-impex.com/
wait_checkout_trading_impex = "//button[@id='dropdownMenu1']"
site_trading_impex = "https://devcab.trading-impex.com/auth/login"

#Всплывающее окно свифт
popup_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[1]"
popup_accept_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[3]/label"
swift_alert_success_xpath = "//button[@id='swift-success']"

#Модальное окно по переходу в impex trading
impex_modal_subtitle = "Инструкция по оплате"
impex_modal_body_text = " Счет действителен в течении 3 дней."

#Переход к элементу
footer_xpath = "//div[@id='footer']//div[@class='footer__top']"
select_payment_system = "//div[contains(text(), 'Выберите платежную систему')]"
elem_position_top = "top"
elem_position_bottom = "bottom"

#Выбор пакета и подписание договора конвертируемого займа
main_balance_xpath = "//span[@class='personal-card__table-value-text']"
package_header_xpath = "//div[@class='package__item-header']"
pay_account_xpath = "//label[@for='pay-w-acc']"
main_account_xpath = "//span[@class='paying__control-label-text']"
total = "Итого"
total_price_xpath = "//span[@id='total_price']"
input_one_xpath = "//input[@id='input1']"
checkout_tree_xpath = "//div[@class='paying__panel-acc-btn']/input"
progress_start_xpath = "//button[@id='progressStart']"
you_select_shares_xpath = "//div[contains(text(), 'Вы собираетесь приобрести следующее количество акций')]"
checkbox_icon_xpath = "//label[@for='agree']"#"//span[@class='swc-elements_checkbox-icon']"
button_buy_xpath = "//button[@id='buy-btn'][not(@disabled)]"
sign_xpath = "//button[@name='sign']"

#Рассрочка
url_pay_instalment = lk_priv_data.main_url + "/investment/pay-instalment"
href_my_installment_xpath = "//div[@id='content']/a"
checkout_myinstalment_xpath = "//h2[contains(text(), 'Мои рассрочки')]"
section_myinstalment = lk_priv_data.main_url + "/investment/myinstalment"
select_pay_instalment_xpath = "//select[@class='swc-elements_pay-select swc-elements_pay-select_low instalment-payment-qty']"
schedule_payment_xpath = "//span[@class='myinstalment_description-title']"
month_pay_instalment_xpath = "//select[@class='swc-elements_pay-select swc-elements_pay-select_low instalment-payment-qty']/option[@value='%s']" % count_month
last_instalment_xpath = "//div[@class='myinstalment_item ']"
name_attr_instalment_id = "data-id"

#Подписание требования к сертификату
requirement_xpath = "//canvas[@id='swc-canvas']"
section_my_certificates_xpath = "//h2[contains(text(), 'Мои сертификаты')]"
section_my_certificates = "Мои сертификаты"
checkout_main_section_xpath = "//a[@class='heading-logo-link']"
all_news_xpath = "//a[@class='news__title-link']"
url_acceptance_page = lk_priv_data.main_url+"/investment/pay-check"
url_my_certificates = lk_priv_data.main_url + "/investment/portfolio"

#Разделы ЛК
#Переход к пополнению
banking_section_xpath = "//span[contains(text(), 'Банкинг')]"
deposit_account_section_xpath = "//a[@title='Пополнить счет']"

#Переход в раздел верификации
settings_section_xpath = "//span[contains(text(), 'Настройки')]"
verification_section_xpath = "//a[@title='Верификация']"

#Верификация
fill_forms_xpath = "//a[contains(text(), 'Заполнить')]"#"//a[@href='/personal']"#
#Заполнение формы "Персональные данные"
header_verif_xpath = "//div[@id='verification-steps']"
verif_field_ln_ru_xpath = "//input[@id='userpersonaldata-last_name']"
verif_ln_ru = "ФамилияВ"
verif_field_ln_en_xpath = "//input[@id='userpersonaldata-last_name_en']"
verif_ln_en = "LastnameV"
verif_field_n_ru_xpath = "//input[@id='userpersonaldata-first_name']"
verif_n_ru = "ИмяВ"
verif_field_n_en_xpath = "//input[@id='userpersonaldata-first_name_en']"
verif_n_en = "NameV"
checkbox_female_xpath = "//input[@id='userpersonaldata-gender-female']/.."
select_birthday_xpath = "//select[@id='userpersonaldata-birthday']"
select_birthday_count_xpath = "//select[@id='userpersonaldata-birthday']/option[@value='10']"
select_birthmonth_xpath = "//select[@id='userpersonaldata-birthmonth']"
select_birthmonth_count_xpath = "//select[@id='userpersonaldata-birthmonth']/option[@value='6']"
select_birthyear_xpath = "//select[@id='userpersonaldata-birthyear']"
select_birthyear_count_xpath = "//select[@id='userpersonaldata-birthyear']/option[@value='1990']"
select_birthplace_xpath = "//select[@id='userpersonaldata-birthplace_country_id']"
select_birthplace_country_xpath = "//select[@id='userpersonaldata-birthplace_country_id']/option[@value='4']"
button_next_passport_xpath = "//a[@data-next='passport-data']"
#Заполнение формы "Паспортные данные"
select_persondoc_xpath = "//select[@id='userpersonaldata-id_type_id']"
select_persondoc_type_xpath = "//select[@id='userpersonaldata-id_type_id']/option[@value='1']"
field_persondoc_num_xpath = "//input[@id='userpersonaldata-id_serial_number']"
persondoc_num = "12459565"
select_persondoc_day_xpath = "//select[@id='userpersonaldata-user_document_day']"
select_persondoc_day_count_xpath = "//select[@id='userpersonaldata-user_document_day']/option[@value='10']"
select_persondoc_month_xpath = "//select[@id='userpersonaldata-user_document_month']"
select_persondoc_month_count_xpath = "//select[@id='userpersonaldata-user_document_month']/option[@value='6']"
select_persondoc_year_xpath = "//select[@id='userpersonaldata-user_document_year']"
select_persondoc_year_count_xpath = "//select[@id='userpersonaldata-user_document_year']/option[@value='2013']"
field_persondoc_who_issue_xpath = "//input[@id='userpersonaldata-id_who_issue']"
persondoc_who_issue = "ОУФМС по стране"
button_next_address_xpath = "//a[@data-next='address-data']"
#Заполнение формы "Адрес регистрации"
field_reg_address_xpath = "//input[@id='userpersonaldata-reg_address_en']"
reg_address = "Адрес текущий"
button_finish_xpath = "//a[@data-next='finish']"
select_address_region_xpath = "//select[@id='userpersonaldata-reg_address_region_id']"
select_address_region_count_xpath = "//select[@id='userpersonaldata-reg_address_region_id']/option[@value='5468686']"
select_address_citytype_xpath = "//select[@id='userpersonaldata-reg_address_city_type_id']"
select_address_citytype_count_xpath = "//select[@id='userpersonaldata-reg_address_city_type_id']/option[@value='1']"
select_address_country_xpath = "//select[@id='userpersonaldata-reg_address_country_id']"
field_city_name_xpath = "//input[@id='userpersonaldata-reg_address_city_name']"
city_name = "Название города"
select_address_streettype_xpath = "//select[@id='userpersonaldata-reg_address_street_type_id']"
select_address_streettype_count_xpath = "//select[@id='userpersonaldata-reg_address_street_type_id']/option[@value='3']"
field_address_street_xpath = "//input[@id='userpersonaldata-reg_address_street_name']"
address_street_name = "Молодежная"
field_address_house_xpath = "//input[@id='userpersonaldata-reg_address_house']"
house_number = 20
#Заполнение формы "Загрузка документов"
section_download_xpath = "//h3[contains(text(), 'Загрузка документов')]"
button_choose_xpath = "//span[contains(text(), 'Выбрать')]"
button_download_xpath = "//button[contains(text(), 'Загрузить')]"
upload_confirm_xpath = "//label[@for='upload_confirm_file']"
button_confirm_xpath = "//button[@id='upload_confirm_file_save']"
#status_ver_after_fill = "На проверке"
#autoit
autoit_title = "Открытие"#"Open"#
autoit_wait = 15
autoit_control_edit = "Edit1"
autoit_image_path = "c{:}{\}users{\}n.chagdurova{\}desktop{\}lk{_}functional{_}test{\}jpg.jpg"#{CAPSLOCK on}#"C{:}{\}Users{\}chagd{\}Desktop{\}lk-tests{\}jpg{.}jpg"#
autoit_control_button = "Button1"
finish_header_verif_xpath = "//h3[contains(text(), 'Ваши данные верификации')]"
personal_list_link = lk_priv_data.main_url + "/personal/list"
#link_download_docs_xpath = "//a[contains(text(), 'Загрузить документы')]"


