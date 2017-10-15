main_url = 'https://cab-test7.skyway.capital'
delay = 10
default_browser = 'Chrome'


sum_cashin_small = 50
sum_cashin_large = 2500
footer_xpath = "//div[@id='footer']"
elem_position_top = "top"
elem_position_bottom = "bottom"


#Смена языка в ЛК
language_search_xpath = "//DIV[@class='login__header-ul']//SPAN[@href='#']"
switching_to_ru_xpath = "//DIV[@class='login__header-ul']//A[@href='#'][text()='RU']"
enter_the_systeme = "//div[@class='login__form-body']/form/h3"

#Сворачиваниие дебагпанели
debug_toolbar_xpath = "yii-debug-toolbar"
debug_minimize_xpath = "//span[@class='yii-debug-toolbar-toggler']"

#Авторизация в ЛК
login_field_xpath = "//input[@name='LoginForm[email]']"
passw_field_xpath = "//input[@name='LoginForm[password]']"
login_button_xpath = "//input[@id='buttonLoginSubmit']"
username_verif_data_xpath = "//h3[@class='personal-card__name personal-card__name_verified']"

#Покупка пакета именное дерево
packet_tree_xpath = "//div[@data-id='450']/div[3]/div/a"
main_balance_xpath = "//span[@class='personal-card__table-value-text']"
package_header_xpath = "//div[@class='package__item-header']"
pay_account_xpath = "//label[@for='pay-w-acc']"
main_account_xpath = "//span[@class='paying__control-label-text']"
total_price_xpath = "//span[@id='total_price']"
input_one_xpath = "//input[@id='input1']"
checkout_tree_xpath = "//div[@id='divStep2']/div[7]/input"
progress_start = "//button[@id='progressStart']"
you_select_shares = "Вы собираетесь приобрести следующее количество акций: "
checkbox_icon_xpath = "//span[@class='swc-elements_checkbox-icon']"
button_buy_xpath = "//button[@id='buy-btn']"
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
ps_ecoin_xpath = "//div[@id='payment-adv-ecoin']/label/div[1]"

#Пополнение через MasterCard (impex)
ps_mc_impex_xpath = "//div[@data-code='impex']"
instruction_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[2]/div"
popup_accept_mc_impex_xpath = "//div[@id='impex-alert']/div/div/div[3]/label"
mc_impex_success_xpath = "//button[@id='impex-success']"

#сайт devcab.trading-impex.com/
wait_checkout_trading_impex = "//button[@id='dropdownMenu1']"
site_trading_impex = "https://devcab.trading-impex.com/auth/login"

#Пополнение через Fasapay
ps_fasapay_xpath = "//div[@id='payment-fasa']"
site_fasapay = "https://sandbox.fasapay.com/sci/"
wait_checkout_fasapay = "//div[@class='lbar1']"

#Пополнение через Impaya (Все страны)
ps_impaya_world_xpath = "//div[@data-code='impeximpaya']"
instruction_impaya_world_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impaya_world_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impaya_world_success_xpath = "//button[@id='impex-tutor-success']"

#Пополнение через impexvisa
ps_impexvisa_xpath = "//div[@data-code='impexvisa']"
instruction_impexvisa_xpath = "//div[@id='impexvisa-alert']/div/div/div[2]/div"
popup_accept_impexvisa_xpath = "//div[@id='impexvisa-alert']/div/div/div[3]/label"
impexvisa_success_xpath = "//button[@id='impexvisa-success']"

#Пополнение через impexorange
ps_impexorange_xpath = "//div[@data-code='impexorange']"
instruction_impexorange_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impexorange_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impexorange_success_xpath = "//button[@id='impex-tutor-success']"

#Пополнение через impexepay
ps_impexepay_xpath = "//div[@data-code='impexepay']"
instruction_impexepay_xpath = "//div[@id='impex-tutor']/div/div/div[2]/div"
popup_accept_impexepay_xpath = "//div[@id='impex-tutor']/div/div/div[3]/label"
impexepay_success_xpath = "//button[@id='impex-tutor-success']"

#Пополнение через web-swift
ps_web_swift_xpath = "//div[@data-payid='4']"
#"//div[@data-code='web-swift']"
#<2500
popup_web_swift_small_xpath = "//div[@id='modalSwiftStep1']/div/div/div/div[2]"
#>=2500
transition_to_payment_swift_xpath = "//h4[@id='currency-choice']"
download_from_verification_swift_xpath = "//a[@id='fill-from-vd']"
accept_swift_xpath = "//form[@id='form-main']/div/div[4]/div[2]/label"
submit_swift_xpath = "//button[@type='submit']"
wait_checkout_swift_page = "//span[@class='label label-danger']"

#Пополнение через Мегаполис
ps_megapolis_xpath = "//div[@data-payid='44']"
choose_the_curr_for_payment = "//div[@id='content']/div[3]/div[2]/h4"

#Пополнение через tt_swift
tt_swift_xpath = "//div[@id='payment-tt']"
choose_val_ru = "//div[@data-val='2']"

#Всплывающее окно свифт
popup_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[1]"
popup_accept_swift_alert_xpath = "//div[@id='swift-alert']/div/div/div[3]/label"
swift_alert_success_xpath = "//button[@id='swift-success']"


all_ps = "//div[@class='paying__panel-item pay-system checkout-button']"