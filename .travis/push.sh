#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout master
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin https://$GH_TOKEN@github.com/mottaquikarim/pydev-psets.git
  git push --quiet --set-upstream origin master 
}

setup_git
commit_website_files
upload_files