# ModerationsResponse

## Example Usage

```typescript
import { ModerationsResponse } from "neosantara-ai/models/components";

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

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |
| `model`                                                                      | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |
| `results`                                                                    | [components.ModerationResult](../../models/components/moderationresult.md)[] | :heavy_minus_sign:                                                           | N/A                                                                          |
| `metadata`                                                                   | [components.Metadata](../../models/components/metadata.md)                   | :heavy_minus_sign:                                                           | Metadata response dari NusantaraAI.                                          |