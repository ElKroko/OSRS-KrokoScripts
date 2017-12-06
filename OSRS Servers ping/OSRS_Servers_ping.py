# Script made by El Kroko
# December 2017

import subprocess
import time
import multiprocessing
import multiprocessing.dummy



def ping_it(hostname):
    #global worlds
    try:
        p = subprocess.check_output(["ping.exe",hostname])
        a = p.split('\n')[-2]
        b = a.split(',')[-1]
        c = b.split()[-1]
        ping = c[:-2]
        worlds.append((ping, hostname.split('.')[0]))
    except subprocess.CalledProcessError, e:
        ping = 'Disconnected'
        worlds.append((ping, hostname.split('.')[0]))

def ping_range(start, end):
    num_threads = 2 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    p.map(ping_it, ['oldschool' + str(i) + '.runescape.com' for i in range(start,end)])

def ping_worlds(values):
    num_threads = 2 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    p.map(ping_it, ['oldschool' + str(i) + '.runescape.com' for i in values])

def how_many_worlds(how_many):
    worlds.sort()
    print 'The best '+ how_many + ' worlds to connect are:'
    for elem in worlds[:int(how_many)]:
        ping1, world = elem
        world = world[9:]
        print 'world', world, 'with (', ping1 + ' ms)', 'average.'

worlds = list()

if __name__ == '__main__':

    type_worlds = {'p2p': {91, 90, 89, 88, 87, 86, 78, 77, 76, 75, 74, 73, 70, 69, 68, 67, 66, 65, 62, 61, 60,
                           59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38,
                           36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 24, 23, 22, 21, 20, 19, 18, 17, 15, 14, 13, 12,
                           11, 10, 9, 7, 6, 5, 4, 3, 2},
                   'f2p': {85, 94, 93, 1, 83, 84, 35, 81, 82, 16, 26, 8},
                   'pvp': {37, 25, 92}
                   }

    worldtype = raw_input("Please write the type of world you're searhcing for: ")
    print '***Pinging ***'
    t = time.time()
    help = False
    worlds = list()
    if worldtype == 'help':
        help = True

    while help :
        print 'The avaliable options are: f2p, p2p, pvp'
        worldtype = raw_input("Please write the type of world you're searhcing for: ")
        help = False
    if worldtype != '':
        ping_worlds(type_worlds[worldtype])
    else:
        ping_range(1, 99)

    how_many = raw_input('How many worlds do you want to display? ')
    how_many_worlds(how_many,worlds)

    print 'The program finished in ', time.time()- t ,'seconds.'
    print 'Happy Scaping!'
