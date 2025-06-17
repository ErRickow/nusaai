# RateLimitErrorError

## Example Usage

```typescript
import { RateLimitErrorError } from "neosantara-ai/models/errors";

let value: RateLimitErrorError = {
  message: "Too many requests. Limit: 10 RPM. Please try again later.",
  type: "rate_limit_exceeded",
  code: "rpm_exceeded",
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `message`                                                                    | *string*                                                                     | :heavy_check_mark:                                                           | N/A                                                                          | Too many requests. Limit: 10 RPM. Please try again later.                    |
| `type`                                                                       | *string*                                                                     | :heavy_check_mark:                                                           | N/A                                                                          | rate_limit_exceeded                                                          |
| `code`                                                                       | *string*                                                                     | :heavy_check_mark:                                                           | N/A                                                                          | rpm_exceeded                                                                 |
| `details`                                                                    | [errors.RateLimitErrorDetails](../../models/errors/ratelimiterrordetails.md) | :heavy_minus_sign:                                                           | Detail informasi rate limit                                                  |                                                                              |