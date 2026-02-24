# test_validator.py

from validator import ConfigValidator


def get_rules():
    return {
        "require_bgp_auth": True,
        "forbid_default_permit": True,
        "required_hostname_prefix": "DC-"
    }


def test_valid_config():
    config = """
    hostname DC-RTR1
    authentication-key secret
    """

    validator = ConfigValidator(get_rules())
    result = validator.validate(config)

    assert result.passed is True
    assert result.violations == []


def test_missing_bgp_auth():
    config = """
    hostname DC-RTR1
    """

    validator = ConfigValidator(get_rules())
    result = validator.validate(config)

    assert result.passed is False
    assert "BGP authentication missing" in result.violations


def test_hostname_prefix_violation():
    config = """
    hostname RTR1
    authentication-key secret
    """

    validator = ConfigValidator(get_rules())
    result = validator.validate(config)

    assert result.passed is False
    assert any("Hostname must start" in v for v in result.violations)