number = r'(?:[\-+]?(?:[0-9]*[.,]?[0-9]+)|(?:[0-9]+[.,]?[0-9]*))'
operand = r'(?:[\-+=]|$)'

part = r'(?:(?:(?P<number>{number}) *\*?)? *(?:(?P<unknown>x) *(?:\^ *(?P<power>{number}))?)?) *(?P<operand>{op})'.format(number=number, op=operand)
