import pyperclip # type: ignore
from phone_number_extractor import PhoneNumberExtractor
from email_extractor import EmailExtractor

class InformationExtractor:
    def extract(self):
        text = str(pyperclip.paste())
        phone_number_extractor = PhoneNumberExtractor()
        phone_number_list = phone_number_extractor.extract(text)
        matches = []
        for groups in phone_number_list:
            print(groups)
            phone_number = '-'.join([groups[1], groups[3], groups[5]])
            if groups[8] != '':
                phone_number += ' x' + groups[8]
            matches.append(phone_number)
        
        email_extractor = EmailExtractor()
        email_list = email_extractor.extract(text)
        for groups in email_list:
            print(groups)
            matches.append(groups[0])
        
        return matches
        