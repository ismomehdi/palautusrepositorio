*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallek
    Set Password  kalle123
    Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Register
    Register Should Not Succeed

Register With Valid Username And Invalid Password
    Set Username  kalleka
    Set Password  k
    Register
    Register Should Not Succeed

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekal
    Input Password  password  password123
    Input Password  password_confirmation  k
    Register
    Register Should Not Succeed

Login After Successful Registration
    Set Username  kallekall
    Set Password  kalle123
    Register
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout

    Go To Login Page
    Set Username  kallekall
    Set Login Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kallekall1
    Set Password  kalle123
    Register
    Register Should Not Succeed

    Go To Login Page
    Set Username  kallekall1
    Set Login Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Set Login Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register
    Click Button  Register

Register Should Succeed
    Successful Register Page Should Be Open

Register Should Not Succeed
    Register Page Should Be Open 

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
