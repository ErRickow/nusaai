# AuthErrorError

## Example Usage

```typescript
import { AuthErrorError } from "openapi";

let value: AuthErrorError = {
  message:
    "API key is missing. Please provide your API key in the 'Authorization' header as 'Bearer <API_KEY>'.",
  type: "auth_error",
  code: "invalid_api_key",
};
```

## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `message`                                                                                            | *string*                                                                                             | :heavy_check_mark:                                                                                   | N/A                                                                                                  | API key is missing. Please provide your API key in the 'Authorization' header as 'Bearer <API_KEY>'. |
| `type`                                                                                               | *string*                                                                                             | :heavy_check_mark:                                                                                   | N/A                                                                                                  | auth_error                                                                                           |
| `code`                                                                                               | [models.Code](../models/code.md)                                                                     | :heavy_check_mark:                                                                                   | N/A                                                                                                  | invalid_api_key                                                                                      |