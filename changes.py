import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from watchdog.events import FileModifiedEvent

class TestEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        type_change = event.event_type
        file_changed = event.src_path
        print "What type of change: " + type_change
        print "What file was modified: " + file_changed
        if type_change == 'created' | 'modified' :
            #upload(file_changed)
            print 'uploaded'
        if type_change == 'deleted' :
            #delete file from server
            print 'deleted'


if __name__ == "__main__" :
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = TestEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


