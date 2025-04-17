<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>RealTextAI Detector</title>
  <style>
    body {
      font-family: monospace;
      background: #0d1117;
      color: #c9d1d9;
      padding: 40px;
      text-align: center;
    }
    textarea {
      width: 80%;
      height: 150px;
      margin: 20px 0;
      padding: 10px;
      background: #161b22;
      color: #fff;
      border: 1px solid #30363d;
    }
    button {
      padding: 10px 20px;
      background: #238636;
      color: white;
      border: none;
      cursor: pointer;
      font-weight: bold;
    }
    .result {
      margin-top: 30px;
      background: #161b22;
      padding: 20px;
      border: 1px solid #30363d;
    }
  </style>
</head>
<body>
  <h1>🧠 RealTextAI Detector</h1>
  <p>Paste your text below and hit <strong>Detect</strong>.</p>
  <textarea id="inputText" placeholder="Paste your text here..."></textarea><br>
  <button onclick="detectText()">Detect</button>

  <div class="result" id="resultBox" style="display:none;">
    <h2>🔍 Detection Result</h2>
    <p id="verdict"></p>
    <p id="confidence"></p>
    <p id="entropy"></p>
    <p id="flags"></p>
  </div>

  <script>
    async function detectText() {
      const text = document.getElementById("inputText").value;
      const resultBox = document.getElementById("resultBox");
      const verdict = document.getElementById("verdict");
      const confidence = document.getElementById("confidence");
      const entropy = document.getElementById("entropy");
      const flags = document.getElementById("flags");

      resultBox.style.display = "none";
      resultBox.innerHTML = "⏳ Detecting...";

      try {
        const response = await fetch("https://ai-w79h.onrender.com/detect", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ text })
        });

        const data = await response.json();

        verdict.textContent = "Verdict: " + data.verdict;
        confidence.textContent = "Confidence: " + data.confidence + "%";
        entropy.textContent = "Entropy: " + data.entropy_score;
        flags.textContent = "Flagged Sentences: " + (data.flagged_sentences?.join(" | ") || "None");

        resultBox.style.display = "block";
      } catch (err) {
        resultBox.innerHTML = "<p style='color:red;'>❌ Error contacting the AI detector.</p>";
      }
    }
  </script>
</body>
</html>
