# ModerationsResponse

## Example Usage

```typescript
import { ModerationsResponse } from "neosantara-ai/models/components";

let value: ModerationsResponse = {
  metadata: {
    creator: "NeosantaraAI",
  },
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |
| `model`                                                                      | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |
| `results`                                                                    | [components.ModerationResult](../../models/components/moderationresult.md)[] | :heavy_minus_sign:                                                           | N/A                                                                          |
| `metadata`                                                                   | [components.Metadata](../../models/components/metadata.md)                   | :heavy_minus_sign:                                                           | N/A                                                                          |