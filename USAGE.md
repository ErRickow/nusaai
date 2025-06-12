<!-- Start SDK Example Usage [usage] -->
```typescript
import { Nusa } from "nusaai";

const nusa = new Nusa({
  apiKeyAuth: process.env["NUSA_XYZ_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await nusa.chat.chatCompletions({
    model: "nusantara-base",
    messages: [
      {
        role: "user",
        content: "Apa itu NusantaraAI?",
      },
    ],
  });

  console.log(result);
}

run();

```
<!-- End SDK Example Usage [usage] -->