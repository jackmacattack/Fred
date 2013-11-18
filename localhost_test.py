
import run_server
import threading
import user_input


def server():
    run_server.run()

t = threading.Thread(name='server', target=server)

t.start()

user_input.main()