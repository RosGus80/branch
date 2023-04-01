def function(str):
    """My docstring"""
    return str.uppper()

def function2(str):
    """Docstring"""
    list = str.split(" ")
    output = []
    for word in list:
        output.append(word.title())
    return " ".join(output)