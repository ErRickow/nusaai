# EmbeddingsResponse

Response dari embeddings endpoint.

## Example Usage

```typescript
import { EmbeddingsResponse } from "neosantara-ai/models/components";

let value: EmbeddingsResponse = {
  object: "list",
  data: [
    {
      object: "embedding",
      embedding: [
        0.12,
        0.34,
        0.56,
      ],
      index: 0,
    },
  ],
  model: "nusantara-embeddings",
  usage: {
    promptTokens: 3,
    totalTokens: 3,
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

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `object`                                                                                 | *string*                                                                                 | :heavy_minus_sign:                                                                       | N/A                                                                                      | list                                                                                     |
| `data`                                                                                   | [components.Data](../../models/components/data.md)[]                                     | :heavy_minus_sign:                                                                       | N/A                                                                                      |                                                                                          |
| `model`                                                                                  | *string*                                                                                 | :heavy_minus_sign:                                                                       | N/A                                                                                      | nusantara-embeddings                                                                     |
| `usage`                                                                                  | [components.EmbeddingsResponseUsage](../../models/components/embeddingsresponseusage.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |                                                                                          |
| `metadata`                                                                               | [components.Metadata](../../models/components/metadata.md)                               | :heavy_minus_sign:                                                                       | Metadata response dari NusantaraAI.                                                      |                                                                                          |