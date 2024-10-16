from src.main import main
from io import StringIO
import pytest

@pytest.mark.parametrize("input_file, expected_output", [
    (
        "src/tests/inputs/case-1.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}]\n"
    ),
    (
        "src/tests/inputs/case-2.txt",
        "[{'tax': 0.0}, {'tax': 10000.0}, {'tax': 0.0}]\n"
    ),
    (
        "src/tests/inputs/case-2+3.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}]\n[{'tax': 0.0}, {'tax': 10000.0}, {'tax': 0.0}]\n"
    ),
    (
        "src/tests/inputs/case-3.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 1000.0}]\n"
    ),
    (
        "src/tests/inputs/case-4.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}]\n"
    ),
    (
        "src/tests/inputs/case-5.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}, {'tax': 10000.0}]\n"
    ),
    (
        "src/tests/inputs/case-6.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}, {'tax': 3000.0}]\n"
    ),
    (
        "src/tests/inputs/case-7.txt",
        "[{'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}, {'tax': 0.0}, {'tax': 3000.0}, {'tax': 0.0}, {'tax': 0.0}, {'tax': 3700.0}, {'tax': 0.0}]\n"
    ),
    (
        "src/tests/inputs/case-8.txt",
        "[{'tax': 0.0}, {'tax': 80000.0}, {'tax': 0.0}, {'tax': 60000.0}]\n"
    )
])
def test_main_cases(monkeypatch, capfd, input_file, expected_output):
    f = open(input_file, "r")
    monkeypatch.setattr('sys.stdin', StringIO(f.read()))
    main()
    out, err = capfd.readouterr()
    assert out == expected_output


def test_main_empty(monkeypatch, capfd):
    monkeypatch.setattr('sys.stdin', StringIO("\n"))
    main()
    out, err = capfd.readouterr()
    assert out == ""