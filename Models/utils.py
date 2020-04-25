import random
import names 
import faker

class Utils:
    def __init__(self):
        self.providers = ['ar_EG','ar_PS','ar_SA','bg_BG','bs_BA','cs_CZ','de_DE','dk_DK','el_GR','en_AU','en_CA','en_GB','en_IN','en_NZ','en_US','es_ES','es_MX','et_EE','fa_IR','fi_FI','fr_FR','hi_IN','hr_HR','hu_HU','hy_AM','it_IT','ja_JP','ka_GE','ko_KR','lt_LT','lv_LV','ne_NP','nl_NL','no_NO','pl_PL','pt_BR','pt_PT','ro_RO','ru_RU','sl_SI','sv_SE','tr_TR']
        self.positions = ['GK','DC','DL','DR','CM','LM','RM','AM','ES','ST']
        self.AttributeType = ['Shoot','Tackle','Pass','Aerial ability','Dribling','Free Kick','Speed','Stamina','Finishing','Mental']

    def getNation(self):
        return random.choice(self.providers)

    def getPosition(self):
        return random.choice(self.positions)
    
    def getName(self,nat=''):
        if not nat:
            nat = random.choice(self.providers)
        return faker.Faker(nat).first_name_male()

    def getSurname(self,nat=''):
        if not nat:
            nat = random.choice(self.providers)
        return faker.Faker(nat).last_name_male()
    
    def getFullName(self,nat=''):
        if not nat:
            nat = random.choice(self.providers)
        return self.getName(nat) + " " + self.getSurname(nat)

    def getDate(self):
        return faker.Faker().date_between(start_date='-40y', end_date='today')
        #return faker.Faker().profile()['birthdate']

    def getAttribute(self):
        return random.choice(self.AttributeType)

    