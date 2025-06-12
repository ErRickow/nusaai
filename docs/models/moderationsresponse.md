# ModerationsResponse

## Example Usage

```typescript
import { ModerationsResponse } from "openapi";

let value: ModerationsResponse = {
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

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        |
| `model`                                                    | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        |
| `results`                                                  | [models.ModerationResult](../models/moderationresult.md)[] | :heavy_minus_sign:                                         | N/A                                                        |
| `metadata`                                                 | [models.Metadata](../models/metadata.md)                   | :heavy_minus_sign:                                         | Metadata response dari NusantaraAI.                        |