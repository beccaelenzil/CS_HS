def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)
def sq(x):
    """
    output: sq returns x squared
    """
    return x**2
print 'sq(3) is', sq(3)
def interp(low,hi,fraction):
    """
    output:  return the floating-point value that is fraction of the way between low and hi
    """
    return (hi - low)*fraction + low
print 'interp(1,9,.25) is', interp(1,9,.25)
def checkends(s):
    """
    true if the last and first characters of s are the same
    """
    if s[0] == s[-1]:
        return True
    else:
        return False
print 'checkends(shoe) is', checkends('shoe')
print 'checkends(shoes) is', checkends('shoes')
def flipside(s):
    x = len(s)/2
    if len(s)%2 == 0:
        return s[x:] + s[0:x]
    else:
        return s[(len(s)-1)/2:] + s[0:(len(s)-1)/2]
print 'flipside(carpets) is', flipside('carpets')
print 'flipside(homework) is', flipside('homework')
def convertfromseconds(s):
    days = (s - s%86400)/86400
    wodays = s - days*86400
    hours = (wodays - wodays%3600)/3600
    wohours = wodays - hours*3600
    minutes = (wohours - wohours%60)/60
    seconds = wohours - minutes*60
    return [days,hours,minutes,seconds]
print 'convertfromseconds(100000) is', convertfromseconds(100000)
def front3(word):
    front = word[0:3]
    return front + front + front
print 'front3(java) is', front3('java')
def pigletlatin(word):
    first = word[0]
    if len('word') == 0:
        return word
    elif first == 'a' or first =='e' or first == 'i' or first == 'o' or first == 'u':
        return word + 'way'
    else:
        return word[-1] + word[0:-1] + 'ay'
print 'pigletlatin(be) is', pigletlatin('be')
print 'pigletlatin(one) is', pigletlatin('one')
print 'pigletlatin() is', pigletlatin('')

