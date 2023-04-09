#!/usr/bin/env bash


cd ../binder && npm run build && cd -
cp -r ../binder/build/static/js/binder/ ./app/static/js/
