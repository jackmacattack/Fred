import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print 'Changes have been made.'
        return 1


if __name__ == "__main__":
    event_handler = MyHandler()
    if MyHandler() == '1' :
        print "It worked"
    else :
        print "Nope"

    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()