class last_occurrence(object):
    
    def _init_(self, pattern, alphabet):
       
        self.occurrences = dict()
        for  letter  in  alphabet :
            self.occurrences[letter] = pattern.rfind(letter)

    def _call_(self, letter):
        
        return self.occurrences[letter]


def boyer_moore_match(text, pattern):
   
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n  =  len ( text )
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if  j  ==  0 :
                return  i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i  =  i  +  m  -  min ( j , 1 + l )
            j = m - 1 
    return -1



### TEST FUNCTION ###

    if _name_ == '_main_':
        
       def show_match(text, pattern):
        print ('Text:  %s' % text)
        pattern = boyer_moore_match(text, pattern)
        print ( 'Match: %s%s' % ('.'*pattern, pattern))

    text = 'BVRITHYDERABAD COLLEGE OF ENGINEERING FOR WOMEN'
    pattern  =  'FOR'
    show_match(text, pattern)
    show_match(text, pattern + 'e')
