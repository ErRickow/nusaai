# ServerErrorError

## Example Usage

```typescript
import { ServerErrorError } from "openapi";

let value: ServerErrorError = {
  message: "Internal server error. Please try again later.",
  type: "server_error",
  code: "internal_error",
};
```

## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `message`                                      | *string*                                       | :heavy_check_mark:                             | N/A                                            | Internal server error. Please try again later. |
| `type`                                         | *string*                                       | :heavy_check_mark:                             | N/A                                            | server_error                                   |
| `code`                                         | *string*                                       | :heavy_check_mark:                             | N/A                                            | internal_error                                 |