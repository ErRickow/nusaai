# Neosantara SDK

## Overview

NusantaraAI API: API NusantaraAI - OpenAI Compatible

**Rate Limit**
Setiap API KEY memiliki limit berdasarkan tier:
- Free: 10 request/menit, 100/hari, 10.000 tokens/menit, 50.000/hari
- Basic: 50 request/menit, 500/hari, 100.000 tokens/menit, 500.000/hari
- Standard: 60 request/menit, 2000/hari, 100.000 tokens/menit, 1.000.000/hari
- Pro: 120 request/menit, 10.000/hari, 200.000 tokens/menit, 5.000.000/hari
- Enterprise: 200 request/menit, 50.000/hari, 500.000 tokens/menit, 10.000.000/hari

Limit berlaku **per API key** dan juga **per user** (akumulasi).
Jika limit terlewati, akan mendapat error 429.
Reset harian dan bulanan otomatis, serta auto-downgrade ke Free jika subscription habis.

Untuk detail sistem rate limit, lihat dokumentasi MDX.

**Auth:** Gunakan header `Authorization: Bearer <API_KEY>`.

### Available Operations
