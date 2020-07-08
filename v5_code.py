def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) > 1 and len(names) <= 3:
        result = ""
        for name in names:
            if names.index(name) == len(names) - 1:
                result += " and " + name + " like this"
            elif names.index(name) == len(names) - 2:
                result += name
            else: 
                result += name + ", "
        return result
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
                
        
