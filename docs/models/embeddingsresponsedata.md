# EmbeddingsResponseData

## Example Usage

```typescript
import { EmbeddingsResponseData } from "openapi";

let value: EmbeddingsResponseData = {
  object: "embedding",
  embedding: [
    0.12,
    0.34,
    0.56,
  ],
  index: 0,
};
```

## Fields

| Field                | Type                 | Required             | Description          | Example              |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| `object`             | *string*             | :heavy_minus_sign:   | N/A                  | embedding            |
| `embedding`          | *number*[]           | :heavy_minus_sign:   | N/A                  | [<br/>0.12,<br/>0.34,<br/>0.56<br/>] |
| `index`              | *number*             | :heavy_minus_sign:   | N/A                  | 0                    |