main_url = 'https://cab-test7.skyway.capital/auth/login'
delay = 5
default_browser = 'Chrome'

login = 'n.chagdurova@skyway.capital'
password = 'Xfulehjdf!1'
username = 'Norzhima Чагдурова'

language_search_xpath = "//input[@name='LoginForm[email]']"
switching_to_ru_xpath = "//input[@name='LoginForm[password]']"
login_field_xpath = "(//BODY[@onload='preload_page()']//INPUT[@class='login__form-control'])[1]"
passw_field_xpath = "(//BODY[@onload='preload_page()']//INPUT[@class='login__form-control'])[2]"
login_button_xpath = "//BODY[@onload='preload_page()']//INPUT[@id='buttonLoginSubmit']"
username_xpath = "//h3[@class='personal-card__name personal-card__name_verified']"