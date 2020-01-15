# FileZilla-Password-Decryptor

This Python script can be used to decrypt FileZilla passwords stored in a "FileZilla Server.xml" file. Extract the password and salt strings from the XML file into the Python script and use the --wordlist parameter to state your password list for the brute forcing attack. The script will then compute each SHA512+SALT hash and compare it to your password hash. If a match has been calculated, the password will be displayed.

Note: You have to replace escaped characters in the SALT string (e.g. with BurpSuite's Decoder, using "Smart Decode"). FileZilla's XML file escapes special characters in the following way:

```
&amp; = &
&lt; = <
&apos; = '
&quot; = "
&gt; = >

# Example
Escaped:   cwl.PD(Zw&lt;EA-@&gt;ux6z,]l5U7]$Cr@cW?aD4~:j4&quot;%_*\6k&quot;Uk{1k@P7IX`.K7v0
Unescaped: cwl.PD(Zw<EA-@>ux6z,]l5U7]$Cr@cW?aD4~:j4"%_*\6k"Uk{1k@P7IX`.K7v0
```



### Usage:

python decrypt.py --wordlist /path/to/password/wordlist
  
### Example:

python decrypt.py --wordlist /opt/wordlists/rockyou.txt
