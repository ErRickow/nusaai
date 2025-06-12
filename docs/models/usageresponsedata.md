# UsageResponseData

## Example Usage

```typescript
import { UsageResponseData } from "openapi";

let value: UsageResponseData = {};
```

## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `timestamp`                 | *number*                    | :heavy_minus_sign:          | Unix timestamp              |
| `usage`                     | *number*                    | :heavy_minus_sign:          | Jumlah token yang digunakan |
| `requests`                  | *number*                    | :heavy_minus_sign:          | Jumlah request              |
| `model`                     | *string*                    | :heavy_minus_sign:          | Nama model                  |