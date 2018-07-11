import paramiko

# future improvement look into channel = p_connect.invoke_shell()

class SSH_LOGIN:
    def __init__(self, port, username, password, server):
        try:
            self.p_connect = self.__login(server, port, username, password)
        except:
            raise ValueError("bad login information")

    def logout(self):
        self.p_connect.close()
        self.p_connect = None

    # public
    def read_file_from_location(self, file_location, file_name): 
        stdin, stdout, sterr = self.p_connect.exec_command(
            "cd {} && cat {}".format(file_location, file_name))
        return self.__check_error(stdout, sterr)

    def add_file_at_location(self, file_location, file_name, file_text):
        stdin, stdout, sterr = self.p_connect.exec_command(
            "cd {} && echo {} > {}".format(file_location, file_text, file_name)) 
        self.__check_error(stdout, sterr)

    def add_folder_and_file_at_location(
            self, folder_name, file_location, file_name, file_text):
        stdin, stdout, sterr = self.p_connect.exec_command(
            "cd {} && mkdir {}".format(file_location, folder_name))
        file_location += "/" + folder_name
        self.add_file_at_location(file_location, file_name, file_text) 
        self.__check_error(stdout, sterr)

    def delete_folder(self, folder_location):
        stdin, stdout, sterr = self.p_connect.exec_command(
            "rm -rf {}".format(folder_location))
        self.__check_error(stdout, sterr)

    def delete_file(self, folder_location, file_name):
        stdin, stdout, sterr = self.p_connect.exec_command(
            "rm {}/{}".format(folder_location, file_name))
        self.__check_error(stdout, sterr)

    # private
    def __login(self, server_name, port, username, password):
        p_connect = paramiko.SSHClient()
        p_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p_connect.connect(server_name, port=port, username=username,password=password)
        return p_connect

    def __check_error(self, stdout, sterr):
        out = stdout.readlines()
        error = sterr.readlines() 
        if len(out) == 0 and len(error) > 0:
            raise ValueError(error[0])
        else:
            return out
