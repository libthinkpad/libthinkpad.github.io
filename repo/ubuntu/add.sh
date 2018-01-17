#!/bin/bash

if [ ! -n "$1" ]; then echo "Missing package name"; exit; fi
if [ ! -n "$2" ]; then echo "Missing package version"; exit; fi

PACKAGE=$1
VERSION=$2

for distro in xenial yakkety zesty artful; do
	reprepro include $distro ~/$distro/$PACKAGE\_$VERSION-*.changes;
	cd dists/$distro;
	gpg --clearsign -o InRelease Release;
	gpg -abs -o Release.gpg Release;
	cd ../../;
done
