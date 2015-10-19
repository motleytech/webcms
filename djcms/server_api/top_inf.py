import os
import subprocess
import json
from pprint import pprint as pp


topEnv = os.environ.copy()
topEnv["COLUMNS"] = "500"

FIELDMAP = {
    'cpu': "%CPU",
    'mem': "%MEM",
    'time': "TIME+",
    'proc': "COMMAND",
}


def compressSpaces(inpString):
    """
    Converts run of multiple consecutive spaces in input string
    into a single space.
    """
    spaceRun = 0
    result = ""
    for char in inpString:
        if char == " ":
            spaceRun += 1
            if spaceRun < 2:
                result += char
        else:
            spaceRun = 0
            result += char
    return result


def splitData(topLine):
    """
    Split top output data, while retaining
    the command in single piece.
    """
    parts = topLine.split(" ")
    result = parts[:11] + [" ".join(parts[11:])]
    return result


def getOutputFromTop():
    """
    Returns the output from top as a string.
    """
    proc = subprocess.Popen(["top", "-c", "-n1", "-b"], stdout=subprocess.PIPE, env=topEnv)

    data = proc.communicate()
    return data[0]


def parseTopOutput(data):
    """
    Separate the data into system info and process info
    Also break the proc info into separate fields for
    later processing.
    """
    dataList = [d.strip() for d in data.strip().split("\n")]

    # system info in the first 5 lines
    sysData = dataList[:5]

    procData = [d for d in dataList[6:] if len(d) > 0]
    procData = map(compressSpaces, procData)
    procData = [splitData(d) for d in procData]

    # PID USER      PR  NI  VIRT
    # RES  SHR S %CPU %MEM
    # TIME+  COMMAND
    order = [1, 8, 9, 4, 5, 6, 10, 11]
    procData = [[d[x] for x in order] for d in procData]

    result = {
        'sysData': sysData,
        'procData': procData,
    }
    return result


def sortData(result, sortField):
    """
    Sort the data based on the sortField.
    """
    if sortField is None or not isinstance(sortField, basestring):
        print "\n\nBad sortField: {}\n\n".format(str(sortField))
        sortField = 'cpu'

    sortField = sortField.lower()
    if sortField not in ('cpu', 'mem', 'proc', 'time'):
        sortField = 'cpu'

    procData = result['procData']

    fieldName = FIELDMAP.get(sortField, '%CPU')
    sortIndex = procData[0].index(fieldName)

    sortedProcData = procData[0] + sorted(procData[1:], key=lambda x: int(x[sortIndex]), reverse=True)

    result['procData'] = sortedProcData

    return result


def getTopData():
    """
    """
    data = getOutputFromTop()
    output = parseTopOutput(data)
    sortedData = sortData(output, 'cpu')

    outJson = json.dumps(sortedData)
    return outJson


if __name__ == '__main__':
    pp(get_top_data())
