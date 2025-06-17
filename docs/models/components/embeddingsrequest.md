# EmbeddingsRequest

Request untuk embeddings.

## Example Usage

```typescript
import { EmbeddingsRequest } from "neosantara-ai/models/components";

let value: EmbeddingsRequest = {
  model: "nusantara-embeddings",
  input: "contoh kalimat",
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `model`                                                                | *string*                                                               | :heavy_minus_sign:                                                     | Nama model embeddings                                                  | nusantara-embeddings                                                   |
| `input`                                                                | *components.Input*                                                     | :heavy_check_mark:                                                     | Text atau array text untuk diembedding                                 |                                                                        |
| `encodingFormat`                                                       | [components.EncodingFormat](../../models/components/encodingformat.md) | :heavy_minus_sign:                                                     | Format encoding output                                                 |                                                                        |