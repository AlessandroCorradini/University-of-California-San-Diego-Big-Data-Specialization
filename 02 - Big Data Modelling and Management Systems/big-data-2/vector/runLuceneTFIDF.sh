#!/bin/bash

L=$HOME/Downloads/lucene-5.5.0
CLASSPATH=${CLASSPATH}:$L/core/*:$L/queryparser/*:$L/analysis/common/*:$L/demo/*
export CLASSPATH

java LuceneTFIDF "$*"
