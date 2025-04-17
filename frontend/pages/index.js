
import { useState } from 'react';

export default function Home() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleDetect = async () => {
    setLoading(true);
    setResult(null);
    try {
      const res = await fetch('http://localhost:8000/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error('Detection failed:', err);
      setResult({ verdict: 'Error', confidence: 0, entropy_score: 0, flagged_sentences: [] });
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadReport = async () => {
    try {
      const res = await fetch('http://localhost:8000/download_report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      const blob = await res.blob();
      const url = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'ai_detection_report.pdf');
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
    } catch (err) {
      console.error('Failed to download report:', err);
    }
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '800px', margin: 'auto', fontFamily: 'sans-serif' }}>
      <h1>RealText AI Detector</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={10}
        placeholder="Paste text here..."
        style={{ width: '100%', padding: '1rem', fontSize: '1rem' }}
      />
      <button onClick={handleDetect} disabled={loading} style={{ marginTop: '1rem', padding: '0.5rem 1rem' }}>
        {loading ? 'Analyzing...' : 'Detect AI'}
      </button>

      {result && (
        <div style={{ marginTop: '2rem', backgroundColor: '#f9f9f9', padding: '1rem', borderRadius: '6px' }}>
          <h2>Verdict: {result.verdict}</h2>
          <p><strong>Confidence:</strong> {result.confidence}%</p>
          <p><strong>Entropy Score:</strong> {result.entropy_score}</p>
          <h3>Flagged Sentences:</h3>
          <ul>
            {result.flagged_sentences.map((sentence, index) => (
              <li key={index}>{sentence}</li>
            ))}
          </ul>
          <button onClick={handleDownloadReport} style={{ marginTop: '1rem', padding: '0.5rem 1rem' }}>
            Download Report as PDF
          </button>
        </div>
      )}
    </div>
  );
}
