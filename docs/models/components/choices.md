# Choices

## Example Usage

```typescript
import { Choices } from "neosantara-ai/models/components";

let value: Choices = {
  message: {
    role: "assistant",
    content: "NusantaraAI adalah platform AI lokal.",
  },
  finishReason: "stop",
};
```

## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `index`                                                  | *number*                                                 | :heavy_minus_sign:                                       | N/A                                                      |                                                          |
| `message`                                                | [components.Message](../../models/components/message.md) | :heavy_minus_sign:                                       | N/A                                                      |                                                          |
| `finishReason`                                           | *string*                                                 | :heavy_minus_sign:                                       | N/A                                                      | stop                                                     |