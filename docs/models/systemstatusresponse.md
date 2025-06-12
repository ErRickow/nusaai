# SystemStatusResponse

## Example Usage

```typescript
import { SystemStatusResponse } from "openapi";

let value: SystemStatusResponse = {
  system: {
    status: "operational",
    version: "1.0.0",
  },
  yourTier: "Free",
  metadata: {
    creator: "nusantaraai",
    status: true,
    timestamp: new Date("2025-06-09T16:00:00Z"),
    requestId: "req_abc123",
    processingTime: 1.234,
  },
};
```

## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `system`                                   | [models.System](../models/system.md)       | :heavy_minus_sign:                         | N/A                                        |                                            |
| `yourTier`                                 | *string*                                   | :heavy_minus_sign:                         | Tier akun Anda                             | Free                                       |
| `yourUsage`                                | [models.YourUsage](../models/yourusage.md) | :heavy_minus_sign:                         | N/A                                        |                                            |
| `metadata`                                 | [models.Metadata](../models/metadata.md)   | :heavy_minus_sign:                         | Metadata response dari NusantaraAI.        |                                            |