#!/bin/sh

set -e

if [ ! -d feff8.5light ]; then
  git clone https://github.com/eucall-software/feff8.5light.git
fi

cd feff8.5light

if [ -d build ]; then
  rm -rf build
fi
mkdir build && cd build

cmake -DCMAKE_Fortran_FLAGS="-fallow-argument-mismatch -std=legacy" ..
make

cp -p feff85L ../../

echo "done."
