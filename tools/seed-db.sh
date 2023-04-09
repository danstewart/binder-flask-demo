#!/usr/bin/env bash

echo "INSERT INTO user VALUES (1, 'Dan')" | sqlite3 /tmp/binder-flask-demo.db
echo "INSERT INTO post VALUES (1, 1, 'Hello, World!')" | sqlite3 /tmp/binder-flask-demo.db
echo "INSERT INTO post VALUES (2, 1, 'Another message')" | sqlite3 /tmp/binder-flask-demo.db
echo "INSERT INTO post VALUES (3, 1, 'Testing...1...2...3...')" | sqlite3 /tmp/binder-flask-demo.db
