#creating an random word counter dictionary
import sys

filename = sys.argv[1]

infile = open(filename)
worddic = {}

for lines in infile:
    for words in lines.lower().split():
        words = words.strip(",\/;!.~!$#")
        if words not in worddic:
            worddic[words] = 0
        worddic[words] = worddic[words]+1

infile.close()

#print("output for wordcounter:")
f2 = sys.argv[2]
outfile = open(f2,"w")

wordlist = sorted(worddic)
for a in wordlist:
    abc = str(a) + "," + str(worddic[words])
    outfile.write(abc + '\n')
