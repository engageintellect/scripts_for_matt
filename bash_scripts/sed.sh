#!/usr/bin/env bash


# sed can replace output in the terminal or even be ran on a file to replace every instance of a string.

echo "===[ BEOFRE SED ]==="
echo "hello world"
echo ""


echo "===[ AFTER SED ]==="
echo hello world | sed 's/hello/fuck you/g'
echo ""
echo ""


echo "===[ ANOTHER ONE, BEFORE... ]==="
echo "see spot run, spot runs fast, run spot run."
echo ""

echo "===[ AND AFTER]==="
echo "see spot run, spot runs fast, run spot run." | sed 's/spot/hooker/g'




