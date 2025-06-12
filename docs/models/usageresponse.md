# UsageResponse

## Example Usage

```typescript
import { UsageResponse } from "openapi";

let value: UsageResponse = {
  object: "usage",
  tierInfo: {
    currentTier: "Free",
  },
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

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `object`                                                     | *string*                                                     | :heavy_minus_sign:                                           | N/A                                                          | usage                                                        |
| `data`                                                       | [models.UsageResponseData](../models/usageresponsedata.md)[] | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `totalUsage`                                                 | *number*                                                     | :heavy_minus_sign:                                           | Total penggunaan token                                       |                                                              |
| `totalRequests`                                              | *number*                                                     | :heavy_minus_sign:                                           | Total request                                                |                                                              |
| `tierInfo`                                                   | [models.TierInfo](../models/tierinfo.md)                     | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `currentUsage`                                               | [models.CurrentUsage](../models/currentusage.md)             | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `metadata`                                                   | [models.Metadata](../models/metadata.md)                     | :heavy_minus_sign:                                           | Metadata response dari NusantaraAI.                          |                                                              |