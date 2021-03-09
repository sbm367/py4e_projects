
def arithmetic_arranger(al, solved=False):
    #print(solved)
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
        'results':[],
        'results_print':'',
        'width_sum':0
    }

    num_expresions = len(al)
    inter_padding = '    '
    front_top_pad = '  '
    res_pad = ' '
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
            express['results_print'] += res_pad
            res = 0
            if '-' in expresion : 
                res = int(top)-int(bottom)
            else :
                res = int(top)+int(bottom)
            res = str(res)
            express['results'].append(res)

            conditional_padding = ''
            if lt > lb:
                #pad_bottom =' '*(lt-lb)
                conditional_padding = ' '*(lt-lb)
                express['top_print']+=str(top)
                express['bottom_print']+= (conditional_padding+str(bottom))
                if lt > longest:
                    longest = lt
            else:
                #pad_top = ' '*(lb-lt)
                conditional_padding = ' '*(lb-lt)
                express['top_print']+= (conditional_padding+str(top))
                express['bottom_print']+= str(bottom)
                if lb > longest:
                    longest = lb
            dash = ('-'*(longest+2))


            res_space_num = len(dash)-len(res)-1
            #print('dash',dash,len(dash),'res',res,len(res),'res space',res_space_num)
            res_space = ' '*res_space_num
            express['line_print'] += dash +inter_padding
            express['results_print'] += res_space + res + inter_padding
           
           
            express['width'].append(longest+2)
            express['width_sum']+=longest+2
            #print(sub)
            express['top_print']+=inter_padding
            express['bottom_print']+=inter_padding
        else:
            return('Error, not an arithmetic expresion')
           
    #print(express)
    #print(longest)
    #white_spacing = 4 
    line_len =  express['width_sum'] + (num_expresions-1)

    return_str = express['top_print'] +'\n'+express['bottom_print'] +'\n'+express['line_print']
    #print(express['top_print'])
    #print(express['bottom_print'])
    #print(express['line_print'])
    if solved:
        #print(express['results_print'])
        return_str += ('\n'+express['results_print'])
    
    return return_str

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))