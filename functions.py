from automate import automate
def remove_extra_spaces(input_string:str):
    words = input_string.split()
    result_string = ' '.join(words)
    return result_string

def remove_extra_Backspaces(input_string:str):
    words = input_string.split()
    result_string = '\n'.join(words)
    return result_string



def strlong(str):
    num = 0
    for i in str:
        num += 1
    
    return num


def custom_replace(string_org, string_old, string_new):
    result = ""
    i = 0
    while i < strlong(string_org):
        if string_org[i:i + strlong(string_old)] == string_old:
            result += string_new
            i += strlong(string_old)
        else:
            result += string_org[i]
            i += 1

    return result




def catch_comments(str):
    results = []
    index_start = -1
    for i in range(strlong(str)):
        if str[i] == '%' and index_start == -1:
            #هنا نجيب الموقع تع اول رمز من التعليق 
            index_start = i
        elif str[i] == '%' and index_start != -1:
            #وهنا تع اخر رمز
            index_end = i
            results.append(str[index_start:index_end + 1])
            #هنا نرجعو لقيمتو الاولى باش يحوس على كومنت اخر
            index_start = -1

    return results

def remove_comments(str:str):
    comments = catch_comments(str)
    for comment in comments:
        str = custom_replace(str,comment,"")
    return str



def numcolone2(tc):
    chfr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ltrM = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ltrm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sep = [';', ',', '(', ')']
    opr = ['*', '/']
    cpr = ['<', '=', '>']
    tri = '_'
    egl = '='
    sub = '-'
    pls = '+'
    dp = ':'
    pnt = '.'
    cmnt = '%'

    if tc in ltrm:
        return 0
    if tc in chfr:
        return 1
    if tc in opr:
        return 2
    if pls == tc:
        return 3
    if sub == tc:
        return 4
    if dp == tc:
        return 5
    if egl == tc:
        return 6
    if tc in cpr:
        return 7
    if cmnt == tc:
        return 8
    if tc in sep:
        return 9
    if pnt == tc:
        return 10
    if tri == tc:
        return 11
    if tc in ltrM:
        return 12

    return 13

def sep_hashtage(cod):
    len_cod = len(cod)
    rslt = ""
    mat = [
        [1, 4, 15, 6, 5, 18, 13, 13, 10, 16, 9, 20, 19, -1],
        [1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1],
        [1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1],
        [-1, 4, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1],
        [-1, 4, -1, -1, 17, -1, -1, -1, -1, -1, 9, -1, -1, -1],
        [-1, 4, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, 10],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 20, -1, -1],
    ]

    i = 0
    ec = 0
    incmr = False

    while i < len_cod:
        print(ec)
        if incmr:
            rslt += cod[i]
        elif cod[i] == '%':
            rslt += '#'
            incmr = True
            rslt += cod[i]
        elif cod[i] == ' ':
            ec = -1
        elif numcolone2(cod[i]) == 13:
            rslt += '#'
            rslt += cod[i]
            ec = -1
        elif (
            i > 1
            and i < len_cod - 1
            and numcolone2(cod[i - 1]) == 1
            and numcolone2(cod[i]) == 3
            and numcolone2(cod[i + 1]) == 1
        ):
            rslt += '#'
            rslt += cod[i]
            rslt += '#'
            rslt += cod[i + 1]
            i += 1
            ec = 14
        elif (
            i > 1
            and i < len_cod - 1
            and numcolone2(cod[i - 1]) != 1
            and numcolone2(cod[i]) == 3
            and numcolone2(cod[i + 1]) == 1
        ):
            rslt += '#'
            rslt += cod[i]
            rslt += cod[i + 1]
            i += 1
            ec = 4
        elif (
            i > 1
            and i < len_cod - 1
            and numcolone2(cod[i - 1]) != 1
            and numcolone2(cod[i]) == 4
            and numcolone2(cod[i + 1]) == 1
        ):
            rslt += '#'
            rslt += cod[i]
            rslt += cod[i + 1]
            i += 1
            ec = 4
        elif (
            i < len_cod - 1
            and numcolone2(cod[i]) == 11
            and (numcolone2(cod[i + 1]) == 0 or numcolone2(cod[i + 1]) == 1)
        ):
            rslt += cod[i]
            rslt += cod[i + 1]
            i += 1
            ec = 1
        elif cod[i] == ' ':
            pass
        elif ec == -1 or mat[ec][numcolone2(cod[i])] == -1:
            ec = 0
            rslt += '#'
            i -= 1
        else:
            rslt += cod[i]
            ec = mat[ec][numcolone2(cod[i])]

        i += 1

    rslt += '#'
    return rslt


def extract_words_between_hashes(input_string):
    words = [word for word in input_string.split('#') if word]
    return words
 

def automate_final(input:str):
    separated_words = sep_hashtage(input)
    words = extract_words_between_hashes(separated_words)
    result = []
    for word in words:
        output = automate(word)
        result.append(output)

    return result

def list_to_string(my_list):
    result_string = '\n'.join(map(str, my_list))
    return result_string


