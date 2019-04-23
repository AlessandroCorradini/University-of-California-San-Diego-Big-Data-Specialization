#!/bin/sh

# download and extract mongodb
wget http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.2.8.tgz
tar xpf mongodb-linux-x86_64-3.2.8.tgz

# create directory for database
mkdir db

# extract data
tar xzf dump.tar.gz

# start server
./mongodb-linux-x86_64-3.2.8/bin/mongod --dbpath db --fork --syslog

# import data
./mongodb-linux-x86_64-3.2.8/bin/mongorestore dump

# shut down server
./mongodb-linux-x86_64-3.2.8/bin/mongod --dbpath db --shutdown

# make symlink
ln -s mongodb-linux-x86_64-3.2.8 mongodb
