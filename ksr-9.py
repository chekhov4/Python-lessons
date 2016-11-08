def type_value_in_words(value):
    word = ''
    dectas = {
      20: 'twenty',
      30: 'thirty',
      40: 'fourty',
      50: 'fifty',
      60: 'sixty',
      70: 'seventy',
      80: 'eighty',
      90: 'ninety'
        }

    tens = {
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifthteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen',
        }
    digits ={
     1: 'one',
     2: 'two',
     3: 'three',
     4: 'four',
     5: 'five',
     6: 'six',
     7: 'seven',
     8: 'eight',
     9: 'nine'
    }

    word = digits[value // 100] +' '+ 'hundred'
    if value % 100 > 10 and value % 100 < 20:
        word = word + ' ' + tens[value % 100]
    else:
        word = word + ' ' + dectas[((value // 10) % 10) * 10] + ' ' + digits[value % 10]
    print word

    return

if __name__ == '__main__':
    value = 912
    type_value_in_words(value)
