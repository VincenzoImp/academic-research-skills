# Security Policy

## Supported Versions

The `main` branch is the supported version for skills.sh installation.

## Reporting A Vulnerability

Open a private security advisory or contact the repository owner before public
disclosure. Do not include secrets, private datasets, API keys, cookies, tokens,
or sensitive research data in an issue.

## Scope

This package contains procedural skills, references, metadata, and validation
scripts. Skills may instruct agents to use external MCP servers or third-party
document tools; review those dependencies before installing them in sensitive
research environments.

## Safe Use

- Prefer project-local installation for sensitive research.
- Review MCP servers before granting credentials or write access.
- Keep API keys and tokens in environment variables or ignored local config.
- Do not commit raw sensitive datasets, scraped private content, or credentials.
