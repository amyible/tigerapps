from gevent import spawn, sleep, kill
from rooms.update_avail import *
from rooms.models import *
import random
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
import time
from gevent.event import Event

class RoomUpdate(object):
    def __init__(self, room):
        self.room_id = room.id
        self.timestamp = int(time.time())

class AvailManager(object):
    SIM_RUNNING = False
    sim_thread = None

    def __init__(self):
        self.updates = []
        self.event = Event()


    def run_sim(self, delay, size):
        roomids = Room.objects.filter(avail=True).values_list('id',flat=True)
        #print 'Room ids: %s ' % roomids
        ids = []
        for i in range(0, len(roomids)):
            ids.append(roomids[i])
            random.shuffle(ids)
        for i in range(0, len(ids)):
            roomg = Room.objects.filter(id=ids[i])
            updateavail(Room.objects.filter(id=ids[i]))
            room = roomg[0]
            self.updates.append(RoomUpdate(room))
            self.event.set()
            self.event.clear()
            if i % size == 0:
                sleep(delay)
        self.SIM_RUNNING = False

    def start_sim(self, delay, size=1):
        if self.SIM_RUNNING:
            kill(self.sim_thread)
        self.updates = []
        Room.objects.all().update(avail=True)
        self.sim_thread = spawn(self.run_sim, delay=delay, size=size)
        self.SIM_RUNNING = True
        return HttpResponse('Started Simulation with delay %d' % delay)

    def stop_sim(self):
        if not self.SIM_RUNNING:
            return HttpResponse('No current simulation')
        kill(self.sim_thread)
        self.SIM_RUNNING = False
        return HttpResponse('Stopped simulation')
    
    def check_avail(self, timestamp):
        if len(self.updates) == 0 or timestamp > self.updates[0].timestamp:
            self.event.wait()
        room_ids = []
        i = len(self.updates) - 1
        while i >= 0:
            i = i - 1
            update = self.updates[i]
            if timestamp <= update.timestamp:
                room_ids.append(update.room_id)
            else:
                break

        return {'timestamp':int(time.time()),
                'rooms':room_ids}

avail_manager = AvailManager()
start_sim = avail_manager.start_sim
stop_sim = avail_manager.stop_sim
check_avail = avail_manager.check_avail
