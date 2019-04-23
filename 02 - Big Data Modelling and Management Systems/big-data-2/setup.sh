#!/bin/sh

sudo yum install -y python-matplotlib libreoffice-calc python-imaging python-pip

pip install tweepy --user

pip install textblob --user

d=$(pwd)
cd $HOME/Downloads
wget http://archive.apache.org/dist/lucene/java/5.5.0/lucene-5.5.0.tgz
tar -xvzf lucene-5.5.0.tgz
cd $d
