# test
import unittest
from ssh_login import SSH_LOGIN
import paramiko

class Test_ssh_log_in(unittest.TestCase):
    
    def setUp(self):
        self.port = 22
        self.user_name = "" 
        self.password = ""
        self.server = ""
        self.ssh_login = SSH_LOGIN(
            self.port, self.user_name, self.password,
            self.server)

    def tearDown(self):
        self.ssh_login.logout()

    def test_log_on_server_and_create_file(self):
        self.ssh_login.add_file_at_location(
            "~", "test.txt", "this is a test")
        text_added = self.ssh_login.read_file_from_location(
            "~", "test.txt")
        self.assertIn("this is a test", text_added[0])
        self.ssh_login.delete_file("~", "test.txt")

    def test_log_on_server_create_folder_and_file(self):
        self.ssh_login.add_folder_and_file_at_location(
            'ali', "~", 'payne.txt', "ali payne was here")
        text_added = self.ssh_login.read_file_from_location(
            "~/ali", "payne.txt")
        self.assertIn("ali payne was here", text_added[0])
        self.ssh_login.delete_folder("~/ali")

    def test_bad_file(self):
        with self.assertRaisesRegexp(
                ValueError, "No such file or directory\n"):
            self.ssh_login.read_file_from_location("~/test_check", "test.txt")

if __name__== "__main__":
    unittest.main()
