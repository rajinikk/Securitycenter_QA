

class Locator(object):


#Nessus_scanner_locator

    _Resources ="Resources"
    _Nessus_scanner = "Nessus Scanners"
    _add = "/html/body/div[1]/section/div/header/div[1]/div/div/div[2]/a[@data-action='add'] "
    _setname = '//*[@id="name-input"]'
    _setDescription  = '//*[@id="description-textarea"]'
    _setHost = '//*[@id="ip-input"]'
    _setport = '//*[@id="port-input"]'
    _entertoggle = '//*[@id="enabled-input"]'
    _setadminusername = '//*[@id="username-input"]'
    _setadminpassword ='//*[@id="password-input"]'
    _clickSubmit = '//a[contains(text(),"Submit")]'
    _agent_toggle_locator = "//*[@id='agentCapable-input']"


#LOGCorrelationEngine
    _lceresource= "Log Correlation Engines"
    _lceAddButton = "/html/body/div[1]/section/div/header/div[1]/div/div/div/a"
    _lceusername = "//*[@id='name-input']"
    _lcedescription = "//*[@id='description-textarea']"
    _lcehost = "//*[@id='host']/span/div/div/div[1]/div[1]/input"
    _lceauthintication = "//*[@id='host']/span/div/div/div[1]/div[2]/button"
    _lcesubmit = "//*[@id='form-overlay-submit']"
#lceclients
    _lceclient_click = "/html/body/div[1]/section/div/header/div[2]/ul/li[6]/a"

