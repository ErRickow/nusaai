# Usage
(*usage*)

## Overview

Usage statistics

### Available Operations

* [usage](#usage) - Get usage statistics

## usage

Mendapatkan statistik penggunaan API.

### Example Usage

```typescript
import { Nusa } from "nusaai";

const nusa = new Nusa({
  apiKeyAuth: process.env["NUSA_XYZ_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await nusa.usage.usage();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { NusaCore } from "nusaai/core.js";
import { usageUsage } from "nusaai/funcs/usageUsage.js";

// Use `NusaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const nusa = new NusaCore({
  apiKeyAuth: process.env["NUSA_XYZ_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await usageUsage(nusa);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("usageUsage failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.UsageRequest](../../models/operations/usagerequest.md)                                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.UsageResponse](../../models/components/usageresponse.md)\>**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.AuthError | 401              | application/json |
| errors.SDKError  | 4XX, 5XX         | \*/\*            |