#matrix = [[1,-1,-1],
          #[-1,2,-1],
          #[-1,-1,0]]

matrix = [
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

def indexof(inputs:str):
    maj_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    min_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    separator = [";", ",", "(", ")"]
    operator = ["*", "/"]
    comparison = ["<", "=", ">"]
    teret = "_"
    equal = "="
    minus = "-"
    plus = "+"
    doublepoint = ":"
    point = "."
    comment = "%"
    a = "a"
    b = "b"
    c = "c"
    if inputs in min_char:
        return 0
    elif inputs in num:
        return 1
    elif inputs in operator:
        return 2
    elif inputs == plus:
        return 3
    elif inputs == minus:
        return 4
    elif inputs == doublepoint:
        return 5
    elif inputs == equal:
        return 6
    elif inputs in comparison:
        return 7
    elif inputs == comment:
        return 8
    elif inputs in separator:
        return 9
    elif inputs == point:
        return 10
    elif inputs == teret:
        return 11
    elif inputs in maj_char:
        return 12
    else:
        return -1


def type_de_sym(ec):
    rslt = ""
    if ec == 1:
        rslt = "Identificateur"
    elif ec == 4:
        rslt = "Integer"
    elif ec == 5 or ec == 6:
        rslt = "Operation"
    elif ec == 7 or ec == 8:
        rslt = "Float"
    elif ec == 11:
        rslt = "Comment"
    elif ec in [12, 13, 14, 15, 17]:
        rslt = "Operation"
    elif ec == 16:
        rslt = "Separator"
    elif ec == 18:
        rslt = "Separator"
    elif ec == 19:
        rslt = "Keyword"
    # No default case, as it's not needed in Python

    return rslt



def automate(string:str):
    initial_state = 0
    final_state = [1,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20]
    current_state = initial_state
    for i in range(len(string)):
        if indexof(string[i]) != -1:
            if matrix[current_state][indexof(string[i])] != -1 :
                current_state = matrix[current_state][indexof(string[i])]
                if current_state in final_state and string[i] == string[-1]:
                    final_res = type_de_sym(current_state)
                    if current_state == 1:
                        if len(string) > 6:
                            return f"{string} Identificateur Rejected"
                        else:
                            return f"{string} is {final_res}"
                    return f"{string} is {final_res}"
                elif current_state not in final_state and string[i] == string[-1]:
                    print("a")
                    return f"{string} Rejected"    
            else :
                print("b")
                return "There's No Transition Here"
        else:
            print("c")
            return "There's No Transition Here"
        
