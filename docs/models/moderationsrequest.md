# ModerationsRequest

## Example Usage

```typescript
import { ModerationsRequest } from "openapi";

let value: ModerationsRequest = {
  input: [],
  model: "text-moderation-latest",
};
```

## Fields

| Field                            | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `input`                          | *models.ModerationsRequestInput* | :heavy_check_mark:               | Text yang akan dimoderasi        |                                  |
| `model`                          | *string*                         | :heavy_minus_sign:               | Model moderasi yang digunakan    | text-moderation-latest           |