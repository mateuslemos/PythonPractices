import re

#Códigos comuns para classes de caracteres em regex:
# \d - Qualquer dígito de 0 a 9
# \D - Qualquer caractere que não seja um dígito de 0 a 9
# \w - Qualquer letra, dígito ou o caractere underscore (_) (isto é, qualquer caractere alfanumérico)
# \W - Qualquer caractere que não seja uma letra, dígito ou o caractere underscore
# \s - Qualquer caractere de espaço em branco (espaço, tabulação, nova linha)
# \S - Qualquer caractere que não seja um espaço em branco

class RegularExpressionPractice: 
    def __init__(self): 
        self.text = "This is a test about regular expressions"

    def __str__(self):
        return self.text
    
    def is_phone_number(self, text): 
        #
        # O padrão \d corresponde a um dígito (0-9)
        phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
        result = phone_number_regex.search(text)
        if result == None:
            return False
        return True
    
    def __get_bat_regex(self, text): 
        bat_regex = re.compile(r'bat(man|mobile|copter|bat)')
        return bat_regex
    
    def get_bat_first_occurance(self, text): 
        regex = self.__get_bat_regex(text)
        result = regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_bat_second_occurance(self, text): 
        regex = self.__get_bat_regex(text)
        result = regex.search(text)
        if result == None:
            return None
        return result[1]
    
    def get_phone_number(self, text):
        #
        # O padrão ()? corresponde a uma informação que pode ou não estar presente
        phone_number_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
        result = phone_number_regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_batman_in_zero_or_more_occurrences(self, text):
        #
        # O padrão ()* corresponde a uma informação que pode estar presente zero ou mais vezes 
        bat_regex = re.compile(r'bat(wo)*man')
        result = bat_regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_batman_in_one_or_more_occurrences(self, text):
        #
        # O padrão ()+ corresponde a uma informação que pode estar presente uma ou mais vezes 
        bat_regex = re.compile(r'bat(wo)+man')
        result = bat_regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_batman_in_specific_occurrences(self, text):
        #
        # O padrão (){x} corresponde a uma informação que pode estar presente x vezes 
        bat_regex = re.compile(r'bat(wo){2}man')
        result = bat_regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_batman_in_specific_range_occurrences(self, text):
        #
        # O padrão (){x,y} corresponde a uma informação que pode estar presente entre x e y vezes 
        bat_regex = re.compile(r'bat(wo){1,3}man')
        result = bat_regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_batman_in_nongreedy_occurrences(self, text):
        #
        # O padrão (){x,y}? corresponde a uma informação que pode estar presente entre x e y vezes de forma não gananciosa(gulosa)
        # Em outras palavras, o default pega a maior quantidade de caracteres possíveis, enquanto o nongreedy pega a menor quantidade de caracteres possíveis
        bat_regex = re.compile(r'bat(wo){1,3}?man')
        result = bat_regex.search(text)
        if result == None:
            return None
        return result.group()
    
    def get_characters_does_not_match_with_vowel(self, text):
        #
        # O padrão [^aeiou] corresponde a qualquer caractere que não seja uma vogal
        consonant_regex = re.compile(r'[^aeiou]')
        result = consonant_regex.findall(text)
        if result == None:
            return None
        return result
    