#!/usr/bin/env bash

echo "========== MODULE REPORT =========="

find services/guardian -maxdepth 1 -type d | sort

echo
echo "========== COUNTS =========="

for k in \
agent brain engine intelligence memory knowledge telemetry decision executive workflow security recommendation
do
printf "%-20s %s\n" "$k" "$(find services -type d | grep -ic "$k")"
done
