# FileZilla-Password-Decryptor

This Python script can be used to decrypt FileZilla passwords stored in a "FileZilla Server.xml" file. Extract the password and salt strings from the XML file into the Python script and use the --wordlist parameter to state your password list for the brute forcing attack. The script will then compute each SHA512+SALT hash and compare it to your password hash. If a match has been calculated, the password will be displayed.

Note: Remember to URL-decode your SALT string! You can e.g. use BurpSuite's Decoder! Do not just copy paste the string into the script - this won't work!

### Usage:

python decrypt.py --wordlist /path/to/password/wordlist
  
### Example:

python decrypt.py --wordlist /opt/wordlists/rockyou.txt
