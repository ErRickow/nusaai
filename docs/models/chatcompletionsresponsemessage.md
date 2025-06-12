# ChatCompletionsResponseMessage

## Example Usage

```typescript
import { ChatCompletionsResponseMessage } from "openapi";

let value: ChatCompletionsResponseMessage = {
  role: "assistant",
  content: "NusantaraAI adalah platform AI lokal.",
};
```

## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `role`                                     | *string*                                   | :heavy_minus_sign:                         | N/A                                        | assistant                                  |
| `content`                                  | *string*                                   | :heavy_minus_sign:                         | N/A                                        | NusantaraAI adalah platform AI lokal.      |
| `toolCalls`                                | [models.ToolCall](../models/toolcall.md)[] | :heavy_minus_sign:                         | N/A                                        |                                            |