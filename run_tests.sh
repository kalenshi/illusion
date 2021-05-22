#!/bin/bash
result=0
coverage erase
coverage run --source='.' manage.py test tests

if [[ $? -ne 0 ]]; then
    result=1
fi

coverage report -m
coverage xml

exit $result