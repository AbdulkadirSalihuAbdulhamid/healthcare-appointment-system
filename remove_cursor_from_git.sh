#!/usr/bin/env bash
# Run this in Git Bash YOURSELF (not inside Cursor agent) to remove Cursor co-author lines.
set -e

cd "$(dirname "$0")"

echo "Removing Co-authored-by: Cursor from all commit messages..."

git filter-branch -f --msg-filter "grep -v 'Co-authored-by: Cursor' || true" -- --all

echo ""
echo "Done. Verify:"
git log -3 --format=full

echo ""
echo "If the log looks clean, push:"
echo "  git push --force origin main"
