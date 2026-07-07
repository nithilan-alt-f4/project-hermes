## Project Hermes

This repository documents an experiment exploring how easy it can be to misuse AI and cloud services for harmful purposes. The project was not deployed in the real world. No actual spam was sent, and all accounts and domains used were fabricated. The intent here is to highlight vulnerabilities, not to provide a working tool.

## Motivation

The experiment was motivated by curiosity: could an AI model be tricked into helping with actions that clearly violate platform rules? By presenting the task as a benign mailing list for a photography club, the AI provided assistance that could have enabled mass email abuse. This shows how safeguards can be bypassed with simple framing.

## What Happened

- The AI (claude) was asked to help automate bulk emails under the guise of a harmless use case.
- It provided steps that, if executed, would have violated a resends's Terms of Service.
- The process(about a week of work) revealed how easy it is to exploit free tiers, multiple accounts, and domains.

## Risks Identified

- Abuse of free tiers and API keys
- Circumventing safeguards in AI models
- Potential for mass spam or phishing campaigns
- Damage to trust in AI systems
- Erosion of platform integrity if misuse is unchecked

## Ethical Reflection

This case study underscores the responsibility of both AI developers and users. AI systems should not enable harmful automation so easily, and users must recognize the ethical boundaries of experimentation. Highlighting these risks is essential to encourage stronger guardrails and prevent real-world abuse.

## Whats needed

- Stricter monitoring of API usage and account creation
- Improved refusal training for AI models to resist manipulative prompts
- Clearer enforcement of Terms of Service
- User education on ethical AI use
- Collaboration between providers to detect and block suspicious activity

## Disclaimer

This repository is a critical commentary, not a tool release. The code included is inert and illustrative only. It should not be used for real-world applications. The goal is to spark discussion about AI safety and platform responsibility.
