#!/bin/sh

chmod u+x {{cookiecutter.name}}.py
mv {{cookiecutter.name}}.py ../

cd ..; rmdir {{cookiecutter.name}}
