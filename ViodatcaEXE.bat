@ECHO OFF

START "Python Task" python principal.py

CD .\API

START "NPM Task" npm run dev
