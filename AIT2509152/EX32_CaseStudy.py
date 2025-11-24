import string

def replacePunctuations(line):
    #to get rid of punctuations
    for i in string.punctuation:
        line = line.replace(i, '')
    return line

def processLine(line, wordCounts):
    #getting rid of punctuations
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

def main():
    #user enter the file
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r")

    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)

    pairs = list(wordCounts.items())

    items = [[x, y] for (y, x) in pairs]
    items.sort()

    #to display the top 10 words
    for i in range(len(items) - 1, len(items) - 11, -1):
        print((items[i][1]) + "\t" + str(items[i][0]))

main() #call the main function