# ModelsResponse

## Example Usage

```typescript
import { ModelsResponse } from "openapi";

let value: ModelsResponse = {
  object: "list",
  data: [
    {
      id: "nusantara-base",
      object: "model",
      ownedBy: "nusantaraai",
      description: "Model dasar NusantaraAI",
      capabilities: [
        "chat",
        "completion",
        "reasoning",
      ],
    },
  ],
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

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `object`                                     | *string*                                     | :heavy_minus_sign:                           | N/A                                          | list                                         |
| `data`                                       | [models.ModelInfo](../models/modelinfo.md)[] | :heavy_minus_sign:                           | N/A                                          |                                              |
| `metadata`                                   | [models.Metadata](../models/metadata.md)     | :heavy_minus_sign:                           | Metadata response dari NusantaraAI.          |                                              |