---
layout: post
title:  How to add a 3.5mm Audio Jack to a Xbox 360
date: 2018-06-03 14:22:26 +0100
category: hardware
description: This is a guide on how to add a analog audio output to a Xbox 360 (Jasper)
---
![X220](/assets/img/jack.jpg)

Why Microsoft did not put an analog audio output on their Xbox 360 game console is beyond me. This design decision makes it all-so-difficult to get sound when using a PC monitor via a HDMI to DVI cable, as the DVI cable does not carry audio. Also you can not plug in the AV cable when the HDMI is plugged in. Of course there is an adapter available, but I am impatient. In this post I will show you how to add a 3.5mm jack to Xbox 360. Where did I put those schematics...

Needeed tools:

1) Soldering station, flux, solder    
2) $1 3.5mm extension cable

After looking at the schematics we see the DAC, which is a custom Microsoft part. Out of the DAC there is some output clamping and filtering, and the output goes to the AV port.

![schem](/assets/img/schem.png)

We will pick the signal up from the ferrite beads FB2A2 and FB2A1. They are located here on the board:

![fbds](/assets/img/fbds.png)

Go ahead, disassemble your Xbox, cut the 3.5mm cable in half and tin the cables. After that, route the cable through the holes
next to the DVD drive on the Xbox, next to the HDD. The below picture was taken after assembling the Xbox again, just to show where
the cable goes.

![top](/assets/img/top.jpg)

Next, solder the wires from the 3.5mm cable to the ferrite beads FB2A2 and FB2A1. FB2A2 is the right channel and FB2A1 is the left channel. Ignore the RGH chip :)    
Solder the ground wire from the 3.5mm jack to the I/O shield.

![top](/assets/img/points.jpg)

And that is it. The signal is weak as there is no amp after the DAC, so use a decent amp after the Xbox.    
**DO NOT PLUG IN THE HEADPHONES DIRECTLY IN, YOU WILL PROBABLY FRY THE DAC.**

