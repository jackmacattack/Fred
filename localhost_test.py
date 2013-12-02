
import run_server
import threading
import user_input


stopper = run_server.Stopper()

def server():
    run_server.run(stopper)

t = threading.Thread(name='server', target=server)
t.setDaemon(True)
t.start()

user_input.main()

print "Exiting"
stopper.stop()
