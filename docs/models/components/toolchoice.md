# ToolChoice

## Example Usage

```typescript
import { ToolChoice } from "neosantara-ai/models/components";

let value: ToolChoice = {
  type: "function",
  function: {
    name: "<value>",
  },
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | [components.ToolChoiceType](../../models/components/toolchoicetype.md)         | :heavy_check_mark:                                                             | N/A                                                                            |
| `function`                                                                     | [components.ToolChoiceFunction](../../models/components/toolchoicefunction.md) | :heavy_check_mark:                                                             | N/A                                                                            |