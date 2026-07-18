#!/data/data/com.termux/files/usr/bin/bash

echo "================================="
echo " AEON MATRIX MOTHER BRAIN ONLINE "
echo "================================="

export PYTHONPATH="$PWD:$PYTHONPATH"

echo "[1] Guardian Intelligence"
python3 -m test_guardian_intelligence

echo ""
echo "[2] Telemetry Bus"
python3 -m test_telemetry_bus

echo ""
echo "[3] Mother Brain Runtime"
python3 -m test_runtime

echo ""
echo "================================="
echo " AEON MATRIX SYSTEM READY"
echo " Sense > Think > Decide > Act > Learn"
echo "================================="
