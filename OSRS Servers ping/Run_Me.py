from Tkinter import *
import Auto_update_CML
import OSRS_Servers_ping
import time

def auto_update():
    # Open different windows for each function
    s = Tk(screenName='CML Update')

    Label1 = Label(s, text = 'Username')
    Label1.pack()
    e1 = Entry(s)
    e1.pack()
    user = e1.get()


    Label2 = Label(s, text = 'Time Period')
    Label2.pack()
    e2 = Entry(s)
    e2.pack()
    period = e2.get()


    Label3 = Label(s, text = 'Update Interval')
    Label3.pack()
    e3 = Entry(s)
    e3.pack()
    interval = e3.get()
    '''
    button = Button(s, text= 'OK', command = get())
    button.pack()
    '''
    s.mainloop()

    t = time.time()
    username = Auto_update_CML.str_to_username(user)
    global_time = time.time()
    total_time = int(global_time) + 60 * int(period)
    c = int(period) / int(interval)
    for i in range(c):
        open(username)
        print 'UPDATED! -', time.strftime('%H:%M:%S', time.gmtime())
        time.sleep(interval.get() * 60)

    print 'The time period has ended. Happy scaping! '

def server_ping():
    window = Tk(screenName='Server Ping')


    Label1 = Label(window, text = "Type of world you're searhcing for")
    Label1.pack()
    e1 = Entry(window)
    e1.pack()



    Label2 = Label(window, text = 'Worlds to Desplay')
    Label2.pack()
    e2 = Entry(window)
    e2.pack()

    

    def get_all():
        how_many = e2.get()
        worldtype = e1.get()

    button = Button(window, text = 'OK', command = get_all())
    button.pack()
    window.mainloop()

    type_worlds = {'p2p': {91, 90, 89, 88, 87, 86, 78, 77, 76, 75, 74, 73, 70, 69, 68, 67, 66, 65, 62, 61, 60,
                           59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38,
                           36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 24, 23, 22, 21, 20, 19, 18, 17, 15, 14, 13, 12,
                           11, 10, 9, 7, 6, 5, 4, 3, 2},
                   'f2p': {85, 94, 93, 1, 83, 84, 35, 81, 82, 16, 26, 8},
                   'pvp': {37, 25, 92}
                   }

    print '***Pinging ***'
    t = time.time()
    worlds = list()
    help = False

    if worldtype == 'help':
        help = True

    while help:
        print 'The avaliable options are: f2p, p2p, pvp'
        worldtype = raw_input("Please write the type of world you're searhcing for: ")
        help = False
    if worldtype != '':
        OSRS_Servers_ping.ping_worlds(type_worlds[worldtype])
    else:
        OSRS_Servers_ping.ping_range(1, 99)

    OSRS_Servers_ping.how_many_worlds(how_many, worlds)

    print 'The program finished in ', time.time() - t, 'seconds.'
    print 'Happy Scaping!'

w = Tk()

l = Label(w, text = 'Select the script')
l.pack()

osrs_server = Button(w, text = 'Server Ping', command = server_ping)
update_cml = Button(w, text = 'Update Stats', command = auto_update)

osrs_server.pack()
update_cml.pack()

w.mainloop()
