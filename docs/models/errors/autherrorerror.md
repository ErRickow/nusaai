# AuthErrorError

## Example Usage

```typescript
import { AuthErrorError } from "neosantara-ai/models/errors";

let value: AuthErrorError = {
  message: "<value>",
  type: "auth_error",
  code: "invalid_api_key",
};
```

## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `message`                                                    | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |                                                              |
| `type`                                                       | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          | auth_error                                                   |
| `code`                                                       | [errors.AuthErrorCode](../../models/errors/autherrorcode.md) | :heavy_check_mark:                                           | N/A                                                          | invalid_api_key                                              |
| `details`                                                    | Record<string, *any*>                                        | :heavy_minus_sign:                                           | N/A                                                          |                                                              |