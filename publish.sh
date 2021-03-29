#!/bin/sh
# commit and push the gme-data to github
cd ~/ver/gme-data
git fetch
git stash; git rebase; git stash pop
git add gme raw
git commit -m"data update from `date`" gme raw
git push
