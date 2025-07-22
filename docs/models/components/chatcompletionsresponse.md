# ChatCompletionsResponse

## Example Usage

```typescript
import { ChatCompletionsResponse } from "neosantara-ai/models/components";

let value: ChatCompletionsResponse = {
  object: "chat.completion",
  metadata: {
    creator: "NeosantaraAI",
  },
};
```

## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *string*                                                         | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |
| `object`                                                         | *string*                                                         | :heavy_minus_sign:                                               | N/A                                                              | chat.completion                                                  |
| `created`                                                        | *number*                                                         | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |
| `model`                                                          | *string*                                                         | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |
| `choices`                                                        | [components.ChatChoice](../../models/components/chatchoice.md)[] | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |
| `usage`                                                          | [components.Usage](../../models/components/usage.md)             | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |
| `metadata`                                                       | [components.Metadata](../../models/components/metadata.md)       | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |