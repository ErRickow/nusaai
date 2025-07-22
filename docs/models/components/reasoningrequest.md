# ReasoningRequest

## Example Usage

```typescript
import { ReasoningRequest } from "neosantara-ai/models/components";

let value: ReasoningRequest = {
  model: "nusantara-base",
  messages: [],
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `model`                                                                | *string*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    | nusantara-base                                                         |
| `messages`                                                             | [components.ChatMessage](../../models/components/chatmessage.md)[]     | :heavy_check_mark:                                                     | N/A                                                                    |                                                                        |
| `temperature`                                                          | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `maxTokens`                                                            | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `stream`                                                               | *boolean*                                                              | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `topP`                                                                 | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `frequencyPenalty`                                                     | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `presencePenalty`                                                      | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `responseFormat`                                                       | [components.ResponseFormat](../../models/components/responseformat.md) | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |