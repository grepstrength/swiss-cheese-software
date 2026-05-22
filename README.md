# 🧀 Swiss Cheese Software

![Swiss Cheese Software](swiss-cheese-software.png)

> *"It works on my machine" — every developer who touched this codebase*

**Swiss Cheese Software** is a deliberately vulnerable multi-language application designed for testing supply chain security scanners, dependency auditors, and SBOM generators. Every security hole is intentional.

## What's Wrong With It?

**Everything. Literally... everything.**

- 🔑 Hardcoded API keys, tokens, and credentials left and right
- 📦 Outdated dependencies with known critical CVEs
- ⚰️ End-of-life packages that haven't been maintained in years
- 🐍 Python backend with prototype-pollution-adjacent packages
- ⚛️ React frontend a couple *leap* years old
- 🦀 Rust data pipeline with pre-1.0 crates
- 🔓 Database credentials in plaintext for all the world to see
- 🎯 The kind of codebase that keeps application security engineers employed

## Structure

```
swiss-cheese-software/
├── frontend/          # React app (Node.js/npm) — circa 2019
│   └── package.json
├── backend/           # Python Flask API with a convoluted hell of dependencies 
│   └── requirements.txt
├── data-pipeline/     # Rust batch processor with crates almost as old as the language itself
│   └── Cargo.toml
├── scripts/           # Deployment scripts that might contain a (not very) secret or two
│   ├── deploy.sh
│   └── config.py
└── .env               # "Don't worry, it's in .gitignore" (it's not)
```

## Purpose

This repo exists as a test target for [RiskwareSupplyChain](https://riskwaresupplychain.com) —  a supply chain risk intelligence tool that scans dependencies for CVEs, public exploits, supply chain compromises, and hardcoded secrets.

**Try scanning this repo yourself:** paste `https://github.com/grepStrength/swiss-cheese-software` into the GitHub repo scanner.

## Disclaimer

**DO NOT deploy this application.** It is intentionally insecure and exists solely for security testing purposes. All secrets in this repo are fake and non-functional... I think.

## License

MIT — I'm not sure who would try to make this proprietary. 

---

*Built with questionable judgment by [grepStrength](https://grepstrength.dev)*
