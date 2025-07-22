# CheckApiKeyStatusResponseBody

API Key status and usage info

## Example Usage

```typescript
import { CheckApiKeyStatusResponseBody } from "neosantara-ai/models/operations";

let value: CheckApiKeyStatusResponseBody = {
  object: "authorization",
  organization: "org-indonesia-ai",
  id: "auth-...",
  tier: "Free",
  metadata: {
    creator: "NeosantaraAI",
  },
};
```

## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `object`                                                     | *string*                                                     | :heavy_minus_sign:                                           | N/A                                                          | authorization                                                |
| `organization`                                               | *string*                                                     | :heavy_minus_sign:                                           | N/A                                                          | org-indonesia-ai                                             |
| `permissions`                                                | *string*[]                                                   | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `authorized`                                                 | *boolean*                                                    | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `created`                                                    | *number*                                                     | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `expires`                                                    | *string*                                                     | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `id`                                                         | *string*                                                     | :heavy_minus_sign:                                           | N/A                                                          | auth-...                                                     |
| `tier`                                                       | *string*                                                     | :heavy_minus_sign:                                           | N/A                                                          | Free                                                         |
| `usageInfo`                                                  | [components.UsageInfo](../../models/components/usageinfo.md) | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `metadata`                                                   | [components.Metadata](../../models/components/metadata.md)   | :heavy_minus_sign:                                           | N/A                                                          |                                                              |