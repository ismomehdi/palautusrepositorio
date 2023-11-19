*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input  kalle  
    Input  kalle123
    Run Application
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command
    Input  kalle  
    Input  kalle123
    Run Application
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input  ka
    Input  kalle123
    Run Application
    Output Should Contain  Username is invalid

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input  kaäääääää  
    Input  kalle123
    Run Application
    Output Should Contain  Username is invalid

Register With Valid Username And Too Short Password
    Input New Command
    Input  kalle  
    Input  k
    Run Application
    Output Should Contain  Password is invalid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  kallekalle
    Run Application
    Output Should Contain  Password is invalid

*** Keywords ***
Input New Command
    Input  new
