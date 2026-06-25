import re

def mask_sensitive_data(log_line: str) -> str:
    """
    Simple example of masking sensitive data before sending logs
    to a GenAI tool.
    """

    # Mask email addresses
    log_line = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "[EMAIL_MASKED]",
        log_line
    )

    # Mask Bearer tokens
    log_line = re.sub(
        r"Bearer\s+[A-Za-z0-9._\-]+",
        "Bearer [TOKEN_MASKED]",
        log_line
    )

    # Mask API keys in key=value format
    log_line = re.sub(
        r"(api[_-]?key=)[A-Za-z0-9._\-]+",
        r"\1[API_KEY_MASKED]",
        log_line,
        flags=re.IGNORECASE
    )

    # Mask IPv4 addresses
    log_line = re.sub(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "[IP_MASKED]",
        log_line
    )

    return log_line


if __name__ == "__main__":
    raw_log = (
        "User john@example.com failed login from 192.168.1.25 "
        "with Authorization: Bearer abc123.secret.token and api_key=sk_test_12345"
    )

    print("Raw log:")
    print(raw_log)

    print("\nMasked log:")
    print(mask_sensitive_data(raw_log))