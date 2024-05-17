# Functions with Outputs
def format_name(f_name, l_name):
    '''Take a first and last name and format is to return the title case version of them.'''
    if f_name == "" or l_name == "":
        return
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name, l_name



output = format_name(input("What is your first name? "), input("What is your last name? "))
print(output)
