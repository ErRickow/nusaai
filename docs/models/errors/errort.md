# ErrorT

## Example Usage

```typescript
import { ErrorT } from "neosantara-ai/models/errors";

let value: ErrorT = {
  message: "Invalid request format or missing required parameters.",
  type: "bad_request",
  code: "invalid_request_format",
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `message`                                              | *string*                                               | :heavy_check_mark:                                     | N/A                                                    | Invalid request format or missing required parameters. |
| `type`                                                 | *string*                                               | :heavy_check_mark:                                     | N/A                                                    | bad_request                                            |
| `code`                                                 | *string*                                               | :heavy_check_mark:                                     | N/A                                                    | invalid_request_format                                 |
| `details`                                              | [errors.Details](../../models/errors/details.md)       | :heavy_minus_sign:                                     | Detail kesalahan request                               |                                                        |