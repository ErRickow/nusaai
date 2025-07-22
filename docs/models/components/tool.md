# Tool

## Example Usage

```typescript
import { Tool } from "neosantara-ai/models/components";

let value: Tool = {
  type: "function",
  function: {
    name: "<value>",
  },
};
```

## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `type`                                                       | [components.ToolType](../../models/components/tooltype.md)   | :heavy_check_mark:                                           | N/A                                                          |
| `function`                                                   | [components.FunctionT](../../models/components/functiont.md) | :heavy_check_mark:                                           | N/A                                                          |