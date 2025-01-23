#!/bin/sh

export PYTHONUNBUFFERED=1
export OMPI_MCA_rmaps_base_oversubscribe=true


sh prepare.sh

time python3 simple.py


result=output/res.txt
reference=ref_res.txt

echo diff $result $reference
res=0
diff $result $reference || res=$?
if [ $res -eq 0 ]; then
  echo TEST PASS
  true
else
  echo TEST FAILED: $result and $reference differ
  false
fi

