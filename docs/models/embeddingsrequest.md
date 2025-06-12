# EmbeddingsRequest

Request untuk embeddings.

## Example Usage

```typescript
import { EmbeddingsRequest } from "openapi";

let value: EmbeddingsRequest = {
  model: "nusantara-embeddings",
  input: "contoh kalimat",
};
```

## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `model`                                              | *string*                                             | :heavy_minus_sign:                                   | Nama model embeddings                                | nusantara-embeddings                                 |
| `input`                                              | *models.EmbeddingsRequestInput*                      | :heavy_check_mark:                                   | Text atau array text untuk diembedding               |                                                      |
| `encodingFormat`                                     | [models.EncodingFormat](../models/encodingformat.md) | :heavy_minus_sign:                                   | Format encoding output                               |                                                      |