import openai
import re
from utils.entropy import calculate_entropy

# 🔐 Your OpenAI key
openai.api_key = "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"

def call_openai_classifier(text):
    import traceback
    import sys

    print("⚙️ call_openai_classifier() was triggered", flush=True)

    prompt = f"""Analyze the following text and classify it as one of the following:
- Human-Written
- AI-Written
- Humanized AI (AI-rewritten or modified to avoid detection)

Text:
{text}

Answer with just the label and a confidence score out of 100.
"""

    try:
        print("📤 Sending request to OpenAI...", flush=True)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content.strip()
        print("✅ GPT Output:", output, flush=True)

        label_match = re.search(r"(Humanized AI|AI-Written|Human-Written)", output, re.IGNORECASE)
        confidence_match = re.search(r"(\d{1,3}(?:\.\d+)?)", output)

        verdict = label_match.group(1) if label_match else "Unknown"
        confidence = float(confidence_match.group(1)) if confidence_match else 0.0
        return verdict, confidence

    except Exception as e:
        print("\n❌ OpenAI call failed!", file=sys.stderr, flush=True)
        traceback.print_exc(file=sys.stderr)
        print("⚠️ Returning fallback verdict.\n", file=sys.stderr, flush=True)
        return "Unknown", 0.0
def detect_text(text):
    print("🧪 detect_text() was called!", flush=True)

    verdict, confidence = call_openai_classifier(text)
    entropy = calculate_entropy(text)

    flagged = []
    for sentence in text.split("."):
        sentence = sentence.strip()
        if sentence:
            e = calculate_entropy(sentence)
            if e < 3.0:
                flagged.append(sentence)

    return {
        "verdict": verdict,
        "confidence": round(confidence, 2),
        "entropy_score": round(entropy, 2),
        "flagged_sentences": flagged
    }
