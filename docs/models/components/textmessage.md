# TextMessage

## Example Usage

```typescript
import { TextMessage } from "neosantara-ai/models/components";

let value: TextMessage = {
  role: "user",
  content: "<value>",
};
```

## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `role`                                             | [components.Role](../../models/components/role.md) | :heavy_check_mark:                                 | N/A                                                |
| `content`                                          | *string*                                           | :heavy_check_mark:                                 | N/A                                                |
| `name`                                             | *string*                                           | :heavy_minus_sign:                                 | N/A                                                |
| `toolCallId`                                       | *string*                                           | :heavy_minus_sign:                                 | N/A                                                |