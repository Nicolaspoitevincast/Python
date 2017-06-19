__author__ = 'geoffrey'

mouth = input('Please enter a description of the fishes mouth:   ')

scale = input('Please enter a description of the fishes scale pattern:  ')

tail = input('Please enter a description of the fishes tail "forked" or "not forked" :   ')

mark = input('Please enter a description of the fishes markings:   ')

if mark == 'black line' or mouth == 'large' or tail == 'forked' or scale == 'green':
    print('Snook!')
    print('Season - from Dec. 1 - end of February; May 1 - August 31.')
    print('Size Limit - Not less than 28" total length or more than 33" total length. ')
    print('1 per harvester per day')

if mark == 'black dot' or mark == 'black spot' or mouth == 'small' or tail == 'not forked' or scale == 'red':
    print('Red Fish!')
    print('Size limit - Not less than 18" no more than 27" total length.')
    print('2 fish per person per day; 8 fish vessel limit.')
else:
    print('No fish found matching description.')
