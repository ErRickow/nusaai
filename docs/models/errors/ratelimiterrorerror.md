# RateLimitErrorError

## Example Usage

```typescript
import { RateLimitErrorError } from "neosantara-ai/models/errors";

let value: RateLimitErrorError = {
  message: "<value>",
  type: "rate_limit_exceeded",
  code: "rpm_exceeded",
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `message`                                                                  | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `type`                                                                     | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        | rate_limit_exceeded                                                        |
| `code`                                                                     | [errors.RateLimitErrorCode](../../models/errors/ratelimiterrorcode.md)     | :heavy_check_mark:                                                         | N/A                                                                        | rpm_exceeded                                                               |
| `details`                                                                  | [components.RateLimitDetails](../../models/components/ratelimitdetails.md) | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |