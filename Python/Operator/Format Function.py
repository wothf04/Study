#format() function

#format(123456789, ',') -> '123,456,789' (세자리마다 쉼표(,) 넣기)
#format(123456789, '15') -> '      123456789' (자릿수를 15로 하기)
#format(123456789, '<15') -> '123456789      ' (자릿수를 15로하고 왼쪽 정렬)
#format(123456789, '015') -> '000000123456789' (자릿수를 15로하고 빈 자리 0으로 채우기)
#format(123456789, 'x') -> '75bcd15' (16진수로 표기)
#format(12345.6789, '.2f') -> '12345.68' (소수점 이하 2자리로 실수 표시)
