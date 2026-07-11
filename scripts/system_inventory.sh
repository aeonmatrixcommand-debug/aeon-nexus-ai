#!/usr/bin/env bash

set -e

echo "==============================================="
echo "      AEON MATRIX SYSTEM INVENTORY REPORT"
echo "==============================================="
echo "Date : $(date)"
echo "Branch : $(git branch --show-current)"
echo "Commit : $(git rev-parse --short HEAD)"
echo

echo "========== MODULES =========="
echo "Guardian Modules        : $(find services/guardian -maxdepth 1 -type d | tail -n +2 | wc -l)"
echo "All Services            : $(find services -type d | wc -l)"
echo

echo "========== AI COMPONENTS =========="
for item in \
agent brain engine intelligence memory knowledge telemetry simulation runtime decision executive recommendation workflow dashboard integration validation security observability digital twin transport supply risk policy orchestration
do
    count=$(find services -type d | grep -i "$item" | wc -l)
    printf "%-24s %s\n" "$item" "$count"
done

echo
echo "========== FILES =========="
echo "Python Files            : $(find . -name '*.py' | wc -l)"
echo "Markdown Docs           : $(find docs -name '*.md' | wc -l)"
echo "YAML Files              : $(find . -name '*.yml' -o -name '*.yaml' | wc -l)"
echo "Test Files              : $(find tests -type f | wc -l)"

echo
echo "========== GITHUB =========="
git status --short

echo
echo "========== WORKFLOWS =========="
find .github/workflows -type f 2>/dev/null | sort || true

echo
echo "========== TOP MODULES =========="
find services/guardian -maxdepth 1 -type d | sort

echo
echo "==============================================="
echo " AEON MATRIX INVENTORY COMPLETE"
echo "==============================================="
