# ChatCompletionsRequest

Request untuk chat completion.

## Example Usage

```typescript
import { ChatCompletionsRequest } from "neosantara-ai/models/components";

let value: ChatCompletionsRequest = {
  model: "nusantara-base",
  messages: [],
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `model`                                                                | *string*                                                               | :heavy_check_mark:                                                     | Nama model (wajib).                                                    | nusantara-base                                                         |
| `messages`                                                             | [components.Messages](../../models/components/messages.md)[]           | :heavy_check_mark:                                                     | Array pesan (role+content).                                            |                                                                        |
| `temperature`                                                          | *number*                                                               | :heavy_minus_sign:                                                     | Kontrol kreativitas response                                           |                                                                        |
| `maxTokens`                                                            | *number*                                                               | :heavy_minus_sign:                                                     | Maksimal token output                                                  |                                                                        |
| `stream`                                                               | *boolean*                                                              | :heavy_minus_sign:                                                     | Stream response                                                        |                                                                        |
| `n`                                                                    | *number*                                                               | :heavy_minus_sign:                                                     | Jumlah response yang dihasilkan                                        |                                                                        |
| `topP`                                                                 | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `frequencyPenalty`                                                     | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `presencePenalty`                                                      | *number*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `responseFormat`                                                       | [components.ResponseFormat](../../models/components/responseformat.md) | :heavy_minus_sign:                                                     | N/A                                                                    |                                                                        |
| `functions`                                                            | [components.Functions](../../models/components/functions.md)[]         | :heavy_minus_sign:                                                     | Fungsi yang tersedia untuk dipanggil                                   |                                                                        |
| `tools`                                                                | [components.Tools](../../models/components/tools.md)[]                 | :heavy_minus_sign:                                                     | Tools yang tersedia                                                    |                                                                        |
| `toolChoice`                                                           | *string*                                                               | :heavy_minus_sign:                                                     | Cara pemilihan tool                                                    |                                                                        |
| `webSearch`                                                            | *boolean*                                                              | :heavy_minus_sign:                                                     | Aktifkan web search                                                    |                                                                        |