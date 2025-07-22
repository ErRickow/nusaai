# ImageMessage

## Example Usage

```typescript
import { ImageMessage } from "neosantara-ai/models/components";

let value: ImageMessage = {
  type: "image_url",
  imageUrl: {
    url: "https://well-made-councilman.org/",
  },
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `type`                                                     | [components.Type](../../models/components/type.md)         | :heavy_check_mark:                                         | N/A                                                        |
| `imageUrl`                                                 | [components.ImageUrl](../../models/components/imageurl.md) | :heavy_check_mark:                                         | N/A                                                        |