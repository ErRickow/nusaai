# System

## Example Usage

```typescript
import { System } from "openapi";

let value: System = {
  status: "operational",
  version: "1.0.0",
};
```

## Fields

| Field              | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `status`           | *string*           | :heavy_minus_sign: | N/A                | operational        |
| `version`          | *string*           | :heavy_minus_sign: | N/A                | 1.0.0              |
| `uptime`           | *number*           | :heavy_minus_sign: | Uptime dalam detik |                    |
| `modelsAvailable`  | *string*[]         | :heavy_minus_sign: | N/A                |                    |