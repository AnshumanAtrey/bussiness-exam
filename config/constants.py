"""Case study constants from PS.txt - SecureNet Technologies Pvt. Ltd."""

COMPANY_NAME = "SecureNet Technologies Pvt. Ltd."
COMPANY_SHORT = "SecureNet"
COMPANY_LOCATION = "Mumbai, India"

# Client base
TOTAL_CLIENTS = 50
INCIDENT_RATE = 0.08  # 8% of clients faced incidents

# Financial figures (in INR)
ANNUAL_OPERATIONAL_COST = 90_00_000  # 90 Lakhs on manual security + incident handling
PROPOSED_INVESTMENT = 60_00_000  # 60 Lakhs for cloud monitoring system
ESTIMATED_ANNUAL_LOSSES = 20_00_000  # 20 Lakhs estimated from breach damages

# Projected improvements
INCIDENT_HANDLING_REDUCTION = 0.40  # 40% reduction in handling costs
SECURITY_LOSS_REDUCTION = 0.50  # 50% reduction in breach losses

# Attack type distribution (realistic weights)
ATTACK_DISTRIBUTION = {
    "Phishing": 0.38,
    "Ransomware": 0.18,
    "Malware": 0.22,
    "DDoS": 0.12,
    "SQL Injection": 0.06,
    "Insider Threat": 0.04,
}

# Severity distribution
SEVERITY_LEVELS = ["Low", "Medium", "High", "Critical"]
SEVERITY_WEIGHTS = [0.35, 0.30, 0.25, 0.10]

# Response time benchmarks (in minutes)
RESPONSE_TIME_BEFORE = {"mean": 247, "std": 85}  # ~4 hours avg
RESPONSE_TIME_AFTER = {"mean": 12, "std": 6}  # ~12 minutes avg

# Industries served
CLIENT_INDUSTRIES = [
    "Healthcare", "Financial Services", "Retail", "Manufacturing",
    "Education", "Legal", "Logistics", "Real Estate", "IT Services", "Media"
]

# Monitoring system features
SYSTEM_FEATURES = [
    "Real-time threat detection and alerting",
    "Automated log collection and analysis",
    "Cloud-based security dashboard",
    "Intrusion detection and prevention",
    "Vulnerability scanning and assessment",
    "Incident response automation",
    "Compliance reporting (ISO 27001, GDPR)",
    "Network traffic anomaly detection",
]
