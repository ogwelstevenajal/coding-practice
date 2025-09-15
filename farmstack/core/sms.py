import os


def send_sms(phone_number: str, message: str) -> None:
    """Pluggable SMS sender. Replace with real provider (e.g., Twilio) using env vars.

    For now, logs to stdout if no provider credentials are set.
    """
    provider = os.getenv('SMS_PROVIDER', 'console')
    if provider == 'console':
        print(f"[SMS] to={phone_number} msg={message}")
        return
    # Example stub for Twilio or other providers
    # Implement actual provider integration here using env vars
    print(f"[SMS-STUB-{provider}] to={phone_number} msg={message}")

