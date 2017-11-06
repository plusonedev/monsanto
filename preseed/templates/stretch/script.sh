#!/bin/sh

echo {{ instance.password }} | sudo -S ifconfig eth0 down;
ifconfig eth0 {{ instance.ip_address }} {{ instance.mask }};
ifconfig eth0 up
route add default gw {{ instance.gateway }};
echo nameserver {{ instance.nameserver }} > /etc/resolv.conf;

