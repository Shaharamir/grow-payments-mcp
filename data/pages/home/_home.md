---
title: "Grow Payments"
slug: _home
type: home
section: home
source_url: https://grow-il.readme.io/
---

# Grow Payments — Documentation Center

Grow Payments (grow-il / Meshulam) is an Israeli payment service provider (PSP). This documentation
center covers integrating Grow's payment products: hosted payment pages, the Light Server REST API,
webhooks, SDKs, 3DS, NFC and POS devices.

## Main sections

- **Guides** — product overviews & integration guides (payment pages, Light API, app, WordPress/Make, NFC, POS, 3DS).
- **API Reference** — the Light Server REST API: regular & token payments, payment links, refunds, direct debit, transaction/payment-process info, plus authentication, errors and IP allow-list.
- **Changelog** — release notes.

## Key integration facts

- Server endpoints: `/api/light/server/1.0/...`; Android/POS: `/api/light/andriod/1.0/...`.
- Sandbox host: `https://sandbox.meshulam.co.il` (alias `https://sandboxapi.grow.link`). Production hosts issued by Grow support.
- Auth per business via `userId` + `pageCode` (and/or API key); the values in docs are examples only.
- Requests are server-to-server, usually `multipart/form-data`; client-side calls are blocked.

See `../../llms.txt` for the full page index.

