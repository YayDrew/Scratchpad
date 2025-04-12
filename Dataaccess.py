def getlines(usefile, questionFile):
    if usefile: 
        # Open the file safely using 'with' so it's closed properly, even if there's an error
        with open(questionFile) as f:
            lines = f.readlines()
    else: 
        # Use a hardcoded fallback list of questions
        lines = [
            'Who invented the backwards worm?~Owen',
            'Who was a powerful landscaper?~Drew'
        ]
    return lines