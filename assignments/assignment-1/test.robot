*** Settings ***
Documentation    Your first python unit test with the robot framework.
Library          hello.py

*** Variables ***
${answer}  Hello, world!

*** Test Cases ***

Calling Hello Function
    ${value}=         Hello
    Should Be True    "${answer}" == "${value}"