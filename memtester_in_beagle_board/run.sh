#/bin/sh

#install gcc
sudo opkg install gcc

#get source
wget http://pyropus.ca/software/memtester/old-versions/memtester-4.3.0.tar.gz

#unpack
tar zxvf memtester-4.3.0.tar.gz
cd memtester-4.3.0

#set compiler
sed 's/cc/gcc/' conf-*

#build
make

#install
sudo cp memtester /usr/bin/memtester
