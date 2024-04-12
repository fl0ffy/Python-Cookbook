def ispalindrome(s):
    return s.replace(' ','').lower() == s[::-1].replace(' ','').lower()

    
print(ispalindrome('Ten animals I slam in a net'))
print(ispalindrome('Eleven animals I slam in a net'))


def isanagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())


print(isanagram('Listen','Silent'))
print(isanagram('modern','norman'))