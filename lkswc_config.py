main_url = 'https://cab-test7.skyway.capital'
delay = 5
default_browser = 'Chrome'


sum_cashin = 50


language_search_xpath = "//DIV[@class='login__header-ul']//SPAN[@href='#']"
switching_to_ru_xpath = "//DIV[@class='login__header-ul']//A[@href='#'][text()='RU']"

debug_toolbar_xpath = "yii-debug-toolbar"
debug_minimize_xpath = "//span[@class='yii-debug-toolbar-toggler']"

login_field_xpath = "//input[@name='LoginForm[email]']"
passw_field_xpath = "//input[@name='LoginForm[password]']"
login_button_xpath = "//input[@id='buttonLoginSubmit']"
username_xpath = "//h3[@class='personal-card__name personal-card__name_verified']"

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

banking_xpath = "//ul[@class='menu-bar__ul']/li[3]"
deposit_account = "//ul[@class='menu-bar__ul']/li[3]/div/ul/li[2]"
check_url_cashin = main_url + "/account/cashin"
field_cashin_xpath = "//input[@id='req1']"
