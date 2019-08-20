#!/bin/bash
rm -rf programs
mkdir programs
cp ../coderdojo-python/*/*.py programs
perl -i -pe 'BEGIN{undef $/;} s/(\s?+)""".*?"""(\s?+)//smg' programs/*.py
