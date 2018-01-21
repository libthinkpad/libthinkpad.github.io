We provide pre-built binaries for all projects that we host. Supported distributions are:     

- [Ubuntu](#ubuntu)
- [Arch Linux](#archlinux)
- [Other Distros](#otherdistros)

## Ubuntu

The ThinkPads.org team manages a couple of official repositories for versions of Ubuntu after Xenial Xerus.     
That includes:

* Ubuntu 17.10 Artful Ardwark (artful)
* Ubuntu 17.04 Zesty Zepus (zesty)
* Ubuntu 16.10 Yakkety Yak (yakkety)
* Ubuntu 16.04 Xenial Xerus (xenial)

To use them, first add the ThinkPads.org owner's GPG key:    


`wget -q -O - http://thinkpads.org/repo/ubuntu/thinkpads.gpg.key | sudo apt-key add - `   
   
Next, use one of the repositories provided:

* Ubuntu 17.10 Artful Ardwark (artful)    

`echo "deb http://thinkpads.org/repo/ubuntu artful main" | sudo tee /etc/apt/sources.list.d/thinkpads.list`    

* Ubuntu 17.04 Zesty Zepus (zesty)    

`echo "deb http://thinkpads.org/repo/ubuntu zesty main" | sudo tee /etc/apt/sources.list.d/thinkpads.list`    

* Ubuntu 16.10 Yakkety Yak (yakkety)    

`echo "deb http://thinkpads.org/repo/ubuntu yakkety main" | sudo tee /etc/apt/sources.list.d/thinkpads.list`    

* Ubuntu 16.04 Xenial Xerus (xenial)    

`echo "deb http://thinkpads.org/repo/ubuntu xenial main" | sudo tee /etc/apt/sources.list.d/thinkpads.list`    

## Arch Linux

All our packages are available in the Arch User Repository (AUR).    

[dockd](https://aur.archlinux.org/packages/dockd)
[libthinkpad](https://aur.archlinux.org/packages/libthinkpad)

## Other distros

We need packagers. If you are willing to package code for ThinkPads.org for other distributions, feel free to contact    
us at <smclt30p@gmail.com>.

Currently help is wanted for:

* Debian    
* Fedora    
* openSUSE    
