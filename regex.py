number = r'(?:[\-+]?(?:[0-9]*[.,]?[0-9]+)|(?:[0-9]+[.,]?[0-9]*))'
operand = r'(?:[\-+=]|$)'

part = r'(?:(?:(?P<number>{number}) *)|(?:(?:(?P<unknown>{number})? *\*? *(?P<negate_unknown>-)?(?P<is_unknown>x)) *(?:\^ *(?P<power>{number}))?)) *(?P<operand>{op})'.format(number=number, op=operand)
