#!/bin/bash

TASK=${1?Err: require a task name}

if [ TASK == "install" ]; then
    echo "hello"
fi