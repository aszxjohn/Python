import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumRegex.search('My Number is 999-888-777')
print('phone number found : ' + mo.group())


'''----------------------------------------------------------------------------------'''


phoneNumRegex_2 = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumRegex_2.search(input('請輸入手機號碼：'))
print('phone number found : ' + mo.group())

'''----------------------------------------------------------------------------------'''