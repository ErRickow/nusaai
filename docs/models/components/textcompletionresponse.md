# TextCompletionResponse

## Example Usage

```typescript
import { TextCompletionResponse } from "neosantara-ai/models/components";

let value: TextCompletionResponse = {
  object: "text_completion",
  metadata: {
    creator: "nusantaraai",
    status: true,
    timestamp: new Date("2025-06-09T16:00:00Z"),
    requestId: "req_abc123",
    processingTime: 1.234,
  },
};
```

## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                   | *string*                                                                                               | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `object`                                                                                               | *string*                                                                                               | :heavy_minus_sign:                                                                                     | N/A                                                                                                    | text_completion                                                                                        |
| `created`                                                                                              | *number*                                                                                               | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `model`                                                                                                | *string*                                                                                               | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `choices`                                                                                              | [components.TextCompletionResponseChoices](../../models/components/textcompletionresponsechoices.md)[] | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `usage`                                                                                                | [components.TextCompletionResponseUsage](../../models/components/textcompletionresponseusage.md)       | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |
| `metadata`                                                                                             | [components.Metadata](../../models/components/metadata.md)                                             | :heavy_minus_sign:                                                                                     | Metadata response dari NusantaraAI.                                                                    |                                                                                                        |