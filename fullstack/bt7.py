#Identifies and counts the different protocols used in the iptablesyslog file.
#python bt7.py iptablesyslog

##!/usr/bin/env python3
import sys

def main():
    protocol = set()
    f = open(sys.argv[1])   #open file
    lines = f.readlines()   #read file
    for l in lines:
        items = l.split(':')
        if items[3].split(' ')[1] == 'OUTBOUND' or items[3].split(' ')[1] == 'INBOUND':
        #the above proves its an ip
            proto = items[3].split(' ')[-1] #this corrects if there is multiple words before protocol
            protocol.add(proto)
    else:
        pass
    print(protocol)
    print(len(protocol))

if __name__ == '__main__':
    main()