# FileZilla-Password-Decryptor

This Python script can be used to crack FileZilla passwords stored in a "FileZilla Server.xml" file. Extract the password and salt strings from the XML file into the Python script and use the --wordlist parameter to state your password list for the brute forcing attack. The script will then compute each SHA512 hash and compare it to your password hash. If a match has been calculated, the clear text password will be displayed.

Note: FileZilla's XML file escapes special characters for the SALT string. So you will need to unescape them first (e.g. with BurpSuite's Decoder, using "Smart Decode")! Then specify it in the Python script and escape all characters with a backslash that may break Python's string syntax.

```
&amp; = &
&lt; = <
&apos; = '
&quot; = "
&gt; = >

# Example
Escaped:        `!U3`CQ;a&amp;3IzbXc/4Wpb\)OZ3TsXP;&apos;Wx#^K&quot;Tu_XX.K&apos;o&lt;&apos;c&amp;A:vItTX-M|Z0Y
Unescaped:      `!U3`CQ;a&3IzbXc/4Wpb\)OZ3TsXP;'Wx#^K"Tu_XX.K'o<'c&A:vItTX-M|Z0Y
```

### Usage:

python decrypt.py --wordlist /path/to/password/wordlist
  
### Example:

python decrypt.py --wordlist /opt/wordlists/rockyou.txt
