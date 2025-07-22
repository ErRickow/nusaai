# ModelInfo

## Example Usage

```typescript
import { ModelInfo } from "neosantara-ai/models/components";

let value: ModelInfo = {
  object: "model",
  ownedBy: "NeosantaraAI",
  pricing: {
    currency: "USD",
  },
};
```

## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *string*                                                           | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `object`                                                           | *string*                                                           | :heavy_minus_sign:                                                 | N/A                                                                | model                                                              |
| `created`                                                          | *number*                                                           | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `ownedBy`                                                          | *string*                                                           | :heavy_minus_sign:                                                 | N/A                                                                | NeosantaraAI                                                       |
| `permission`                                                       | [components.Permission](../../models/components/permission.md)[]   | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `root`                                                             | *string*                                                           | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `parent`                                                           | *string*                                                           | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `description`                                                      | *string*                                                           | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `capabilities`                                                     | *string*[]                                                         | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `maxTokens`                                                        | *number*                                                           | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |
| `pricing`                                                          | [components.ModelPricing](../../models/components/modelpricing.md) | :heavy_minus_sign:                                                 | N/A                                                                |                                                                    |