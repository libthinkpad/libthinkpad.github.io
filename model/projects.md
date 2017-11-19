### What is ThinkPads.org?

We are a small community of developers, testers and package maintainers who are developing drivers and background services for your Lenovo ThinkPad.   
We build software that makes your life using your ThinkPad on Linux systems a breeze.    
There are a couple of projects already there and many planned. Here are the currently published projects:

- [dockd - Dock Management Daemon](#dockddockmanagementdaemon)

---

## dockd - Dock Management Daemon
When moving from Windows to Linux on a lightweight desktop environment like Xfce or LXDE, using the dock is really hard.   
Usually nothing happens when you insert the dock, and you use xrandr to configure your displays. Then, you remove the ThinkPad   
from the dock and the screen stays blank.

That's why we created dockd, a program that runs in the background and detects when your ThinkPad is added or removed from a dock    
and it automatically switches output mode profiles that you have configured before.

[More information here](/projects/dockd)    
    
Latest version: 1.20    
Developer: Ognjen Galić <smclt30p@gmail.com>    
[Upstream releases](http://thinkpads.org/ftp/dockd/)     
[git repository](https://github.com/libthinkpad/dockd)


## libthinkpad - General Lenovo ThinkPad userspace library
This library was created to abstract away all Lenovo ThinkPad-specific hardware like the docks and the ThinkLight. This library    
provides advanced features to software projects using it specific to Lenovo ThinkPad Laptops directly from the userspace.

This was created to avoid manual crawling of sysfs entries and udev rule filterings by each executable individually.     
All ThinkPads.org use this library in some way.

[More information here](/projects/libthinkpad)    
    
Latest version: 2.3      
Developer: Ognjen Galić <smclt30p@gmail.com>    
[Upstream releases](http://thinkpads.org/ftp/libthinkpad/)     
[git repository](https://github.com/libthinkpad/libthinkpad)