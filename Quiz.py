from random import shuffle
import sys

print('\n\nYour Quiz Starting...\n\nYour args passed in are:')
for arg in sys.argv: print arg

questionFile=''
if (len(sys.argv)<=1):
 print('\nsys.argv has length of: %s' % len(sys.argv))
 questionFile="mytest.tsv"
 print('You will be tested from questions in the default file: mytest.tsv')
else:
 questionFile=sys.argv[1]
 print('you asked for questions from the file: %s' % sys.argv[1])
with open(questionFile) as f:
    lines = f.readlines()

shuffle(lines)
numRight = 0
wrong = []

numQuestions = int(raw_input("How many questions? "))
try:
 for line in lines[:numQuestions]:
  question, rightAnswer = line.strip().split("\t")
  answer = raw_input(question + ' ')
  if answer.upper().strip() == rightAnswer.upper().strip():
   print('Right!')
   numRight += 1
  else:
   print('No, the answer is %s.' % rightAnswer)
   wrong.append(question)
except:
 raise

print('You got %d right' % (numRight))
if (wrong):
    print('You got these wrong: ')
    for q in wrong:
        print(q)

percentage = ((numRight*1.0)/numQuestions)
percentage = float(percentage * 100.00)
print('\nYour percentage is:   %s' %str(percentage))