from regular_expression_practice import RegularExpressionPractice

regular = RegularExpressionPractice()
print(regular.is_phone_number('334-847-9488'))
print(regular.is_phone_number('334847-9488'))
print(regular.get_bat_first_occurance('batmobile lost a wheel'))
print(regular.get_bat_second_occurance('batmobile lost a wheel'))
print(regular.get_batman_in_zero_or_more_occurrences('batman'))
print(regular.get_batman_in_zero_or_more_occurrences('batwoman'))
print(regular.get_batman_in_zero_or_more_occurrences('batwowoman'))
print(regular.get_batman_in_one_or_more_occurrences('batman'))
print(regular.get_batman_in_one_or_more_occurrences('batwoman'))
print(regular.get_batman_in_one_or_more_occurrences('batwowoman'))