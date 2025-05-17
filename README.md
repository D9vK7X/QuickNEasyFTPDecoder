# QuickNEasyFTPDecoder

There is this old school ftp server tool called "Quick 'n Easy FTP Server". Despite having screenshots straight out of Windows XP in their documentation, I recently stumbled upon this program running on a production server.

The lite version has a very simple user management: User names and passwords are saved in a file users.xml in the same folder as the executable.
```xml
<>
```

The passwords are not encrypted, but rather just encoded with a Caesaric cipher.
I implemented the encoding and decoding methods in python, allowing the easy retrieval of cleartext credentials.

## Usage
$ python3 decoder.py encode "VeryS3cureP4ssword"
-> w-G+{K,)~q/p"2p5:6
$ python3 decoder.py decode 'w-G+{K,)~q/p"2p5:6'
-> VeryS3cureP4ssword#
