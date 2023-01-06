pytest -v -s --html=Reports\report.html testcases --browser chrome
REM pytest -v -s --html=Reports\report.html testcases/test_searchCustomerByName.py --browser chrome
REM pytest -v -s -m "sanity and regression"--html=Reports\report.html testcases/test_searchCustomerByName.py --browser chrome (if  markers /grouping of test cases provided)