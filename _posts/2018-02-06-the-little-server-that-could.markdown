---
layout: post
title:  The little server that could
date: 2018-02-06 14:22:26 +0100
category: hardware
description: A story about a half-dead HP laptop turned onto its back like a turtle.
---

This blog is hosted on a dedicated server in my closet at home. I switched from Github Pages to a self-hosted server because of finer control over the server, dynamic content and full HTTPS encryption.
Let me introduce you to Yggdrasil:

![logo](/assets/img/server.jpg)

Yup, that's a HP Pavilion DV6000 turned onto its back. The GPU is dead, half of the keys on the keyboard don't work, the sound card is shot and the PCMCIA slot is missing, and yet it has been dead-reliable in hosting this site for 7 days straight, with the only interuptions being the Dynamic DNS updates between power outages. And that's it.

It's rocking a Intel Core2 T5500 ticking at 1.66GHz and is packing a whole 3GB of RAM. And all that glory is running Debian Stable.

Here are some traffic statistics in the past 7 days:

* Served 1604 *unique* IP addressses
* Served people from 73 unique countries
* Served __23770__ HTTP requests without problems
* Rejected 1015 invalid SSH connection attempts from 77 unique IP addresses
* System uptime is 37 days (had a previous life)

And also the core die temperature sensor is shot too, it is showing 13C in a 25C room:

```
coretemp-isa-0000
Adapter: ISA adapter
Core 0:       +16.0°C  (high = +100.0°C, crit = +100.0°C)
Core 1:       +13.0°C  (high = +100.0°C, crit = +100.0°C)
```

If you are thinking about using a laptop as a server, all I'm saying is go for it! :)
