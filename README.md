# 🧀 Swiss Cheese Software

![Swiss Cheese Software](swiss-cheese-software.png)

> *"It works on my machine" — every developer who touched this codebase*

**Swiss Cheese Software** is a deliberately vulnerable multi-language application designed for testing supply chain security scanners, dependency auditors, and SBOM generators. Every hole is intentional.

## 🕳️ What's Wrong With It?

**Everything.**

- 🔑 Hardcoded API keys, tokens, and credentials scattered throughout
- 📦 Outdated dependencies with known critical CVEs
- ⚰️ End-of-life packages that haven't been maintained in years
- 🐍 Python backend with prototype-pollution-adjacent packages
- ⚛️ React frontend frozen in 2019
- 🦀 Rust data pipeline with pre-1.0 crates
- 🔓 Database credentials in plaintext
- 🎯 The kind of codebase that makes security auditors cry

## 📁 Structure

```
swiss-cheese-software/
├── frontend/          # React app (Node.js/npm) — circa 2019
│   └── package.json
├── backend/           # Python Flask API — dependency hell
│   └── requirements.txt
├── data-pipeline/     # Rust batch processor — ancient crates
│   └── Cargo.toml
├── scripts/           # Deployment scripts with secrets
│   ├── deploy.sh
│   └── config.py
└── .env               # "Don't worry, it's in .gitignore" (it's not)
```

## 🎯 Purpose

This repo exists as a test target for [RiskwareSupplyChain](https://riskwaresupplychain.com) — a supply chain risk intelligence tool that scans dependencies for CVEs, public exploits, supply chain compromises, and hardcoded secrets.

**Try scanning this repo yourself:** paste `https://github.com/grepStrength/swiss-cheese-software` into the GitHub repo scanner.

## ⚠️ Disclaimer

**DO NOT deploy this application.** It is intentionally insecure and exists solely for security testing purposes. All secrets in this repo are fake and non-functional.

## 📝 License

MIT — because even terrible code deserves freedom.

---

*Built with questionable judgment by [grepStrength](https://grepstrength.dev)*
