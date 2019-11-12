number = r'(?:[\-+]?(?:[0-9]*[.,]?[0-9]+)|(?:[0-9]+[.,]?[0-9]*))'
operand = r'(?:[\-+=]|$)'


part = r'(?:(?:(?P<number>{number}) *)|(?:(?:(?P<unknown>{number})? *\*? *(?P<negate_unknown>-)?(?P<is_unknown>x)) *(?:\^ *(?P<power>{number}))?)) *(?P<operand>{op})'.format(number=number, op=operand)

test_part = r'(?:(?:(?:{number}) *)|(?:(?:(?:{number})? *\*? *(?:-)?(?:x)) *(?:\^ *(?:{number}))?)) *(?:{op})'.format(number=number, op=operand)
equation = r'^ *(?:{part} *)+'.format(part=test_part)
