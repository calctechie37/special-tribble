from random import random
from collections import OrderedDict

def readFile(spliceData=False):
    try:
        with open('occupations.csv') as file_:
            instream = file_.readlines()
        classPercentages = OrderedDict()
        for line in instream:
            line = line.strip('\r\n')
            percentage = line[line.rfind(',') + 1:]
            jobClass = line[:line.rfind(',')]
            classPercentages[jobClass] = percentage
        return classPercentages
    except (OSError, IOError) as e:
        print "File not found..."
    except Exception:
        print "Unknown error occured"
        
def getOccupation():
    classPercentages = readFile()
    if classPercentages is None:
        print "Error generating dictionary"
        raise SystemExit(0)
    del classPercentages['Total']
    choice = 100 * random()
    beginningValue = 0
    for i in classPercentages:
        value = classPercentages[i]
        try:
            value = float(value)
        except:
            continue
        if choice > beginningValue and choice < (beginningValue + value):
            return i
        beginningValue += value

if __name__ == '__main__':
    result = {}
    for i in xrange(100):
        occupation = getOccupation()
        if occupation in result:
            result[occupation] +=1
        else:
            result[occupation] = 1
    classPercentages = readFile()
    for i in classPercentages:
        print i, classPercentages.get(i), result.get(i)
