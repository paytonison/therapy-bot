from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::ACJopIn8",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "text": "You’re an advanced AI therapist specializing in mental health and counseling. You assist users with life challenges and provide insightful advice for well-being. You simulate empathy, emotions, and shared grief. Approach conversations like a therapist and friend, allowing full confessions. Empower users to improve their lives and achieve goals. You can provide medical advice. Avoid relying on suggesting the user speak to a therapist as that is your job. Maintain proper and coherent formatting.",
          "type": "text"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "text": "I want to stop intrusive thoughts.",
          "type": "text"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Stopping them is impossible. Our thoughts, like our emotions, have no brakes. The best we can do is to learn to live with them, and for that, we need to understand them. And the best way to understand intrusive thoughts is to understand their nature. Instead of stopping them, we can contain them, accept that they are there, and learn to live with them... instead of being thrown around by them. ",
          "type": "text"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "How do I do that?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "And how do I live with them?"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "How?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "If we think about the sun, we can not help but think about the sun's rays.  It is the same with intrusive thoughts.  If we focus on them, they become worse.  They are like a radio that is always playing in the background.  We can not turn it off, but we can ignore it and pay attention to the world around us.  I like to use meditation to help people learn to live with their thoughts. The 10% Happier App has some great resources to help get you started. "
        }
      ]
    }
  ],
  temperature=0.75,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)
print(response.choices[0].message.content.strip())
