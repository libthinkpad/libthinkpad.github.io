## libthinkpad updated to 2.6

A new version of libthinkpad has been released that fixes dock detection
on a lot of newer ThinkPad models, including the P5X, and P7X series of laptops, 
as well as the majority of the XX50, XX60 and XX70 fleet.

Related commit: https://patchwork.kernel.org/patch/9416841/

Author: Ognjen Galić <smclt30p@gmail.com>
Date: 17th January 2018

## Added support for the Mini Dock Series 3 in dockd!

A new version of libthinkpad has been released that fixes dock detection    
for the Mini Dock Series 3 dock for various models. Get the new version now!   
 
Author: Ognjen Galić <smclt30p@gmail.com>    
Date: 23rd November 2017   

## Added support for Ubuntu 16.10 Yakkety Yak!

Somehow we overlooked Yakkety Yak when packaing for Ubuntu. Official repositories for Yakkety Yak are available    
on the [repositories](/repositories) page.
    
Author: Ognjen Galić <smclt30p@gmail.com>    
Date: 19th November 2017  

## New website design!

The site has been redesigned and the original Doxygen webpage has moved to the documentation of the libthinkpad library.    
Hope you like the new website!    
    
Author: Ognjen Galić <smclt30p@gmail.com>    
Date: 19th November 2017    

## dockd version 1.20 released

This is the first public release of dockd that has been tested locally and is open to public testing on other platforms.    
The library and executable have been tested on a ThinkpPad X220 and a Ultrabase Series 3, and are expected to work on any    
pre-XX40 series laptop and dock.     
    
In order to support laptops and docks after the XX40 series (including the P50/51/T450+) we need people who can dedicate their    
time and hardware to get it developed and tested.    
    
If you are willing to spare some time to test new hardware you can find me over at Freenode in #ibmthinkpad or contact me via    
email and we will meet on IRC.

Changelog:

* Removed udev dependency and mirgrated triggering to libthinkpad
* Added support for switching display modes when waking/sleeping the ThinkPad
* First public release


Any bugs can be reported on [GitHub](https://github.com/libthinkpad/dockd/issues).

Author: Ognjen Galić <smclt30p@gmail.com>    
Date: 18th November 2017 
