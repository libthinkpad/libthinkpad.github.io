---
layout: post
title:  Ricoh Drivers are causing high CPU usage on ThinkPad laptops
date: 2018-01-21 14:22:26 +0100
category: software
description: Are you seeing high CPU usage by the "System" process on Windows 10 on your ThinkPad? Read this.
---
![Ricoh logo](https://www.ricoh.com/about/company/history/img/logo/img-logo04.svg)

So after a few days of using my Lenovo ThinkPad on Windows 10 I noticed a major issue when it comes to the performance and thermals. The laptop was constantly hitting 85-90C when doing *nothing*, basicall in idle.

Of course my first action was to blame all my life problems on Microsoft, but Microsoft was not at fault this time. Opening Task Manager I noticed that the "System" process is using around 30% of CPU time.

![Task Manager](/assets/img/task.PNG)

So I downloaded Microsoft's Windows Performance Toolkit so that I could analyze what was using most of the CPU time inside the kernel, and after 2 hours of memory dumps, kernel logging and crash dumps, I finally found what was causing the high CPU time:

___risdxc64.sys___

That's the Ricoh card driver. It all made sense, I'm using a unofficial Windows 7 driver on Windows 10.
After disabling the Ricoh card reader driver, the CPU immediately surged down to 0% and my X220 cooled down to 50C.

The currently affected systems are:
* ThinkPad X220
* ThinkPad T420

Currently, the only known solution that is working is to disable the device in Device Manager. The card reader functions fine tho.