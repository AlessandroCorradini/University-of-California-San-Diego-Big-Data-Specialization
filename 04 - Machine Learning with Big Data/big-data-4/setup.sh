#!/bin/bash

# upgrade spark python to work with python 3
sudo yum upgrade -y spark-python hive

# remove old derby jar so only one version is on spark's classpath
sudo rm /usr/lib/flume-ng/lib/derby-10.8.2.2.jar

# decompress datasets
gzip -d *.csv.gz

# download and install anaconda for pandas, jupyter
rm -f Anaconda3-4.0.0-Linux-x86_64.sh
wget http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
bash Anaconda3-4.0.0-Linux-x86_64.sh

# add spark-csv jars to classpath
echo export SPARK_CLASSPATH="$(pwd)/lib/spark-csv_2.10-1.5.0.jar:$(pwd)/lib/commons-csv-1.1.jar" >> ~/.bashrc

# set environment variables to load spark libs in jupyter
echo "export PYSPARK_DRIVER_PYTHON_OPTS=\"notebook\"" >> ~/.bashrc
echo "export PYSPARK_DRIVER_PYTHON=jupyter"  >> ~/.bashrc

echo "Run 'source ~/.bashrc' to complete the setup."
