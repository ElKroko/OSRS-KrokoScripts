import urllib
import time

def open_link(username):
    return urllib.urlopen('https://crystalmathlabs.com/tracker/update.php?player='+username)

def str_to_username(str):
    str.replace(' ', '_')
    return str

if __name__ == '__main__':
    str = raw_input('Please introduce your username: ')
    username = str_to_username(str)
    period = int (raw_input('Introduce the time period (in minutes): '))
    interval = int(raw_input('Introduce the update interval (in minutes): '))
    global_time = time.time()
    total_time = int(global_time) + 60 * period
    c = period/interval
    for i in range(c):
        open(username)
        print 'UPDATED! -', time.strftime('%H:%M:%S', time.gmtime())
        time.sleep(interval * 60)

    print 'The time period has ended. Happy scaping! '