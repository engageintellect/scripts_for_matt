#!/usr/bin/env bash

# THIS SCRIPT IS A DEMO OF 'AWK' AND 'SED'.



# First, lets look at awk... awk will filter data in a file. Or can be used in a pipe.
# eg; "echo 'Hello World'| awk '{print $2}'" will give us "World"


# BEFORE AWK
echo "===[ AWK ]==="
echo ""
echo "[BEFORE AWK]"
cat text_for_script/bob.txt
echo ""


# This time we're gonna use awk to print the second line...
echo "[printing just the second line]"
cat text_for_script/bob.txt | awk 'NR==2'
echo ""


# This time we're gonna use awk to print the 3rd line...
echo "[printing just the second line]"
cat text_for_script/bob.txt | awk 'NR==3'
echo ""


# Now were going to print the first word of the seciond column..
echo "[printing first word of the second column]"
cat text_for_script/bob.txt | awk 'NR==2 {print $1}'
echo ""


# Lastly were going to print the first word of the seciond column..
echo "[printing fourth word of the first column]"
cat text_for_script/bob.txt | awk 'NR==1 {print $4}'




