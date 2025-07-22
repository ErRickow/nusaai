# ChatMessage

## Example Usage

```typescript
import { ChatMessage } from "neosantara-ai/models/components";

let value: ChatMessage = {
  role: "user",
  content: "<value>",
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `role`                                                                   | [components.ChatMessageRole](../../models/components/chatmessagerole.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `content`                                                                | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `name`                                                                   | *string*                                                                 | :heavy_minus_sign:                                                       | N/A                                                                      |
| `toolCallId`                                                             | *string*                                                                 | :heavy_minus_sign:                                                       | N/A                                                                      |