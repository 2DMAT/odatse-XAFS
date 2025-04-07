#!/bin/sh

export PYTHONUNBUFFERED=1
export OMPI_MCA_rmaps_base_oversubscribe=true

CMD=odatse-XAFS

#MPIEXEC=""
MPIEXEC="mpiexec -np 4"


sh prepare.sh

time $MPIEXEC $CMD input.toml


result=output/ColorMap.txt
reference=ref_ColorMap.txt
tolerance=1.0e-5

echo diff $result $reference
res=0
#diff $result $reference || res=$?
python3 ../tools/almost_diff.py $tolerance $result $reference || res=$?
if [ $res -eq 0 ]; then
  echo TEST PASS
  true
else
  echo TEST FAILED: $result and $reference differ
  false
fi

