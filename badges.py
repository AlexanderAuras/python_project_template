"""Generates badge_information for use with shields.io from calls to linters and data in ./reports."""
import json
import os
import subprocess
import tempfile
from functools import reduce

import defusedxml.minidom


def main() -> None:
    """Execute calls and generate badge infos."""
    temp_dir = os.path.join(tempfile.gettempdir(), "__python_project_template__")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    if not os.path.exists("./.badges"):
        os.mkdir("./.badges")

    subprocess.run(["python", "-m", "bandit", "-c", "pyproject.toml", "-f", "xml", "-o", os.path.join(temp_dir, "bandit.xml"), "-r", "src"])
    dom = defusedxml.minidom.parse(os.path.join(temp_dir, "bandit.xml"))
    bandit_issues = len(dom.documentElement.childNodes)
    with open("./.badges/bandit.json", "w") as file:
        json.dump({
            "schemaVersion": 1,
            "label": "bandit",
            "message": str(bandit_issues) + " issues",
            "color": "success" if bandit_issues == 0 else "critical"
        }, file)

    try:
        subprocess.check_output(["python", "-m", "pycodestyle", "src", "tests"])
    except subprocess.CalledProcessError as e:
        pycodestyle_issues = len(e.output.decode("utf-8").split("\n")) - 1
    else:
        pycodestyle_issues = 0
    with open("./.badges/pycodestyle.json", "w") as file:
        json.dump({
            "schemaVersion": 1,
            "label": "pycodestyle",
            "message": str(pycodestyle_issues) + " issues",
            "color": "success" if pycodestyle_issues == 0 else "yellow"
        }, file)

    try:
        subprocess.check_output(["python", "-m", "pydocstyle", "src"])
    except subprocess.CalledProcessError as e:
        pydocstyle_issues = len(e.output.decode("utf-8").split("\n")) - 1
    else:
        pydocstyle_issues = 0
    with open("./.badges/pydocstyle.json", "w") as file:
        json.dump({
            "schemaVersion": 1,
            "label": "pydocstyle",
            "message": str(pydocstyle_issues) + " issues",
            "color": "success" if pydocstyle_issues == 0 else "yellow"
        }, file)

    try:
        result = subprocess.check_output(["python", "-m", "pyright", "--outputjson"])
    except subprocess.CalledProcessError as e:
        result = e.output
    result = json.loads(result.decode("utf-8"))
    pyright_issues = int(result["summary"]["errorCount"]) + int(result["summary"]["warningCount"])
    with open("./.badges/pyright.json", "w") as file:
        json.dump({
            "schemaVersion": 1,
            "label": "pyright",
            "message": str(pyright_issues) + " issues",
            "color": "success" if pyright_issues == 0 else "important"
        }, file)

    subprocess.run(["python", "-m", "pytest", "--junitxml=" + os.path.join(temp_dir, "pytest.xml"), "--cov-report", "lcov:" + os.path.join(temp_dir, "lcov.info")], capture_output=True)
    dom = defusedxml.minidom.parse(os.path.join(temp_dir, "pytest.xml"))
    test_count = int(dom.documentElement.firstChild.attributes["tests"].value)
    fail_count = int(dom.documentElement.firstChild.attributes["errors"].value) + int(dom.documentElement.firstChild.attributes["errors"].value)
    with open("./.badges/pytest.json", "w") as file:
        json.dump({
            "schemaVersion": 1,
            "label": "tests",
            "message": "✓ " + str(test_count - fail_count) + " | ✗ " + str(fail_count),
            "color": "success" if fail_count == 0 else "critical"
        }, file)

    percentages = []
    line_count = 0
    covered_line_count = 0
    with open(os.path.join(temp_dir, "lcov.info")) as file:
        for line in file.readlines():
            if line.startswith("TN:") and line_count != 0:
                percentages.append(min(covered_line_count / line_count, 1.0))
                line_count = 0
                covered_line_count = 0
            elif line.startswith("LF:"):
                covered_line_count += int(line[3:])
            elif line.startswith("LH:"):
                line_count += int(line[3:])
        if line_count != 0:
            percentages.append(min(covered_line_count / line_count, 1.0))
            line_count = 0
            covered_line_count = 0
    coverage_percent = int(reduce(lambda acc, x: acc + x, percentages) / len(percentages) * 100.0)
    with open("./.badges/pytest_cov.json", "w") as file:
        json.dump({
            "schemaVersion": 1,
            "label": "coverage",
            "message": str(coverage_percent) + "%",
            "color": "success" if coverage_percent >= 90 else ("yellow" if coverage_percent >= 75 else "critical")
        }, file)


if __name__ == "__main__":
    main()
