# EmbeddingsResponse

## Example Usage

```typescript
import { EmbeddingsResponse } from "neosantara-ai/models/components";

let value: EmbeddingsResponse = {
  object: "list",
  data: [
    {
      object: "embedding",
    },
  ],
  metadata: {
    creator: "NeosantaraAI",
  },
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `object`                                                                   | *string*                                                                   | :heavy_minus_sign:                                                         | N/A                                                                        | list                                                                       |
| `data`                                                                     | [components.EmbeddingObject](../../models/components/embeddingobject.md)[] | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |
| `model`                                                                    | *string*                                                                   | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |
| `usage`                                                                    | [components.EmbeddingUsage](../../models/components/embeddingusage.md)     | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |
| `metadata`                                                                 | [components.Metadata](../../models/components/metadata.md)                 | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |