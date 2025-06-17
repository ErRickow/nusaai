# ModerationsRequest

## Example Usage

```typescript
import { ModerationsRequest } from "neosantara-ai/models/components";

let value: ModerationsRequest = {
  input: [],
  model: "text-moderation-latest",
};
```

## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `input`                              | *components.ModerationsRequestInput* | :heavy_check_mark:                   | Text yang akan dimoderasi            |                                      |
| `model`                              | *string*                             | :heavy_minus_sign:                   | Model moderasi yang digunakan        | text-moderation-latest               |