'''here is where we use the questionFile variable
 the below could be rewritten as f = open(questionFile)
 it could also be rewritten as lines = open(questionFile).readlines()# the previous line would require commands like TRY and include error handling so we use WITH
 to take care of common errors.'''
def getlines(usefile, questionFile):
    if usefile: 
        with open(questionFile) as f:
            lines = f.readlines()
            """print(type(lines))
            print(type('Bob'))"""
    else: 
        lines = [ 'Who invented the backwards worm?~Owen', 'Who was a powerful landscaper?~Drew']
    return lines