import socket

lookupList = []
lookupJSON = []
with open('servers.txt', 'rt') as file:
    line = file.readline()
    while line:
        line = line.split(' ')
        if len(line) > 1:
            try:
                newIp = socket.gethostbyname(line[0])
            except socket.SO_ERROR:
                print('Lookup error!')
            if newIp != line[1].strip():
                print(f'[ERROR] {line[0]} IP mismatch: {line[1].strip()} {newIp}')
            lookupList.append(line[0] + ' ' + newIp)
            lookupJSON.append('{\n"' + line[0] +'"' + ' : ' + '"' + newIp + '"\n },')
        line = file.readline()

with open('servers.txt', 'wt') as file:
    for line in lookupList:
        file.write(line + '\n')

with open('servers.json', 'wt') as file:
    for line in lookupJSON:
        file.write(line + '\n')

with open('servers.yaml', 'wt') as file:
    for line in lookupList:
        file.write(line + '\n')


