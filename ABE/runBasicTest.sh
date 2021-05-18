#!/bin/bash

PURPLE='\033[0;95m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

#set -x

function assert()
{
    msg=$1; shift
    expected=$1; shift
    actual=$1; shift
    printf "${PURPLE}[+] $msg:${NC} "
    if [ "$expected" != "$actual" ]; then
        printf "${RED}FAILED with ERROR=$actual${NC}\n"
    else
        printf "${GREEN}PASSED${NC}\n"
    fi
}

function log() {
    printf "${PURPLE}[+] $1${NC}\n"
}

function log_test() {
    printf "${PURPLE}- Testing $1${NC}\n"
}


function cleanup() {
    file=$1
    suffix=$2
    rm plainOK.${file} *.${suffix}
    rm -f *.key
}

function echo_line() {
    echo "********************************************"
}

if [ $# -eq 0 ]; then
    log "No input file argument supplied. Exiting."
    exit -1
fi

INPUT=$1


#### TEST CP-ABE ####
echo_line
echo ""
echo_line
log_test "CP-ABE"
./oabe_setup -s CP -p org1
assert "Generate system parameters for CP" 0 $?

./oabe_keygen -s CP -p org1 -i "ONE|TWO|THREE" -o aliceCPABE
assert "Generate key for alice" 0 $?

./oabe_keygen -s CP -p org1 -i "ONE|TWO" -o bobCPABE
assert "Generate key for bob" 0 $?


echo_line
./oabe_enc -s CP -p org1 -e "(ONE and TWO and THREE)" -i ${INPUT} -o ${INPUT}.cpabe
assert "Encrypt under a simple policy" 0 $?

echo_line
./oabe_dec -s CP -p org1 -k bobCPABE.key -i ${INPUT}.cpabe -o plainFail.${INPUT}
assert "Decrypt using bob's key -- should fail" 32 $?

echo_line
./oabe_dec -s CP -p org1 -k aliceCPABE.key -i ${INPUT}.cpabe -o plainOK.${INPUT}
assert "Decrypt using alice's key -- should pass" 0 $?
