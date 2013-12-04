import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from watchdog.events import FileModifiedEvent
import client
import os
import Queue

class TestEventHandler(FileSystemEventHandler):

    def __init__(self, c, dir):
        self.c = c
        self.dir = dir
        self.q = Queue.Queue()

    def on_any_event(self, event):
        self.q.put_nowait(event)

    def validate(self, path, name):
        return name[0] != '.' and name[-1] != '~' and not os.path.isdir(path)

    def process_event(self, event):
        type_change = event.event_type
        file_changed = event.src_path

        file_name = file_changed.split("/")[-1]

        print "What type of change: " + type_change
        print "What file was modified: " + file_changed
        print "Just the name: " + file_name

        if self.validate(file_changed, file_name):
            if type_change == 'created' :
                self.c.upload(file_changed)
                print 'uploaded'
            elif type_change == 'modified' :
                self.c.upload(file_changed)
                print 're-uploaded'
            elif type_change == 'deleted' :
                self.c.remove(file_changed)
                #delete file from server
                print 'deleted'
        else:
            print "Invalid"

    def process_events(self):
        while not self.q.empty():
            print "Found item!"
            self.process_event(self.q.get_nowait())
    
    def send_changes(self):
        while self.c.sync:
            print "Read Queue"
            self.process_events()
            time.sleep(1)

    def start(self):
        logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
        #path = sys.argv[1] if len(sys.argv) > 1 else '.'

        path = self.dir
        if not os.path.isdir(path):
            os.makedirs(path)

        observer = Observer()

        observer.schedule(self, path, recursive=True)
        observer.start()

        try:
            while self.c.sync:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        observer.stop()
        observer.join()

