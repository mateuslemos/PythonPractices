import pyperclip # type: ignore
from phone_number_extractor import PhoneNumberExtractor
from email_extractor import EmailExtractor

# A lib pyperclip tem a função de copiar e colar textos no clipboard do sistema operacional
# O método paste() retorna o texto que está no clipboard
# O método copy() copia um texto para o clipboard

class InformationExtractor:
    def extract(self):
        text = str(pyperclip.paste())
        phone_number_extractor = PhoneNumberExtractor()
        phone_number_list = phone_number_extractor.extract(text)
        matches = []
        for groups in phone_number_list:
            phone_number = '-'.join([groups[1], groups[3], groups[5]])
            if groups[8] != '':
                phone_number += ' x' + groups[8]
            matches.append(phone_number)
        
        email_extractor = EmailExtractor()
        email_list = email_extractor.extract(text)
        for groups in email_list:
            matches.append(groups[0])
        
        return matches
        