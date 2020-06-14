# coding: utf-8
import csv
outputFile = open('output.csv', 'w', newline=")
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'backon', 'bacon'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
