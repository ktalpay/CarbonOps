# Security and Confidentiality

## Public-Safe Repository Policy

CarbonOps should remain safe to inspect publicly. The repository should use generic examples, placeholder data, and documented assumptions.

## No Private Systems

Do not include references to private infrastructure, internal services, private repositories, or non-public architecture.

## No Customer Data

Do not commit customer names, customer identifiers, operational records, or data derived from customer systems.

## No Credentials

Do not commit:

- API keys.
- Passwords.
- Tokens.
- Certificates.
- Private keys.
- `.env` files.

## No Internal Endpoints

Do not include internal URLs, private hostnames, VPN-only endpoints, or non-public service names.

## No Employer-Specific Implementation Details

Keep examples generic. Do not describe employer-specific systems, customers, revenue, transaction volume, or production incidents.

## Safe Demo Data Principles

Safe demo data should be:

- Synthetic.
- Small.
- Clearly marked as example data.
- Free of private identifiers.
- Documented with its assumptions and limitations.

## Secret Scanning Checklist

Before committing, search for:

- `api_key`
- `password`
- `token`
- `secret`
- `.env`
- `client`
- `customer`
- internal URLs or private hostnames

## What Not To Commit

Do not commit private data, credentials, logs, local caches, generated secrets, private configuration, or screenshots that reveal private systems.
