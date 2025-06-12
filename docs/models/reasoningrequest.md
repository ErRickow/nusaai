# ReasoningRequest

## Example Usage

```typescript
import { ReasoningRequest } from "openapi";

let value: ReasoningRequest = {
  model: "nusantara-base",
  messages: [],
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `model`                                                                              | *string*                                                                             | :heavy_minus_sign:                                                                   | Model yang digunakan                                                                 | nusantara-base                                                                       |
| `messages`                                                                           | [models.ReasoningRequestMessage](../models/reasoningrequestmessage.md)[]             | :heavy_check_mark:                                                                   | N/A                                                                                  |                                                                                      |
| `temperature`                                                                        | *number*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `maxTokens`                                                                          | *number*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `stream`                                                                             | *boolean*                                                                            | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `topP`                                                                               | *number*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `frequencyPenalty`                                                                   | *number*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `presencePenalty`                                                                    | *number*                                                                             | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |
| `responseFormat`                                                                     | [models.ReasoningRequestResponseFormat](../models/reasoningrequestresponseformat.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |                                                                                      |