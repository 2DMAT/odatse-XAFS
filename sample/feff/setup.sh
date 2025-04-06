#!/bin/sh

set -e

if [ ! -d feff8.5light ]; then
  git clone https://github.com/eucall-software/feff8.5light.git

  cd feff8.5light
  patch -p1 < ../feff8.5light_output.patch
  cd ..
fi

cd feff8.5light

if [ -d build ]; then
  rm -rf build
fi
mkdir build && cd build

#-- for gfortran 10 or later
cmake -DCMAKE_Fortran_COMPILER="gfortran" -DCMAKE_Fortran_FLAGS="-fallow-argument-mismatch -std=legacy" ..

#-- for gfortran 9 or earlier
#cmake -DCMAKE_Fortran_COMPILER="gfortran" -DCMAKE_Fortran_FLAGS="-Wno-argument-mismatch -std=legacy" ..

#-- for intel compiler, use the following line instead of the above.
#cmake -DCMAKE_Fortran_COMPILER="ifort" ..

make

cp -p feff85L ../../

echo "done."
