
def arithmetic_arranger(al, solved=False):
    # 3 space seperation 
    
    # if solved: 
        #conditional expresion here
    express = {
        'top':[],
        'bottom':[],
        'operator':[],
        'width':[]
    }
    longest = 0
    units = len(al)
    
    for expresion in al:
        if '-' in expresion or '+' in expresion:
            sub = expresion.split(' ')
            top = sub[0]
            bottom = sub[2]
            lt = len(top)
            lb = len(bottom)
            express['top'].append(top)
            express['bottom'].append(bottom)
            express['operator'].append(sub[1])
            if lt > lb:
                if lt > longest:
                    longest = lt
            else:
                 if lb > longest:
                    longest = lb
            express['width'].append(longest+2)
            print(sub)
        else:
            return('Error, not an arithmetic expresion')
    print(express)
    print(longest)
    white_spacing = 4 


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)