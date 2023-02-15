import bleach # mozilla sanitizing user input lib


def str_equals(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for c1, c2 in zip(first_string, second_string):
        if c1 != c2:
            return False

    return True

# facking useless bra
def is_str_empty(str):
    try:
        if len(str) == 0:
            return True

        if not str:
            return True
            
        if str == "":
            return True

        if str is None:
            return True

    except:
        pass

def sanitize(str:str) -> str:
    return bleach.clean(str)