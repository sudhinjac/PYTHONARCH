# main.py

import yaml
import sys
from validator import ConfigValidator
from drift import detect_drift


def load_rules(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_file(path: str):
    with open(path, "r") as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <config_file>")
        sys.exit(1)

    config_path = sys.argv[1]

    rules = load_rules("rules.yaml")
    config_text = load_file(config_path)

    validator = ConfigValidator(rules)
    result = validator.validate(config_text)

    print("Validation Passed:", result.passed)

    if not result.passed:
        print("Violations:")
        for v in result.violations:
            print("-", v)


if __name__ == "__main__":
    main()