# ModelsListResponse

## Example Usage

```typescript
import { ModelsListResponse } from "neosantara-ai/models/components";

let value: ModelsListResponse = {
  object: "list",
  data: [
    {
      object: "model",
      ownedBy: "NeosantaraAI",
      pricing: {
        currency: "USD",
      },
    },
  ],
  metadata: {
    creator: "NeosantaraAI",
  },
};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `object`                                                       | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            | list                                                           |
| `data`                                                         | [components.ModelInfo](../../models/components/modelinfo.md)[] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |
| `metadata`                                                     | [components.Metadata](../../models/components/metadata.md)     | :heavy_minus_sign:                                             | N/A                                                            |                                                                |