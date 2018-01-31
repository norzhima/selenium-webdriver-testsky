from selenium import webdriver
from slacker import Slacker
#line = sys.argv[1]
slack = Slacker('slack_key')
hub = 'http://10.0.3.1:4444/wd/hub' #hub host
#PROXY = "kakawka:ZbhZVEF1@host:65534" # user:pass@IP:PORT
#options = webdriver.ChromeOptions()
#options.add_argument('--proxy-server=http://%s' % PROXY)
wd = webdriver.Remote(
            command_executor=hub,
            desired_capabilities={
                "seleniumProtocol": "WebDriver",
                "browserName": "chrome",
                "maxInstances": "4",  # on hub "docker-compose scale chrome=3"
                "maxSession": "6",
                "version": "any",
                "applicationName": "",
                "platform": "LINUX",
                "chrome.switches": '--proxy-server=kakawka:ZbhZVEF1@host:65534'
            }
)
success = True
print wd
wd.implicitly_wait(120)
wd.set_window_size(1400, 1000)
print "logs in " + hub + "/session/" + wd.session_id + "/log"
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
wd.get('http://icanhazip.com')
wd.save_screenshot('/tmp/open_ip.png')
slack.files.upload('/tmp/open_ip.png', filetype='png', channels='#test_alert')
