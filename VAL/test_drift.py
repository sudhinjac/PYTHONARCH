from drift import detect_drift

def test_no_drift():
    config = """
    interface ge-0/0/0
    ip address 10.0.0.1
    """

    result = detect_drift(config, config)

    assert result == []


def test_missing_line():
    intended = """
    interface ge-0/0/0
    ip address 10.0.0.1
    """

    running = """
    interface ge-0/0/0
    """

    result = detect_drift(intended, running)

    assert any("Missing line" in r for r in result)


def test_extra_line():
    intended = """
    interface ge-0/0/0
    """

    running = """
    interface ge-0/0/0
    ip address 10.0.0.1
    """

    result = detect_drift(intended, running)

    assert any("Unexpected line" in r for r in result)