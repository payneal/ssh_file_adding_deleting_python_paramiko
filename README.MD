# python ssh login and file placement
* created to facilitate automation of placing file in certain location 
* python 2.7

## how to use

* fist make sure you have pip and or can install paramiko libary
```console
    
    # if you are using virtualenv
    virtualenv venv 
    source venv/bin/activate
    pip install requirements.txt

```

* add class and initiate
```python

    from ssh_login import SSH_LOGIN
    ssh_login = SSH_LOGIN(port#, "username", "password", "server.com" )

```

* add file to location on server
```python
    
    ssh_login.add_file_at_location(
        "location/you/want/to/place/file", 
        "file_name.txt", 
        "text that you want in the file you are placing")
```

* reading from file on server
```python
    
    text_read =  ssh_login.read_file_from_location(
        "location/of/file/to/read",
        "file_reading_name.txt")

    print text_read
    # all text we read
```

* delete file from server
```python
    
    ssh_login.delete_file(
        "file/to/delete/location ", 
        "file_deleting_name.txt")
```

* add folder and file with text to server
```python

    ssh_login.add_folder_and_file_at_location(
    "folder_name_adding",
    "location/placing/created/folder",
    "file_name.txt",
    "this is the text that will be added to file_name.txt")
```

* delete folder from server
```python

    ssh_login.delete_folder("/folder/to/delete")
```

## future upgrades
* look into channel = p_connect.invoke_shell() so we can have interactive console with multiple intences and can jus do a bunch of stuff on a bunch of different servers in a certain order, keep in mind thats interactive shell so big change potential prolly need exact use cases see: https://www.youtube.com/watch?v=lLKdxIu3-A4
