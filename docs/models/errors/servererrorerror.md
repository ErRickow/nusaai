# ServerErrorError

## Example Usage

```typescript
import { ServerErrorError } from "neosantara-ai/models/errors";

let value: ServerErrorError = {
  message: "<value>",
  type: "server_error",
  code: "internal_error",
};
```

## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `message`                                                        | *string*                                                         | :heavy_check_mark:                                               | N/A                                                              |                                                                  |
| `type`                                                           | *string*                                                         | :heavy_check_mark:                                               | N/A                                                              | server_error                                                     |
| `code`                                                           | [errors.ServerErrorCode](../../models/errors/servererrorcode.md) | :heavy_check_mark:                                               | N/A                                                              | internal_error                                                   |
| `details`                                                        | Record<string, *any*>                                            | :heavy_minus_sign:                                               | N/A                                                              |                                                                  |