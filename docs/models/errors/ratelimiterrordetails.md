# RateLimitErrorDetails

Detail informasi rate limit

## Example Usage

```typescript
import { RateLimitErrorDetails } from "neosantara-ai/models/errors";

let value: RateLimitErrorDetails = {};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `limit`                                                                                       | *number*                                                                                      | :heavy_minus_sign:                                                                            | Batas maksimal                                                                                |
| `remaining`                                                                                   | *number*                                                                                      | :heavy_minus_sign:                                                                            | Sisa kuota                                                                                    |
| `reset`                                                                                       | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_minus_sign:                                                                            | Waktu reset limit                                                                             |
| `retryAfter`                                                                                  | *number*                                                                                      | :heavy_minus_sign:                                                                            | Retry setelah berapa detik                                                                    |