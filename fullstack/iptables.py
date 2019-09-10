#View number of unique ips in a file
#This will change based on which string # contains ips

##!/usr/bin/env python3
import sys

def main():
    ips = set()
    f = open(sys.argv[1])   #open file
    lines = f.readlines()   #read file
    for l in lines: #loop through each line of file
        #print(l.split(' ')) #split each line at the spaces, making a list
        items = l.split(' ')
        if len(items) > 13:
            src = items[11] #denotes source IP as 11th string in list
            src = src.split('=')[1] 
            dst = items[12]
            dst = dst.split('=')[1] #denotes destination IP as 12th string in list
            #print(src, dst)
            ips.add(src)
            ips.add(dst)
            #print(ips)
            #sys.exit()
        else:
            #print(items)
            pass
    print(len(ips))

if __name__ == '__main__':
    main()