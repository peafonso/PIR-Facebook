# Proxy
 For this part, we used the mitmproxy project : [mitmproxy](https://mitmproxy.org/). 


### How to use it?
* First, download and install mitmproxy.
* Generate the certificate for mitmproxy and add it to your Firefox list of certificates
* Change your Firefox network settings to use the proxy. Choose "manual configuration" with the IP address 127.0.0.1 and the port number 8080. Check the box to use this proxy with HTTPS and FTP (you will need this since Facebook uses HTTPS).
* Copy and paste the file remplacertouteslesimages.py in the same directory as the mitmproxy executables. You will also need an image of your choice, named image.jpg, in that same directory.
* Open that directory in a terminal and enter the command line "mitmdump -s remplacertouteslesimages.py" to run the proxy.
* Open Firefox and go to any web page with images. You should be able to see the results.

This directory also include the PAC file we used for auto-proxy configuration with other proxies (proxy.pac) and an unfinished version of the final addon (ouraddon.py).
