# ModerationResult

## Example Usage

```typescript
import { ModerationResult } from "neosantara-ai/models/components";

let value: ModerationResult = {};
```

## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `flagged`                 | *boolean*                 | :heavy_minus_sign:        | Apakah konten terflag     |
| `categories`              | Record<string, *boolean*> | :heavy_minus_sign:        | Kategori yang terflag     |
| `categoryScores`          | Record<string, *number*>  | :heavy_minus_sign:        | Skor setiap kategori      |