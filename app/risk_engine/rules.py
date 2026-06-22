RISK_RULES = {
    21: {
        "service": "FTP",
        "severity": "HIGH",
        "recommendation": "Disable FTP and use SFTP instead."
    },

    22: {
        "service": "SSH",
        "severity": "MEDIUM",
        "recommendation": "Restrict SSH access to trusted IP addresses."
    },

    23: {
        "service": "TELNET",
        "severity": "CRITICAL",
        "recommendation": "Disable Telnet immediately and replace it with SSH."
    },

    80: {
        "service": "HTTP",
        "severity": "LOW",
        "recommendation": "Consider enforcing HTTPS."
    },

    443: {
        "service": "HTTPS",
        "severity": "LOW",
        "recommendation": "Maintain valid TLS certificates."
    },

    3306: {
        "service": "MySQL",
        "severity": "CRITICAL",
        "recommendation": "Do not expose MySQL directly to the internet."
    },

    3389: {
        "service": "RDP",
        "severity": "HIGH",
        "recommendation": "Restrict RDP access and enforce MFA."
    }
}

def get_risk_info(port):
    return RISK_RULES.get(
        port,
        {
            "service": "Unknown",
            "severity": "LOW",
            "recommendation": "Review this service manually."
        }
    )