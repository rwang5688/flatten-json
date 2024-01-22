#!/bin/bash
# delete and recreate output directory
rm -rf output/game=$1
mkdir output/game=$1

# execute command
echo "[CMD] python main.py"
cd src
python ./main.py --input-filename ../input/$1.json --output-filename-base ../output/game=$1/$1
cd ..
