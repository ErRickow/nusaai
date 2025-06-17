# ChatCompletionsResponse

Response chat completion.

## Example Usage

```typescript
import { ChatCompletionsResponse } from "neosantara-ai/models/components";

let value: ChatCompletionsResponse = {
  id: "chatcmpl-xyz",
  object: "chat.completion",
  created: 1717950000,
  model: "nusantara-base",
  choices: [
    {
      message: {
        role: "assistant",
        content: "NusantaraAI adalah platform AI lokal.",
      },
      finishReason: "stop",
    },
  ],
  usage: {
    promptTokens: 12,
    completionTokens: 5,
    totalTokens: 17,
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

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        | chatcmpl-xyz                                               |
| `object`                                                   | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        | chat.completion                                            |
| `created`                                                  | *number*                                                   | :heavy_minus_sign:                                         | N/A                                                        | 1717950000                                                 |
| `model`                                                    | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        | nusantara-base                                             |
| `choices`                                                  | [components.Choices](../../models/components/choices.md)[] | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `usage`                                                    | [components.Usage](../../models/components/usage.md)       | :heavy_minus_sign:                                         | N/A                                                        |                                                            |
| `metadata`                                                 | [components.Metadata](../../models/components/metadata.md) | :heavy_minus_sign:                                         | Metadata response dari NusantaraAI.                        |                                                            |