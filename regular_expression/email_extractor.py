import re

class EmailExtractor:
    def extract(self, text):
        email_regex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+ # nome do usuário
            @ # símbolo @
            [a-zA-Z0-9.-]+ # nome do domínio
            (\.[a-zA-Z]{2,4}) # ponto seguido de outros caracteres
        )''', re.VERBOSE)
        result = email_regex.findall(text)
        return result
        