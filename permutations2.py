def permutations(string, result=[]):

    if len(string) == 1:
        return string
    
    prefix = string[:1]
    suffix = string[1:]

    perms = permutations(suffix)
    perms_this_level = []

    for i in range(len(suffix) + 1):
        for perm in perms:
            new_perm = perm[:i] + prefix + perm[i:]
            perms_this_level.append(new_perm)
    
    return perms_this_level

print(permutations('cat'))