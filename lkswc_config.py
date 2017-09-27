main_url = 'https://cab-test7.skyway.capital'
delay = 5
default_browser = 'Chrome'


sum_cashin_small = 50

#Смена языка в ЛК
language_search_xpath = "//DIV[@class='login__header-ul']//SPAN[@href='#']"
switching_to_ru_xpath = "//DIV[@class='login__header-ul']//A[@href='#'][text()='RU']"

#Сворачиваниие дебагпанели
debug_toolbar_xpath = "yii-debug-toolbar"
debug_minimize_xpath = "//span[@class='yii-debug-toolbar-toggler']"

#Авторизация в ЛК
login_field_xpath = "//input[@name='LoginForm[email]']"
passw_field_xpath = "//input[@name='LoginForm[password]']"
login_button_xpath = "//input[@id='buttonLoginSubmit']"
username_xpath = "//h3[@class='personal-card__name personal-card__name_verified']"

#Покупка пакета именное дерево
packet_tree_xpath = "//a[@href='/investment/programs?packet=450']"
main_balance_xpath = "//span[@class='personal-card__table-value-text']"
pay_account_xpath = "//label[@for='pay-w-acc']"
main_account_xpath = "//span[@class='paying__control-label-text']"
total_price_xpath = "//span[@id='total_price']"
input_one_xpath = "//input[@id='input1']"
checkout_tree_xpath = "//div[@class='paying__panel-acc-btn']/input"
progress_start = "//button[@id='progressStart']"
you_select_shares = "Вы собираетесь приобрести следующее количество акций: "
checkbox_icon_xpath = "//span[@class='swc-elements_checkbox-icon']"
button_buy_xpath = "//button[@id='buy-btn']"
verif_data_xpath = "//h3[@class='personal-card__name personal-card__name_verified']"
sign_xpath = "//button[@name='sign']"
requirement_xpath = "//canvas[@id='swc-canvas']"
section_my_certificates = "Мои сертификаты"
checkout_main_section_xpath = "//a[@class='heading-logo-link']"
all_news_xpath = "//a[@class='news__title-link']"

#Переход к пополнению
banking_xpath = "//ul[@class='menu-bar__ul']/li[3]"
deposit_account_xpath = "//ul[@class='menu-bar__ul']/li[3]/div/ul/li[2]"
check_url_cashin = main_url + "/account/cashin"
field_cashin_xpath = "//input[@id='req1']"
deposit_button_xpath = "//button[@id='buttonPay']"

#Пополнение через PERFECT MONEY
ps_perfect_money_xpath = "//div[@id='payment-perfect']"
site_perfect_money = "https://perfectmoney.is/api/step1.asp"
wait_checkout_pm = "//a[@href='https://perfectmoney.is']"

#Пополнение через MERA (Россия, СНГ, Прибалтика)
ps_mera_xpath = "//div[@id='payment-mera']"
popup_checkbox_accept_xpath = "//div[@class='swc-modal-content']/div[3]/label"
mera_success_xpath = "//button[@id='mera-success']"
#сайт cool-pay (mera)
site_mera = "https://lk.cool-pay.com/"
wait_checkout_mera = "//img[@alt='CoolPay']"

#сайт advcash (exmo, ecoin)
site_advcash = "https://wallet.advcash.com/sci/paymentRequest.jsf"
wait_checkout_advcash = "//a[@href='https://advcash.com/']"

#Пополнение через Exmo
ps_exmo_xpath = "//div[@id='payment-adv-exmo']"

#Пополнение через ECOIN
ps_ecoin_xpath = "//div[@id='payment-adv-ecoin']"

#Пополнение через MasterCard (impex)
ps_mc_impex_xpath = "//div[@data-code='impex']"
title_instruction_xpath = "//div[@class='swc-modal-subtitle']"
popup_accept_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[3]/label"
mc_impex_success_xpath = "//button[@id='impex-success']"



