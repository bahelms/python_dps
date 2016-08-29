#!/bin/bash
./tasks/whenavail.sh postgres 5432 0 python setup.py
python dps.py
