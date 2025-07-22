# ErrorT

## Example Usage

```typescript
import { ErrorT } from "neosantara-ai/models/errors";

let value: ErrorT = {
  message: "<value>",
  type: "invalid_request_error",
  code: "invalid_parameter",
};
```

## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `message`                                  | *string*                                   | :heavy_check_mark:                         | N/A                                        |                                            |
| `type`                                     | *string*                                   | :heavy_check_mark:                         | N/A                                        | invalid_request_error                      |
| `code`                                     | [errors.Code](../../models/errors/code.md) | :heavy_check_mark:                         | N/A                                        | invalid_parameter                          |
| `param`                                    | *string*                                   | :heavy_minus_sign:                         | N/A                                        |                                            |
| `details`                                  | Record<string, *any*>                      | :heavy_minus_sign:                         | N/A                                        |                                            |