import  re

string_with_simbol = str(input('Введите строку с символами:'))
simbol = len(re.findall('\W+', string_with_simbol))
if simbol:
    print('Количество спец. символов в строке:', simbol)
else:
    print('Символы не обнаружены')


