#!/usr/bin/env bash

set -e

echo "========================================"
echo "      AEON MATRIX SPRINT HEALTH"
echo "========================================"

echo
echo "[Git]"
echo "Branch : $(git branch --show-current)"
echo "Commit : $(git rev-parse --short HEAD)"

echo
echo "[Project]"
echo "Python Files : $(find . -name '*.py' | wc -l)"
echo "Test Files   : $(find tests -type f 2>/dev/null | wc -l)"
echo "Docs         : $(find docs -name '*.md' 2>/dev/null | wc -l)"
echo "Services     : $(find services -type d | wc -l)"

echo
echo "[Guardian]"
find services/guardian -maxdepth 1 -type d | tail -n +2 | wc -l

echo
echo "[TODO]"
grep -R "TODO\|FIXME" . --exclude-dir=.git 2>/dev/null | wc -l

echo
echo "[Git Status]"
git status --short

echo
echo "Sprint Health : OK"
echo "========================================"
