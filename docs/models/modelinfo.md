# ModelInfo

## Example Usage

```typescript
import { ModelInfo } from "openapi";

let value: ModelInfo = {
  id: "nusantara-base",
  object: "model",
  ownedBy: "nusantaraai",
  description: "Model dasar NusantaraAI",
  capabilities: [
    "chat",
    "completion",
    "reasoning",
  ],
};
```

## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `id`                                           | *string*                                       | :heavy_minus_sign:                             | N/A                                            | nusantara-base                                 |
| `object`                                       | *string*                                       | :heavy_minus_sign:                             | N/A                                            | model                                          |
| `created`                                      | *number*                                       | :heavy_minus_sign:                             | N/A                                            |                                                |
| `ownedBy`                                      | *string*                                       | :heavy_minus_sign:                             | N/A                                            | nusantaraai                                    |
| `permission`                                   | [models.Permission](../models/permission.md)[] | :heavy_minus_sign:                             | N/A                                            |                                                |
| `root`                                         | *string*                                       | :heavy_minus_sign:                             | N/A                                            |                                                |
| `parent`                                       | *string*                                       | :heavy_minus_sign:                             | N/A                                            |                                                |
| `description`                                  | *string*                                       | :heavy_minus_sign:                             | N/A                                            | Model dasar NusantaraAI                        |
| `capabilities`                                 | *string*[]                                     | :heavy_minus_sign:                             | N/A                                            | [<br/>"chat",<br/>"completion",<br/>"reasoning"<br/>] |