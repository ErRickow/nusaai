# ChatCompletionsResponseChoice

## Example Usage

```typescript
import { ChatCompletionsResponseChoice } from "openapi";

let value: ChatCompletionsResponseChoice = {
  message: {
    role: "assistant",
    content: "NusantaraAI adalah platform AI lokal.",
  },
  finishReason: "stop",
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `index`                                                                              | *number*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `message`                                                                            | [models.ChatCompletionsResponseMessage](../models/chatcompletionsresponsemessage.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `finishReason`                                                                       | *string*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  | stop                                                                                 |