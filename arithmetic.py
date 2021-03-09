
def arithmetic_arranger(al, solved=False):
    print(solved)
    #num_lines condiitonal on if solved
    # 3 space seperation 
    
    # if solved: 
        #conditional expresion here
    express = {
        'top':[],
        'top_print':'',
        'bottom':[],
        'bottom_print':'',
        'operator':[],
        'width':[],
        'line_print':'',
        'width_sum':0
    }

    if solved: 
        express['results']=[]
        express['results_print']=''

    num_expresions = len(al)
    inter_padding = '    '
    front_top_pad = '  '
    for expresion in al:
        if '-' in expresion or '+' in expresion:
            longest = 0
            sub = expresion.split(' ')
            top = sub[0]
            bottom = sub[2]
            op = sub[1]
            lt = len(top)
            lb = len(bottom)
            express['top'].append(top)
            express['bottom'].append(bottom)
            express['operator'].append(op)
            express['bottom_print']+=(op+' ')
            express['top_print']+= front_top_pad
            if lt > lb:
                pad_bottom =' '*(lt-lb)
                express['top_print']+=str(top)
                express['bottom_print']+= (pad_bottom+str(bottom))
                if lt > longest:
                    longest = lt
            else:
                pad_top = ' '*(lb-lt)
                express['top_print']+= (pad_top+str(top))
                express['bottom_print']+= str(bottom)
                if lb > longest:
                    longest = lb
            express['line_print'] += (('-'*(longest+2))+inter_padding)
            express['width'].append(longest+2)
            express['width_sum']+=longest+2
            print(sub)
            express['top_print']+=inter_padding
            express['bottom_print']+=inter_padding
        else:
            return('Error, not an arithmetic expresion')
    print(express)
    print(longest)
    #white_spacing = 4 
    line_len =  express['width_sum'] + (num_expresions-1)
    print(express['top_print'])
    print(express['bottom_print'])
    print(express['line_print'])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])