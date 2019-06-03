import pytest
from Day04 import Shell

if __name__ == '__main__':
    shell = Shell.Shell()
    pytest.main(['-s','-q','--alluredir','./Report/xml/','.'])
    shell.invoke('allure generate ./Report/xml -o ./Report/html --clean')