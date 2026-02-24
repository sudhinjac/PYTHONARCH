# validator.py

from dataclasses import dataclass
from typing import List


@dataclass
class ValidationResult:
    passed: bool
    violations: List[str]


class ConfigValidator:

    def __init__(self, rules: dict):
        self.rules = rules

    def validate(self, config_text: str) -> ValidationResult:
        violations = []

        if self.rules.get("require_bgp_auth"):
            if "authentication-key" not in config_text:
                violations.append("BGP authentication missing")

        if self.rules.get("forbid_default_permit"):
            if "permit any any" in config_text.lower():
                violations.append("Default permit rule detected")

        prefix = self.rules.get("required_hostname_prefix")
        if prefix:
            if "hostname" in config_text:
                lines = config_text.splitlines()
                for line in lines:
                    if line.strip().startswith("hostname"):
                        hostname = line.split()[1]
                        if not hostname.startswith(prefix):
                            violations.append(
                                f"Hostname must start with {prefix}"
                            )

        return ValidationResult(
            passed=len(violations) == 0,
            violations=violations
        )