#!/bin/bash

if [[ $# == 0 ]]; then
    echo "missing \"release\" or \"debug\" build mode argument"
    exit 1
fi

if [[ $1 == "release" ]]; then
    build_mode="release"
elif [[ $1 == "debug" ]]; then
    build_mode="debug"
else
    echo "unknown \"$1\" build mode"
    exit 1
fi

cmake -DCMAKE_BUILD_TYPE=$build_mode .
