

def FormErrors(*args):

    message = ''
    for i in args:
        if i.errors:
            message = i.errors.as_text()
    return message
    