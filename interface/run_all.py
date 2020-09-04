import pytest

if __name__ == "__main__":
    pytest.main(['-v', '--tb=line', '-m=smoke', '--junitxml=test-report.xml'])
    # pytest.main(['-v', '-s', '-m=smoke'])
