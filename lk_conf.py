import lk_priv_data

delay = 15
default_browser = 'Chrome'

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
instruction_impexvisa_xpath = "//div[@id='impexvisa-alert']/div/div/div[2]/div"
popup_accept_impexvisa_xpath = "//div[@id='impexvisa-alert']/div/div/div[3]/label"
impexvisa_success_xpath = "//button[@id='impexvisa-success']"

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
tt_swift_xpath = "//div[@id='payment-tt']"
choose_val_ru = "//div[@data-val='2']"
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

#Авторизация в ЛК
login_field_xpath = "//input[@name='LoginForm[email]']"
passw_field_xpath = "//input[@name='LoginForm[password]']"
login_button_xpath = "//input[@id='buttonLoginSubmit']"
username_verif_data_xpath = "//h3[@class='personal-card__name personal-card__name_verified']"
username_non_verified_xpath = "//h3[@class='personal-card__name personal-card__name_nonVerified']"
#проверка авторизации
auth = lk_priv_data.main_url + "/auth/login"
enter_email_address = "//span[contains(text(), 'Нужно ввести email')]"#"Нужно ввести email"
enter_password = "//span[contains(text(), 'Нужно ввести пароль')]"#"Нужно ввести пароль"
username_or_password_incorrect = "//span[contains(text(), 'Неверное имя пользователя или пароль. ')]"#"Неверное имя пользователя или пароль. "
email_valid = "//span[contains(text(), 'Значение «Email» не является правильным email адресом.')]"#"Значение «Email» не является правильным email адресом."

#Переход к пополнению
banking_xpath = "//span[contains(text(), 'Банкинг')]"
deposit_account_xpath = "//a[@title='Пополнить счет']"
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

#сайт devcab.trading-impex.com/
wait_checkout_trading_impex = "//button[@id='dropdownMenu1']"
site_trading_impex = "https://devcab.trading-impex.com/auth/login"

#Всплывающее окно свифт
popup_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[1]"
popup_accept_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[3]/label"
swift_alert_success_xpath = "//button[@id='swift-success']"

#Модальное окно по переходу в impex trading
impex_modal_subtitle = "Инструкция по оплате"
impex_modal_body_text = " Счет действителен в течении 7 дней."

#Переход к элементу
footer_xpath = "//div[@id='footer']"
select_payment_system = "//div[. = 'Выберите платежную систему']"
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
checkbox_icon_xpath = "//span[@class='swc-elements_checkbox-icon']"
button_buy_xpath = "//button[@id='buy-btn']"
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







