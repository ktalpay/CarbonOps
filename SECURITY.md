# Security Policy

CarbonOps is pre-alpha. This policy describes how to report security issues and how the repository should treat public-safe examples.

## Supported Versions

| Version | Supported |
|---|---|
| 0.0.x | Best-effort review for the current pre-alpha baseline |

## Reporting A Vulnerability

If you believe you have found a security issue, do not create a public GitHub issue with exploit details.

Report it to:

```text
security@futureops.co.uk
```

Include, if available:

- Description of the issue.
- Steps to reproduce.
- Affected version or commit.
- Local environment details.

## Public-Safe Scope

CarbonOps examples should avoid:

- Credentials.
- Private keys.
- Customer data.
- Internal endpoints.
- Private service names.
- Non-public source code.

## Out Of Scope

The current repository does not provide a production platform, hosted API, deployment target, or real carbon-intensity integration. Reports that assume those features exist may be treated as documentation or roadmap feedback rather than a security vulnerability.
