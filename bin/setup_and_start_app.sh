#!/bin/bash
./bin/whenavail.sh postgres 5432 0 python setup.py
exec python bin/start_dps.py
