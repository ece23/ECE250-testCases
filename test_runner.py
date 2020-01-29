import subprocess
import platform
import sys

NLC = '\\n'


def getTestFilesAsList(folder):
    if platform.system() == 'Windows':
        ls = subprocess.run(['dir', folder], stdout=subprocess.PIPE)
    else:
        ls = subprocess.run(['ls', folder], stdout=subprocess.PIPE)
    files = str(ls.stdout).lstrip("b'").rstrip("'").replace('\\t', ' ').replace('\\n', ' ').split()
    outFiles = filter(lambda file: file[-4:] == '.out', files)
    inFiles = filter(lambda file: file[-3:] == '.in', files)
    testFiles = {'inFiles': [], 'outFiles': []}
    for file in inFiles:
        testFiles['inFiles'].append(folder + '/' + file)
    for file in outFiles:
        testFiles['outFiles'].append(folder + '/' + file)

    return testFiles

program = sys.argv[1]
testFolder = sys.argv[2]

testFiles = getTestFilesAsList(testFolder)

for testNumber in range(len(testFiles['inFiles'])):
    with open(testFiles['inFiles'][testNumber], 'r') as inFile:
        completedProcess = subprocess.run([program], stdin=inFile, stdout=subprocess.PIPE)

    output = str(completedProcess.stdout).lstrip("b'").rstrip("'")
    # print(output)
    output = output.split(NLC)

    with open(testFiles['outFiles'][testNumber], 'r') as outFile:
        for line in output:
            expectedOutput = outFile.readline().strip()
            if expectedOutput != line:
                print('Expected: ', expectedOutput)
                print('Recieved: ', line)
                print('Are equal: ', bool(expectedOutput == line))
                print('Exiting...')
    print(f'test {testNumber} passed')
print('All tests passed')


