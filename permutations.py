def calculate_perms(string, index, result):
    if index == len(string):
        result.append(''.join(string))
        return
    
    for i in range(index, len(string)):
        string[i], string[index] = string[index], string[i]
        calculate_perms(string, index + 1, result)
        string[i], string[index] = string[index], string[i]
    
    return result

def permutations(string):
    if len(string) < 2:
        return string
    string = list(string)
    return calculate_perms(string, 0, [])

print(permutations("boat"))