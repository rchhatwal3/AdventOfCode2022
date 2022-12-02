#!/bin/bash
for i in {2..25}
do
    mkdir -p "Day$i"
    cd "Day$i"
    touch "solution.py"
    touch "input.txt" 
    touch "README.md"
    cd ..
    echo "created folder Day$i"
done