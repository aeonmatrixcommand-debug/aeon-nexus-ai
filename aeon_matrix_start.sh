#!/data/data/com.termux/files/usr/bin/bash

echo "================================="
echo " AEON MATRIX ENTERPRISE OS BOOT "
echo "================================="

export PYTHONPATH="$PWD:$PYTHONPATH"

echo ""
echo "[1] Guardian Intelligence"
python3 test_guardian_intelligence.py

echo ""
echo "[2] Autonomous Execution"
python3 test_autonomous_execution.py

echo ""
echo "[3] Digital Twin Control"
python3 test_digital_twin_simulation.py

echo ""
echo "[4] Strategic Intelligence"
python3 test_world_intelligence.py

echo ""
echo "[5] Learning Loop"
python3 test_learning_loop.py

echo ""
echo "[6] Command Center"
python3 test_command_center.py

echo ""
echo "================================="
echo " AEON MATRIX CORE ONLINE "
echo " Sense > Think > Decide > Act > Learn "
echo " ENTERPRISE INTELLIGENCE READY "
echo "================================="
