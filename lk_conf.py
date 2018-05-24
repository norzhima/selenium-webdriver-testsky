import lk_priv_data
import random

delay = 40
default_browser = 'Chrome'
#default_browser = 'Firefox'

short_company_name = "SkyWay"
full_company_name = "SkyWay Capital"

# locator_id = "id"
# locator_xpath = "xpath"
logout = "//a[@href='/auth/logout']"

sum_small = 50
sum_large = 2500

#Смена языка в ЛК
language_search_xpath = "//DIV[@class='login__header-ul']//SPAN[@href='#']"
switching_to_ru_xpath = "//DIV[@class='login__header-ul']//A[@href='#'][text()='RU']"
enter_the_systeme_xpath = "//h3[contains(text(), 'Вход в систему')]"

#Сворачиваниие дебагпанели
debug_toolbar_id = "yii-debug-toolbar"
debug_minimize_xpath = "//span[@class='yii-debug-toolbar-toggler']"

#Пополнение через биткоин
ps_bitcoin_id = "payment-bitcoin"
popup_bitcoin_xpath = "//div[@id='modal-bitcoin']/div/div/div[2]/img"
header_bitcoin = "//div[@id ='myModalLabel']"

#сайт advcash (exmo, ecoin)
site_advcash = "https://wallet.advcash.com/sci/paymentRequest.jsf"
wait_checkout_advcash = "//a[@href='https://advcash.com/']"
#Пополнение через advcash
ps_adv_id = "payment-adv"
ps_adv_exmo_id = "payment-adv-exmo"
ps_adv_ecoin_id = "payment-adv-ecoin"
ps_adv_payeer_id = "payment-adv-payeer"
ps_adv_swift_id = "payment-adv-swift"

tab_visa_mastercard = "//a[@href='#psCategory2']"
tab_cryptonator = "//a[@href='#psCategory1']"
tab_swift = "//a[@href='#psCategory3']"
tab_aggregators = "//a[@href='#psCategory4']"
tab_systems = "//a[@href='#psCategory5']"
tab_cash = "//a[@href='#psCategory6']"


#Пополнение через Fasapay
ps_fasapay_id = "payment-fasa"
site_fasapay = "https://sandbox.fasapay.com/sci/"
wait_checkout_fasapay_xpath = "//div[@class='lbar1']"

#Пополнение через impexepay
ps_impex_epay_id = "payment-impex-epay"
instruction_impexepay_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impexepay_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impexepay_success_id = "impex-tutor-success"

#Пополнение через Impaya_world (Все страны)
ps_impex_impaya_world_id = "payment-impex-impaya"
instruction_impaya_world_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impaya_world_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impaya_world_success_id = "impex-tutor-success"

#Пополнение через MasterCard (impex)
ps_impex_mc_id = "payment-impex-mastercard"
instruction_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[2]/div"
popup_accept_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[3]/label"
mc_impex_success_id = "impex-success"

#Пополнение через impex_orange
ps_impex_orange_id = "payment-impex-orange"
instruction_impexorange_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impexorange_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impexorange_success_id = "impex-tutor-success"

#Пополнение через impex_visa
ps_impex_visa_id = "payment-impex-visa"
instruction_impexvisa_xpath = "//div[@id='impexvisa-alert']//div[contains(text(), 'Инструкция по оплате')]"#"//div[@id='impexvisa-alert']/div/div/div[2]/div"
popup_accept_impexvisa_xpath = "//div[@id='impexvisa-alert']/div/div/div[3]/label"
impexvisa_success_id = "impexvisa-success"

#Пополнение через payboutique
ps_impex_payboutique_id = "payment-impex-payboutique"
instruction_impexpayboutique_xpath = "//div[@id='impexpayboutique-alert']//div[contains(text(), 'Инструкция по оплате')]"#"//div[@id='impexvisa-alert']/div/div/div[2]/div"
popup_accept_impexpayboutique_xpath = "//div[@id='impexpayboutique-alert']/div/div/div[3]/label"
impexpayboutique_success_id = "impexpayboutique-success"

#Пополнение через Мегаполис
popup_megapolis_xpath = "//div[@id='agreemodal']"
button_megapolis_xpath = "//a[contains(text(), 'Перейти на сайт для подтверждения')]"
enter_to_megapolis_xpath = "//h1[contains(text(), 'Вход на сайт')]"
site_megapolis = "http://xn----7sbbjhcxbcqidfvkebk5be4i5i.xn--p1ai/login"
megapolis_for_swift_xpath = "//div[@data-href~='Megapolis']"
ps_megapolis_agree_id = "payment-megapolis_agree"
ps_megapolis_id = "payment-megapolis"
#ps_megapolis_agree_xpath = "//div[@id='payment-megapolis_agree']"
id_attr_megapolis = "id"
choose_the_curr_for_payment_xpath = "//div[@id='content']/div[3]/div[2]/h4"

#Пополнение через Тинькофф
popup_tinkoff_id = "agreemodal-tinkoff"
#popup_tinkoff = "//div[@id='agreemodal-tinkoff']"
button_tinkoff_xpath = "//div[@id='agreemodal-tinkoff']//a[contains(text(), 'Перейти на сайт для подтверждения')]"
ps_tinkoff_id = "payment-megapolis_tinkoff"
ps_tinkoff_agree_id = "payment-megapolis_tinkoff_agree"

#Пополнение через MERA(Россия, СНГ, Прибалтика)
ps_mera_id = "payment-mera"
popup_checkbox_accept_xpath = "//div[@class='swc-modal-content']/div[3]/label"
mera_success_xpath = "//button[@id='mera-success']"
#сайт cool-pay (mera)
site_mera = "https://lk.cool-pay.com/"
wait_checkout_mera_xpath = "//img[@alt='CoolPay']"
#Пополнение через Qiwi(Россия, СНГ, Прибалтика)
ps_mera_qiwi_id = "payment-mera-qiwi"
#Пополнение через Euroset(Россия, СНГ, Прибалтика)
ps_mera_euroset_id = "payment-mera-euroset"

#Пополнение через PERFECT MONEY
ps_perfect_money_id = "payment-perfect"
site_perfect_money = "https://perfectmoney.is/api/step1.asp"
wait_checkout_pm_xpath = "//a[@href='https://perfectmoney.is']"

#Пополнение через swift
ps_swift_id = "payment-swift"
#<2500
popup_web_swift_small_xpath = "//div[@id='modalSwiftStep1']/div/div/div/div[2]"
swift_modal_title = "Банковский перевод"
link_in_modal_body = "www.advcash.com"
#Страница заполнения инфойса (swift >=2500, megapolis, ttswift)
transition_to_payment_swift_xpath = "//h4[@id='currency-choice']"
download_from_verification_swift_id = "fill-from-vd"
accept_swift_xpath = "//input[@id='agree']/.."
submit_swift_xpath = "//button[@type='submit']"
wait_checkout_swift_page_xapth = "//span[@class='label label-danger']"
url_swift_invoices =  lk_priv_data.main_url + "/swift/"

#Пополнение через tt_swift
ps_tt_swift_id = "payment-tt"

#Выбор валюты для формы свифта
choose_val_gbp_xpath = "//div[@data-val='1']"
choose_val_ru_xpath = "//div[@data-val='2']"
choose_val_eur_xpath = "//div[@data-val='4']"

#Пополнение через tt_swift
ps_ameria_swift_id = "payment-armenia"
header_page = "//h3[contains(text(), 'Пополнить счет')]"

#Пополнение через webmoney
ps_webmoney_id = "payment-webmoney"
popup_webmoney_xpath = "//div[@id='modal-web-money']"

#Пополнение через cryptonator
ps_cryptonator_id = "payment-cryptonator-cryptonator"
wait_checkout_cryptonator = "//h1[contains(text(), 'First Skyway Invest Group Limited')]"
site_cryptonator = "https://www.cryptonator.com/merchant/invoice"

#Пополнение через cryptonator - все:
ps_cryptonator_bitcoin_id = "payment-cryptonator-bitcoin_crypto"
ps_cryptonator_bitcoincash_id = "payment-cryptonator-bitcoincash"
ps_cryptonator_dash_id = "payment-cryptonator-dash"
ps_cryptonator_dogecoin_id = "payment-cryptonator-dogecoin"
ps_cryptonator_ethereum_id = "payment-cryptonator-ethereum"
ps_cryptonator_litecoin_crypto_id = "payment-cryptonator-litecoin_crypto"
ps_cryptonator_monero_id = "payment-cryptonator-monero"
ps_cryptonator_ripple_id = "payment-cryptonator-ripple"
ps_cryptonator_zcash_id = "payment-cryptonator-zcash"

#ПОКУПКА ПАКЕТОВ
url_checkout_inst = lk_priv_data.main_url + "/investment/instalment?packet=%s"
url_checkout_simple = lk_priv_data.main_url + "/investment/programs?packet=%s"

#Покупка пакета рассрочка 500
#Здесь необходимо заполнить все свойства пакетов, которые собираемся тестировать
packet_instalment_500 = {
 'packet_id':491,
 'choose_packet_xpath':"//div[@data-id='491']/div[3]/div/a",
 'price': 500,
 'count_shares':"//strong[contains(text(), '275 000')]",
 'count_month':9,
 'price_all':5000,
 'instalment':True,
 'pay':'a'
}

#Покупка пакета premium_5000
packet_premium_5000 = {
 'packet_id': 487,
 'choose_packet_xpath':"//div[@data-name='Premium 5 000']//a",
 'count_shares':"//strong[contains(text(), '300 000')]",
 'price_all':5000,
 'instalment':False
}


exp_without_plus = [498, 499, 500, 501]
#Покупка пакета рассрочка старт
first_payment_25_xpath = "//input[@name='package_498'][@data-first_payment='25']/.."
packet_start = {
 'packet_id':498,
 'choose_packet_xpath':"//a[@href='/investment/instalment?packet=498']",
 'price': 25,
 'count_shares':"//strong[contains(text(), '7 750')]",
 'count_month':9,
 'price_all':250,
 'instalment':True
}

exp_with_plus = [502, 503, 504, 505]
#Покупка пакета рассрочка старт +
first_payment_50_xpath = "//input[@name='package_498'][@data-first_payment='50']/.."
packet_start_plus = {
 'packet_id': 502,
 'choose_packet_xpath':"//a[@href='/investment/instalment?packet=502']",
 'price': 50,
 'count_shares':"//strong[contains(text(), '7 750')]",
 'count_month':8,
 'instalment':True,
 'price_all': 250,
}
innotrans_one = {
 'packet_id': 428,
 'choose_packet_xpath': "//a[@href='/investment/programs?packet=428']",
 'count_shares': "//strong[contains(text(), '90 000')]",
 'price_all': 1000,
 'instalment': False,
 'innotrans':True
}

#Выбор метода оплаты:
pay_account_a = {
 'type': "a",
 'pay_from_b':0,
 'pay_from_c':0,
}
pay_account_b = {
 'type':"b",
 'pay_from_a':0,
 'pay_from_c':0,
}
pay_account_c = {
 'type':"c",
 'pay_from_a':0,
 'pay_from_b':0,
}
pay_account_ab = {
 'type':"ab",
 'pay_from_c':0,
 'pay_from_b':5,
}
pay_account_ac = {
 'type': "ac",
 'pay_from_c': 5,
 'pay_from_b': 0,
}
pay_account_bc = {
 'type': "bc",
 'pay_from_a': 0,
 'pay_from_c': 5,
}
pay_account_abc = {
 'type': "abc",
 'pay_from_b': 5,
 'pay_from_c': 5,
}
pay_ameria = {
 'type': "ameria",
}
pay_ameria_xpath = "//div[@data-ps-id='56']"

#Выбор пакета и подписание договора конвертируемого займа
balance_a_xpath = "//div[@data-slider='swcSliceCalculation']//tr[1]//span"
balance_b_xpath = "//div[@data-slider='swcSliceCalculation']//tr[2]//span"
balance_c_xpath = "//div[@data-slider='swcSliceCalculation']//tr[3]//strong"
balance_d_xpath = "//div[@data-slider='swcSliceCalculation']//tr[4]//strong"
pay_w_acc = "//label[@for='pay-w-acc']"
pay_w_ps = "//label[@for='pay-w-ps']"
input_a_id = "input1"
input_b_id = "input2"
input_c_id = "input7"
package_header_xpath = "//div[@class='package__item-header']"
pay_accounts_xpath = "//label[@for='pay-w-acc']"
main_account_xpath = "//span[@class='paying__control-label-text']"
total = "Итого"
total_price_id = "total_price"
checkout_button_xpath = "//div[@class='paying__panel-acc-btn']/input"
progress_start_id = "progressStart"
you_select_shares_xpath = "//div[contains(text(), 'Вы собираетесь приобрести следующее количество акций')]"
checkbox_icon_xpath = "//label[@for='agree']"
button_buy_xpath = "//button[@id='buy-btn'][not(@disabled)]"
sign_xpath = "//button[@name='sign']"

#Рассрочка
url_pay_instalment = lk_priv_data.main_url + "/investment/pay-instalment"
href_my_instalment_xpath = "//div[@id='content']/a"
tab_myinstalment = "//*[@id='divStep1']/div[1]/h2/a"
checkout_myinstalment_xpath = "//h2[contains(text(), 'Мои рассрочки')]"
pay_instalment_xpath = "//h2[contains(text(), 'Мои рассрочки')]"
section_myinstalment = lk_priv_data.main_url + "/investment/myinstalment-not-paid"
select_pay_instalment_xpath = "//select[@class='swc-elements_pay-select swc-elements_pay-select_low instalment-payment-qty']"
schedule_payment_xpath = "//span[@class='myinstalment_description-title']"
month_pay_instalment_xpath = "//select[@class='swc-elements_pay-select swc-elements_pay-select_low instalment-payment-qty']/option[@value='%s']"
last_instalment_xpath = "//div[@class='myinstalment_item ']"
button_for_pay_instalment_xpath = "//button[@data-id='%s']"
name_attr_instalment_id = "data-id"
select_a_or_b = "//select[@id='pay-select%s']"
select_b = "//select[@id='pay-select%s']/option[@value='B']"

#Подписание требования к сертификату
requirement_xpath = "//canvas[@id='swc-canvas']"
section_my_certificates_xpath = "//h2[contains(text(), 'Мои сертификаты')]"
section_my_certificates = "Мои сертификаты"
checkout_main_section_xpath = "//a[@class='heading-logo-link']"
all_news_xpath = "//a[@class='news__title-link']"
url_acceptance_page = lk_priv_data.main_url+"/investment/pay-check"
url_my_certificates = lk_priv_data.main_url + "/investment/portfolio"


#Регистрация
sign_up_xpath = "//a[contains(text(), 'Зарегистрироваться')]"
simple_reg_email = 'simple_reg'
domain_name = "@mail.ru"
field_email_xpath = "//input[@name='email']"
for_phisical_xpath = "//label[@for='register-physical']"
button_sign_up_xpath = "//input[@value='Зарегистрироваться']"
partner_sky_xpath = "//input[@value='SkyWay Capital']"
field_phone_id = "signupform-phone"
phone_code = 7
region_code = 977
field_regname_xpath = "//input[@name='SignupForm[firstname]']"
regname = "name"
username_in_lk = "//h3[contains(text(), '%s')]"
field_reglastname_xpath = "//input[@name='SignupForm[lastname]']"
reglastname = "lastname"
field_reg_password = "//input[@name='SignupForm[password]']"
field_reg_confirmpassword = "//input[@name='SignupForm[confirmpassword]']"
button_reg_signup_xpath = "//input[@value='Зарегистрироваться']"
auth_link_xpath = "//a[contains(text(), 'Авторизоваться')]"
confirm_email_xpath = "//h3[contains(text(), 'Подтвердите свой email')]"
#Почта
login_for_gmail_id = "identifierId"
confirm_auth_button_xpath = "//span[contains(text(), 'Далее')]"#"//span[contains(text(), 'Next')]"#
password_for_gmail_xpath = "//input[@name='password']"
check_new_email_xpath = "//tr[@class='zA zE']"#"Верификация email на SkyWay Capital" //tr[@class='zA zE']//b[contains(text(), 'Верификация email на SkyWay Capital')]Новый вход в личный кабинет new.skyway.capital

link_reg = lk_priv_data.main_url + '/auth/verify-register?code='
new_reg_link_xpath = "//a[@href='mailto:%s']/../a[4]"
reg_link_xpath = "//div[@role='listitem'][last()]//a[contains(@href, '%s')]" % link_reg
registration_completed_xpath = "//a[contains(text(), 'Регистрация завершена')]"
#Модалка, где необходимо выбрать страну и указать город
url_after_reg = lk_priv_data.main_url + "/site/index"
choose_country_modal_xpath = "//select[@id='choose-citizenship-country']"
header_model_citizenship_xpath = "//div[contains(text(), 'Выберите страну и укажите город')]"
field_citizenship_country_id = "choose-citizenship-country"
ru_citizenship_country_xpath = "//select[@id='choose-citizenship-country']/option[contains(text(), 'Россия')]"
field_country_id = "choose-country"
ru_country_xpath = "//select[@id='choose-country']/option[contains(text(), 'Россия')]"
field_city_id = "choose-city"
reg_city = "Moscow"
button_save_id = "save-citizenship"

#Авторизация в ЛК
login_field_xpath = "//input[@name='LoginForm[email]']"
passw_field_xpath = "//input[@name='LoginForm[password]']"
login_button_xpath = "//input[@id='buttonLoginSubmit']"
username_verif_data_xpath = "//h3[@class='personal-card__name js-tooltipster personal-card__name_verified tooltipstered']"
username_non_verified_xpath = "//h3[@class='personal-card__name js-tooltipster personal-card__name_nonVerified tooltipstered']"

#Проверка авторизации
auth = lk_priv_data.main_url + "/auth/login"
enter_email_address = "//span[contains(text(), 'Нужно ввести email')]"
enter_password = "//span[contains(text(), 'Нужно ввести пароль')]"
username_or_password_incorrect = "//span[contains(text(), 'Неверное имя пользователя или пароль. ')]"
email_valid = "//span[contains(text(), 'Значение «Email» не является правильным email адресом.')]"

#Пополнение счета
dep_acc_title_xpath = "//h3[contains(text(), 'Пополнить счет')]"
check_url_cashin = lk_priv_data.main_url + "/account/cashin"
field_cashin_id = "req1"
deposit_button_id = "createInvoice"
pay_invoice_id = "payInvoice"

#Получение списка всех включенных ПС
last_ps_xpath = "//div[last()][@data-code]"
all_ps_xpath = "//div[@data-code]"
name_attribute = 'id'
#name_attribute = 'data-code'
you_were_billed_xpath = "//span[contains(text(), 'Вам был выставлен счет №')]"

#сайт devcab.trading-impex.com/
wait_checkout_trading_impex_id = "dropdownMenu1"
site_trading_impex = "https://devcab.trading-impex.com/auth/login"

#Всплывающее окно свифт
popup_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[1]"
popup_accept_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[3]/label"
swift_alert_success_id = "swift-success"

#Модальное окно по переходу в impex trading
impex_modal_subtitle = "Инструкция по оплате"
impex_modal_body_text = " Счет действителен в течении 3 дней."

#Переход к элементу
footer_xpath = "//div[@id='footer']//div[@class='footer__top']"
select_payment_system = "//div[contains(text(), 'Выберите платежную систему')]"
elem_position_top = "top"
elem_position_bottom = "bottom"

#Разделы ЛК
#Переход к пополнению
banking_section_xpath = "//span[contains(text(), 'Банкинг')]"
deposit_account_section_xpath = "//a[@title='Пополнить счет']"

#Переход к переводу средств
funds_transfer_section_xpath = "//a[@title='Перевод средств']"
#Перевод средств
enter_the_sum_main_id = "sumA"
enter_the_sum_bonus_id = "sumB"
enter_email_recipient_id = "recipient"
input_submit_id = "findrec"
pay1button_id = "pay1button"
recipient_fio_id = "recipient_fio"
confirmation_email_xpath = "//input[@value='email']/.."
funds_transfer_modal_xpath = "//div[@id='myModal']"
funds_code_xpath = "//a[contains(@href, 'mailto:chagdurova1992@mail.ru')]/parent::*"
transfer_success_id = "myModal-success"
input_sms_code_id = "sms-code"
button_sms_code_id = "send-sms-code"

#Переход в раздел верификации
settings_section_xpath = "//span[contains(text(), 'Настройки')]"
verification_section_xpath = "//a[@title='Верификация']"

#Верификация
fill_forms_xpath = "//a[contains(text(), 'Заполнить')]"
#Заполнение формы "Персональные данные"
header_verif_xpath = "//div[@id='verification-steps']"
verif_field_ln_ru_id = "userpersonaldata-last_name"
verif_ln_ru = "ФамилияВ"
verif_field_ln_en_id = "userpersonaldata-last_name_en"
verif_ln_en = "LastnameV"
verif_field_n_ru_id = "userpersonaldata-first_name"
verif_n_ru = "ИмяВ"
verif_field_n_en_id = "userpersonaldata-first_name_en"
verif_n_en = "NameV"
checkbox_female_xpath = "//input[@id='userpersonaldata-gender-female']/.."
select_birthday_id = "userpersonaldata-birthday"
select_birthday_count_xpath = "//select[@id='userpersonaldata-birthday']/option[@value='10']"
select_birthmonth_id = "userpersonaldata-birthmonth"
select_birthmonth_count_xpath = "//select[@id='userpersonaldata-birthmonth']/option[@value='6']"
select_birthyear_id = "userpersonaldata-birthyear"
select_birthyear_count_xpath = "//select[@id='userpersonaldata-birthyear']/option[@value='1990']"
select_birthplace_id = "userpersonaldata-birthplace_country_id"
select_birthplace_country_xpath = "//select[@id='userpersonaldata-birthplace_country_id']/option[@value='4']"
button_next_passport_xpath = "//a[@data-next='passport-data']"
#Заполнение формы "Паспортные данные"
select_persondoc_id = "userpersonaldata-id_type_id"
select_persondoc_type_xpath = "//select[@id='userpersonaldata-id_type_id']/option[@value='1']"
field_persondoc_num_id = "userpersonaldata-id_serial_number"
persondoc_num = "12459565"
select_persondoc_day_id = "userpersonaldata-user_document_day"
select_persondoc_day_count_xpath = "//select[@id='userpersonaldata-user_document_day']/option[@value='10']"
select_persondoc_month_id = "userpersonaldata-user_document_month"
select_persondoc_month_count_xpath = "//select[@id='userpersonaldata-user_document_month']/option[@value='6']"
select_persondoc_year_id = "userpersonaldata-user_document_year"
select_persondoc_year_count_xpath = "//select[@id='userpersonaldata-user_document_year']/option[@value='2013']"
field_persondoc_who_issue_id = "userpersonaldata-id_who_issue"
persondoc_who_issue = "ОУФМС по стране"
button_next_address_xpath = "//a[@data-next='address-data']"
#Заполнение формы "Адрес регистрации"
field_reg_address_xpath = "//input[@id='userpersonaldata-reg_address_en']"
reg_address = "Адрес текущий"
button_finish_xpath = "//a[@data-next='finish']"
select_address_region_id = "userpersonaldata-reg_address_region_id"
select_address_region_count_xpath = "//select[@id='userpersonaldata-reg_address_region_id']/option[@value='5468686']"
select_address_citytype_id = "userpersonaldata-reg_address_city_type_id"
select_address_citytype_count_xpath = "//select[@id='userpersonaldata-reg_address_city_type_id']/option[@value='1']"
select_address_country_xpath = "//select[@id='userpersonaldata-reg_address_country_id']"
field_city_name_id = "userpersonaldata-reg_address_city_name"
city_name = "Название города"
select_address_streettype_id = "userpersonaldata-reg_address_street_type_id"
select_address_streettype_count_xpath = "//select[@id='userpersonaldata-reg_address_street_type_id']/option[@value='3']"
field_address_street_id = "userpersonaldata-reg_address_street_name"
address_street_name = "Молодежная"
field_address_house_id = "userpersonaldata-reg_address_house"
house_number = 20
#Заполнение формы "Загрузка документов"
section_download_xpath = "//h3[contains(text(), 'Загрузка документов')]"
button_choose_xpath = "//span[contains(text(), 'Выбрать')]"
button_download_xpath = "//button[contains(text(), 'Загрузить')]"
upload_confirm_xpath = "//label[@for='upload_confirm_file']"
button_confirm_id = "upload_confirm_file_save"
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

#Запрос на вывод:
#1) добавление реквизитов
req_section_xpath = "//a[@href='/account/settings']"
req_title_section_xpath = "//h2[contains(text(), 'Платежные реквизиты')]"
req_button_add = "opener"
open_mymodal_id = "myModal"
select_req_type_id = "account-type"
select_req_visa_xpath = "//option[@data-code='VISA']"
input_req_number_visa_id = "number"
input_req_name_owner_id = "name"
req_name_owner = "test user"
input_req_expiry_id = "expiry"
req_expiry = 1220
button_add_requisites_id = "sendaccountdata"
added_rows = "(//DIV[@id='wrap']//TABLE)[3]/tbody/tr[%s]"
title_requisites_xpath = "//h2[@class='cabinet__title']"
all_rows_table_requisites_xpath = "(//DIV[@id='wrap']//TABLE)[3]/tbody/tr"
len_td_table_xpath = "(//DIV[@id='wrap']//TABLE)[3]/tbody/tr[1]/td"
#2) переход к заросу на вывод
withdrawal_request_xpath = "//a[@href='/account/cashout']"
count_request_xpath = "//div[@id='w1']//td"
text_del_xpath = "//div[@id='w1']//td[7]"
link_for_delete = "//div[@id='w1']//tr[1]/td[7]"
exp_text_for_del = "Отменить"
data_type_visamaster_xpath = "//input[@data-type-id='4']/parent::*"
input_sum_request_id = "summ"
button_request_id = "pay1button"
last_message_xpath = "//div[@role='listitem'][last()]"
last_rows_table_requisites_xpath = "(//DIV[@id='wrap']//TABLE)[3]/tbody/tr[last()]"
element_with_code_xpath = "//div[@role='listitem'][last()]//div[contains(text(), 'Ваш проверочный код')]"