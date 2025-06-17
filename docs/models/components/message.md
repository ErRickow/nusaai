# Message

## Example Usage

```typescript
import { Message } from "neosantara-ai/models/components";

let value: Message = {
  role: "assistant",
  content: "NusantaraAI adalah platform AI lokal.",
};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `role`                                                         | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            | assistant                                                      |
| `content`                                                      | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            | NusantaraAI adalah platform AI lokal.                          |
| `toolCalls`                                                    | [components.ToolCalls](../../models/components/toolcalls.md)[] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |