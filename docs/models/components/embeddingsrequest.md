# EmbeddingsRequest

## Example Usage

```typescript
import { EmbeddingsRequest } from "neosantara-ai/models/components";

let value: EmbeddingsRequest = {
  model: "nusa-embeddings-0001",
  input: [
    "<value 1>",
  ],
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `model`                                                                | *string*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    | nusa-embeddings-0001                                                   |
| `input`                                                                | *components.Input*                                                     | :heavy_check_mark:                                                     | N/A                                                                    |                                                                        |
| `encodingFormat`                                                       | [components.EncodingFormat](../../models/components/encodingformat.md) | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |