import { useState } from "react";
import "./App.css";

// ─── Quick-pick keyword chips shown on the UI ───────────────────────────────
const CHIP_GROUPS = [
  { label: "Category",  chips: ["dress", "tops", "shoes", "bags", "accessories"] },
  { label: "Vibe",      chips: ["cute", "minimalist", "glam", "chic", "cozy", "edgy"] },
  { label: "Colour",    chips: ["black", "white", "blue", "pink", "red", "beige", "green", "yellow"] },
  { label: "Season",    chips: ["summer", "winter", "spring", "fall"] },
  { label: "Occasion",  chips: ["casual", "formal", "party", "sports", "travel"] },
];

const API = "http://localhost:5000";

// ─── Single outfit card ─────────────────────────────────────────────────────
function OutfitCard({ item }) {
  const [imgError, setImgError] = useState(false);

  return (
    <div style={s.card}>
      {imgError ? (
        <div style={s.imgFallback}>No Image</div>
      ) : (
        <img
          src={`${API}${item.image_url}`}
          alt={item.name}
          style={s.cardImg}
          onError={() => setImgError(true)}
        />
      )}
      <div style={s.cardBody}>
        <p style={s.cardName}>{item.name}</p>
        <div style={s.tagRow}>
          {[item.season, item.usage, item.color].map(t => (
            <span key={t} style={s.tag}>{t}</span>
          ))}
        </div>
        <p style={s.similarity}>Match: {Math.round(item.similarity * 100)}%</p>
      </div>
    </div>
  );
}

// ─── Main app ───────────────────────────────────────────────────────────────
export default function App() {
  const [text,       setText]       = useState("");
  const [selected,   setSelected]   = useState([]);
  const [results,    setResults]    = useState([]);
  const [loading,    setLoading]    = useState(false);
  const [error,      setError]      = useState("");
  const [searched,   setSearched]   = useState(false);

  // Toggle a quick-pick chip
  const toggleChip = (chip) =>
    setSelected(prev =>
      prev.includes(chip) ? prev.filter(c => c !== chip) : [...prev, chip]
    );

  // Keep the free-text phrase intact so the backend can recognize phrases
  // such as "smart casual", "navy blue", and "off white".
  const buildKeywords = () => {
    const freeText = text.trim().toLowerCase();
    return freeText ? [...selected, freeText] : selected;
  };

  const handleSearch = async () => {
    const keywords = buildKeywords();
    if (!keywords.length) {
      setError("Pick at least one keyword or type something.");
      return;
    }

    setLoading(true);
    setError("");
    setSearched(true);

    try {
      const res = await fetch(`${API}/api/recommend`, {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ keywords, n: 8 }),
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      setResults(data.results ?? []);
    } catch (err) {
      setError(err.message || "Could not connect to backend. Is Flask running?");
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setText(""); setSelected([]); setResults([]);
    setError(""); setSearched(false);
  };

  return (
    <div style={s.page}>
      {/* ── Header ── */}
      <header style={s.header}>
        <h1 style={s.title}>✨Outfit Recommender✨</h1>
        <p style={s.sub}>Describe your vibe—we'll find your look.</p>
      </header>

      {/* ── Keyword chips ── */}
      <div style={s.chipSection}>
        {CHIP_GROUPS.map(({ label, chips }) => (
          <div key={label} style={s.chipGroup}>
            <span style={s.chipGroupLabel}>{label}</span>
            <div style={s.chipRow}>
              {chips.map(chip => (
                <button
                  key={chip}
                  onClick={() => toggleChip(chip)}
                  style={{
                    ...s.chip,
                    ...(selected.includes(chip) ? s.chipOn : {}),
                  }}
                >
                  {chip}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* ── Free-text input ── */}
      <div style={s.inputRow}>
        <input
          style={s.input}
          type="text"
          placeholder='Add more keywords, e.g. "navy midi dress"'
          value={text}
          onChange={e => setText(e.target.value)}
          onKeyDown={e => e.key === "Enter" && handleSearch()}
        />
        <button style={s.btn} onClick={handleSearch} disabled={loading}>
          {loading ? "Searching…" : "Find Outfits"}
        </button>
        {searched && (
          <button style={{ ...s.btn, ...s.btnGhost }} onClick={handleClear}>
            Clear
          </button>
        )}
      </div>

      {/* ── Active keyword pills ── */}
      {buildKeywords().length > 0 && (
        <p style={s.activeLabel}>
          Searching for: {buildKeywords().map(k => (
            <strong key={k}> #{k}</strong>
          ))}
        </p>
      )}

      {/* ── Errors ── */}
      {error && <p style={s.error}>{error}</p>}

      {/* ── Results grid ── */}
      {results.length > 0 && (
        <>
          <p style={s.resultCount}>{results.length} outfits found</p>
          <div style={s.grid}>
            {results.map(item => <OutfitCard key={item.id} item={item} />)}
          </div>
        </>
      )}

      {searched && !loading && results.length === 0 && !error && (
        <p style={s.empty}>No outfits matched. Try different keywords!</p>
      )}
    </div>
  );
}

// ─── Styles ─────────────────────────────────────────────────────────────────
const s = {
  page:            { maxWidth: 1000, margin: "0 auto", padding: "2rem 1rem", fontFamily: "system-ui, sans-serif" },
  header:          { textAlign: "center", marginBottom: "1.5rem" },
  title:           { fontSize: "2rem", margin: 0, color: "#000" },
  sub:             { color: "#666", margin: "0.25rem 0 0" },

  chipSection:     { display: "flex", flexDirection: "column", gap: "0.6rem", marginBottom: "1.2rem" },
  chipGroup:       { display: "flex", alignItems: "center", gap: "0.5rem", flexWrap: "wrap" },
  chipGroupLabel:  { minWidth: 72, fontSize: "0.75rem", fontWeight: 600, color: "#888", textTransform: "uppercase" },
  chipRow:         { display: "flex", gap: "0.4rem", flexWrap: "wrap" },
  chip:            { padding: "0.35rem 0.85rem", border: "1.5px solid #ddd", borderRadius: 999, background: "#fff", color: "#333", cursor: "pointer", fontSize: "0.82rem", transition: "all 0.15s" },
  chipOn:          { background: "#111827", color: "#fff", border: "1.5px solid #111827" },

  inputRow:        { display: "flex", gap: "0.5rem", marginBottom: "0.75rem", flexWrap: "wrap" },
  input:           { flex: 1, minWidth: 200, padding: "0.6rem 1rem", border: "1.5px solid #ddd", borderRadius: 8, fontSize: "0.95rem", background: "#f5f5dc", color: "#333" },
  btn:             { padding: "0.6rem 1.4rem", background: "#111827", color: "#fff", border: "none", borderRadius: 8, cursor: "pointer", fontSize: "0.95rem", whiteSpace: "nowrap" },
  btnGhost:        { background: "#fff", color: "#111827", border: "1.5px solid #ddd" },

  activeLabel:     { fontSize: "0.85rem", color: "#555", marginBottom: "0.5rem" },
  error:           { color: "#c0392b", textAlign: "center", margin: "1rem 0" },
  resultCount:     { fontSize: "0.85rem", color: "#888", marginBottom: "0.75rem" },
  empty:           { textAlign: "center", color: "#999", marginTop: "2rem" },

  grid:            { display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(210px, 1fr))", gap: "1rem" },
  card:            { border: "1px solid #eee", borderRadius: 12, overflow: "hidden", background: "#fff", boxShadow: "0 2px 10px rgba(0,0,0,0.06)", display: "flex", flexDirection: "column" },
  cardImg:         { width: "100%", height: 250, objectFit: "cover" },
  imgFallback:     { width: "100%", height: 250, background: "#f5f5f5", display: "flex", alignItems: "center", justifyContent: "center", color: "#aaa", fontSize: "0.85rem" },
  cardBody:        { padding: "0.75rem", flex: 1 },
  cardName:        { fontSize: "0.82rem", fontWeight: 500, margin: "0 0 0.5rem", color: "#222", lineHeight: 1.4 },
  tagRow:          { display: "flex", gap: "0.3rem", flexWrap: "wrap", marginBottom: "0.4rem" },
  tag:             { fontSize: "0.68rem", background: "#f3f4f6", padding: "0.2rem 0.5rem", borderRadius: 99, color: "#555" },
  similarity:      { fontSize: "0.72rem", color: "#888", margin: 0 },
};
