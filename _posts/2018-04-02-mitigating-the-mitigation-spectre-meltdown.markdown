---
layout: post
title:  Disabling Spectre and Meltdown mitigation on Linux 4.1X
date: 2018-04-02 14:22:26 +0100
category: software
description: How to mitigate the mitigation for Spectre and Meltdown
---

After the whole Spectre and Meltdown fiasco has cooled down, let's take a look at real world performance with the mitigation patches applied to the Linux kernel.
Lately I noticed that my personal ThinkPad X220 is really sluggish, and I needed something to blame.

![logo](/assets/img/screenshot_retpo.png)

After a recent system upgrade from Ubuntu 17.10 to Ubuntu 18.04, I noticed that my system just feels slower. Opening PyCharm takes ages, compiling the Ubuntu kernel takes 30 minutes more and Firefox is struggling to render complex pages such as YouTube. I blamed it on my old SSD and brushed it off, but it started to get *really* annoying, considering my i5-2520m is performing like a last-gen i5 M540 in my dads ThinkPad X201.

Turns out, the real problem here is the mitigation for the x86 "security" bugs, more specifically repoline and KPTI.

### The benchmarks

In order to test performance of a mixed I/O heavy work load, I used the Phoronix Test Suite pts/compilebench-1.0.2 and a simple `time` on a Linux kernel compile. I tested a few kernels on my X220:

* 4.13.0-32-generic
* 4.15.0-13-generic
* 4.16-insecure

The 4.13 kernel is the original kernel Ubuntu keeps when installing a system for rollbacks. This kernel has no patches for Spectre and Meltdown. The 4.15 kernel is the latest kernel for Ubuntu 18.04 LTS with the KPTI and retpoline patchset applied and enabled, and 4.16-insecure is my own custom build of the mainline kernel provided by the Ubuntu Mainline kernel team, but with the retpoline and KPTI patches disabled via the config.

First, let's look at the results from the Phoronix test suite. The results are in MB/s.

| Kernel version     | Compile test | Initial create | Read compiled tree |
| ----------------   | ------------ | -------------- | ------------------ |
| 4.16-insecure      | 591.65       | 278.98         | 597.01             |
| 4.15.0-13-generic  | 572.86       | 250.24         | 283.95             |
| 4.13.0-32-generic  | 578.4        | 246.52         | 568.18             |

![pts1](/assets/img/pts_1.png)

From the image we can see that the 4.16 kernel is in itself faster than the old 4.13 kernel, but the 4.15 kernel with the Spectre and Meltdown patches applied is significantly slower on the I/O heavy workloads. On the raw CPU workloads the perform almost the same. Here is the normalized performance hit.

![pts2](/assets/img/pts_2.png)

In this test we clearly see that the performance hit on raw CPU workloads is not impacted that significantly, but I/O heavy workloads that require a lot of syscalls are up to __50%__ slower. This explains why PyCharm is indexing and opening painfully slow.

Now, let's take a look at my custom little benchmark, where I compile the Linux 4.16 kernel straight from kernel.org. The commands to replicate these benchmarks are:

```
wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.16.tar.xz
tar -xf linux-4.16.tar.xz
cd linux-4.16
time bash -c "git init . && git add . && git commit -m '1'"
make defconfig
time make -j4
```

Here are the wall clock time resuls from the benchmark in seconds:

| Kernel version    | make -j5     | git commit    |
| ----------------- | ------------ | ------------- |
| 4.16-insecure     | 515          | 22            |
| 4.15.0-13-generic | 570          | 24            |
| 4.13.0-32-generic | 528          | 22            |

![cmp1](/assets/img/cmp_1.png)

Here we can clearly see that the Linux compile time on the 4.15 kernel takes a lot more time. This explains the 30 minutes longer Ubuntu kernel build time. Here is the normalized performance hit in percents:

![cmp2](/assets/img/cmp_2.png)

Here we can see that the impact is around 10%, and that sounds about right for these patches. One could argue that a 10% performance hit is not that bad, but I disagree. According to [userbenchmark.com](http://cpu.userbenchmark.com/Compare/Intel-Core-i5-M-540-vs-Intel-Core-i5-2520M/m882vsm29), the i5-2520m is in itself only around 15% faster than a older i5 M540. These patches basically downgrade your laptop or PC one generation behind. 

The same is true for the i5-3230m found in the all-so-popular XX30 series of Lenovo ThinkPads, these patches turn your XX30 series laptop into a XX20 series laptop.

### So what now?

In order to keep performance on older laptops, I have decided to distribute my `-insecure` kernels via a APT repository for Ubuntu. This way, people who do not believe in Spectre or Meltdown or who want a 10% performance boost have the option to install my custom kernel.

If there is more interest, I will package the kernels for other distributions too.

The repositories are not ready, but the will be ready in a few days time. Thanks for reading!
