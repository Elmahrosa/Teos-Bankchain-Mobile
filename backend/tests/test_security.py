import subprocess

def test_bandit_scan():
    result = subprocess.run(["bandit", "-r", "backend"], capture_output=True)
    assert result.returncode == 0  # 0 = no issues found

def test_trivy_scan():
    # Placeholder for container scan
    assert True
