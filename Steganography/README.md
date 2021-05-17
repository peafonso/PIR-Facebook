# Steganography
 For this part, we used the JS library for steganography with encryption : [Crypto Stego](https://github.com/zeruniverse/CryptoStego) who support least significant bit mode and DCT mode. 


**Note: This JS library needs HTML5 support!**

### How to use it?
* After cloning the repository, you will need to go in the "test/test_launch" directory. 
* Launch the index.html file on a local web page in order to test both actions. This file refers to the two others html : hide.html and reveal.html.

This directory also include a manifest.json used to implement a temporary plugin on Mozilla

**To change modes (DCT or LSB) you need to modify the levels in two functions writeIMG and readIMG (located in hide.html and reveal.html), within those functions are called writeMsgfromCanvas and reagMsgfromCanvas, the last argument of those functions represent the level used (level 0 > LSB with Best Secrecy, No Robustness to Compression/ level 1 to 5 > DCT with Best Robustness to Compression, Worst Secrecy).
Originally the level is 1**
