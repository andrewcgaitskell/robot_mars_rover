Introduction

Really do not like having to run led control as root.

We should be able to create a raspian image that is run within the host and it will have access to just the GPIO.

# Created a Pi with a Lite Image

## Installed Docker

https://docs.docker.com/engine/install/ubuntu/

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

## Get Raspian Image

try to download the root file from this location

wget https://downloads.raspberrypi.org/raspbian_lite/root.tar.xz

may try:

https://downloads.raspberrypi.org/raspios_lite_arm64/

## Unzip Raspian Image

unxz root.tar.xz


Easier approach to extracting the root filesystem and not the boot system

https://www.computerhope.com/unix/losetup.htm

Very straightforward way of creating a Docker image

https://www.boulderes.com/resource-library/building-raspberry-pi-disk-images-with-docker-a-case-study-in-software-automation

# Create Dockerfile

nano Dockerfile

      from scratch
      user root
      add root.tar /
      CMD ["/bin/bash"]


# Create Image

docker build -t raspi-base .

# Run Container

docker run --name mycontainer -d -i -t alpine /bin/sh

docker run --name mypicont -d -i -t raspi-base:latest /bin/sh

# Connect to Container

docker exec -it mycontainer sh

docker exec -it mypicont sh


# Inside Container

apt update
apt upgrade

# Exit container

exit

# List Containers

docker ps

find container id

copy and paste into command below

# Commit changes

docker commit c2bb6383ff6e raspi-base:v1

# Links found

https://stackoverflow.com/questions/67838895/docker-access-to-raspberry-pi-gpio-pins-privileged-does-not-work

https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins

https://wiki.metacentrum.cz/wiki/Creating_Docker_Image_from_.iso_File

https://www.raspberrypi.com/software/operating-systems/

https://docs.podman.io/en/latest/markdown/podman-import.1.html

https://docs.oracle.com/en/learn/intro_podman/index.html#run-the-oracle-linux-8-slim-image

trying

podman import --change CMD=/bin/bash --change ENTRYPOINT=/bin/sh 2022-09-22-raspios-bullseye-arm64-lite.img.xz

alternatives

https://bleepcoder.com/podman/516849778/podman-import-from-a-tarball-doesn-t-preserve-metadata


Pi is stuck on storing signatures

https://github.com/containers/podman/issues/3323

hope to upload image to docker.io

https://stackoverflow.com/questions/55322347/docker-how-to-get-docker-image-to-github

