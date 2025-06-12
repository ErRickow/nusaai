# Metadata

Metadata response dari NusantaraAI.

## Example Usage

```typescript
import { Metadata } from "openapi";

let value: Metadata = {
  creator: "nusantaraai",
  status: true,
  timestamp: new Date("2025-06-09T16:00:00Z"),
  requestId: "req_abc123",
  processingTime: 1.234,
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `creator`                                                                                     | *string*                                                                                      | :heavy_minus_sign:                                                                            | Pembuat API                                                                                   | nusantaraai                                                                                   |
| `status`                                                                                      | *boolean*                                                                                     | :heavy_minus_sign:                                                                            | Status response (true = sukses, false = error)                                                | true                                                                                          |
| `timestamp`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_minus_sign:                                                                            | Timestamp response                                                                            | 2025-06-09T16:00:00Z                                                                          |
| `requestId`                                                                                   | *string*                                                                                      | :heavy_minus_sign:                                                                            | ID unik untuk request                                                                         | req_abc123                                                                                    |
| `processingTime`                                                                              | *number*                                                                                      | :heavy_minus_sign:                                                                            | Waktu pemrosesan dalam detik                                                                  | 1.234                                                                                         |