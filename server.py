__author__ = 'Jack'

import listener
import os
import shelvemod
import threading


class Server(listener.Listener):

    def __init__(self, host, port, db_location):
        listener.Listener.__init__(self, host, port)
        self.host = host  # Get local machine name
        self.port = port  # Reserve a port for your service.

        self.session = {}
        self.diff = {}
        self.db = shelvemod.DataFile(db_location)
        self.on = False

    def start(self):
        self.s.start()
        self.on = True
        
        self.t = threading.Thread(name='update', target=self.update)
        self.t.setDaemon(True)
        self.t.start()

    def add_connection(self, host, port):
        self.s.connect(host, port)

    def saveFile(self, user, path, data):
        folderPath= "/".join(path.split("/")[:-1])                #get just folder to check if the folder exists
        folder = os.path.expanduser("~/OneDir_server/%s%s" %(user,folderPath))

        print folder

        if not os.path.exists(folder):                              #check if folder exists
            os.makedirs(folder)
        #fullpath = os.path.expanduser("./%s/%s" %(user,path))
        fullpath = folder + "/" + path.split("/")[-1]
        print fullpath

        createFile = open(fullpath,"wb")
        createFile.write(data)
        createFile.close()

    def server_send_message(self, client, message):
        #self.s.connect(addr[0], addr[1] )
        self.s.connect(self.session[client][0], self.session[client][1])
        self.s.send(message)
        self.s.disconnect()

    def update_client(self, client, file_name):

        size = os.path.getsize(file_name)   #send the file size(needed for recv())

        readByte=open(file_name,"rb")       #read file
        data = readByte.read()
        readByte.close()

        message = "Update;Add;" + file_name + ";" + data

        self.server_send_message(client, message)

    def remove(self, client, file_name):
        self.server_send_message("Update;Remove;" + file_name)

    def delete(self, user, file_name):
        print "Remove"

    def auth(self, username, password):
        return self.db.verify(username, password)

    def on_message(self, addr, data):
        print "Client to Server:", addr, data

        arr = data.split(";")
        message = "Love"

        if arr[0] == "Connect":
            # host, port, user, filepath, filesize
            self.session[addr[0]] = [arr[1], int(arr[2]), "", "", 0]
            message = "Received"

        elif arr[0] == "Disconnect":
            del self.session[addr[0]]
            return

        elif arr[0] == "Add":

            if self.db.username_available(arr[1]):
                self.db.add_user(arr[1], arr[2], arr[3], arr[4], 0)

                folder = os.path.expanduser("~/OneDir_server/%s" %(arr[1]))

                print folder

                if not os.path.exists(folder):                              #check if folder exists
                    os.makedirs(folder)

                message = "Add;Success"
            else:
                message = "Add;NameTaken"

        elif arr[0] == "Login":

            if self.auth(arr[1], arr[2]):
                self.session[addr[0]][2] = arr[1]
                if arr[1] in self.diff:
                    self.diff[arr[1]] = {}
                message = "Login;Success;" + arr[1]
            else:
                message = "Login;Failure"

        elif arr[0] == "Message":

            if arr[1] == "Upload":
                self.session[addr[0]][3] = arr[2]
                self.session[addr[0]][4] = int(arr[3])
                message = "File;Send;" + arr[2]
            elif arr[1] == "Remove":
                self.delete(arr[2])
                self.diff[self.session[addr[0]][2]][self.session[addr[0]][3]].append("Remove", [addr[0]])
            elif arr[1] == "ChangePW":
                self.db.change_password(self.session[addr[0]][2], arr[2])

        elif arr[0] == "File":

            self.saveFile(self.session[addr[0]][2], self.session[addr[0]][3], arr[1])
            self.diff[self.session[addr[0]][2]][self.session[addr[0]][3]].append(self.session[addr[0]][3], "Add", [addr[0]])
            message = "File;Success"

        elif arr[0] == "RecoverPW":

            if not self.db.retrieve_password(arr[1], arr[2]):
                message = "PasswordFail"
            else:
                message = "Password;" + arr[1]

        elif arr[0] == "Debug":

            if arr[1] == "Kill":
                 self.stop()
                 return

        else:
            pass

        self.server_send_message(addr[0], message)

    def stop(self):
        self.s.disconnect()
        self.s.stop()
        self.db.close()
        self.on = False

    def update(self):
        while self.on:
            self.apply_changes()

    def apply_changes(self):
        for key1 in self.diff:
            diff = self.diff[key1]
            for conn in self.session:
                user = self.session[conn]
                if not user in diff[2]:
                    try:
                        if diff[1] == "Add":
                            self.update_client(user, diff[0])
                        elif diff[1] == "Remove":
                            self.remove(user, diff[0])

                        diff[2].append()
                    except Exception:
                        break


