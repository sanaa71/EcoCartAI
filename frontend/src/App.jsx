import { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    category: "",
    material: "",
    weight_g: "",
    packaging: "",
    recyclable: "",
    reusable: "",
    durability_years: "",
    certification: "",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const calculateEcoScore = async (e) => {
    e.preventDefault();

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...formData,
          weight_g: Number(formData.weight_g),
          durability_years: Number(formData.durability_years),
        }),
      });

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error(error);
      setResult({
        error: "Unable to connect to Eco-Cart AI server.",
      });
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="container">

        <h1>🌱 Eco-Cart AI</h1>

        <p className="subtitle">
          AI-Powered Sustainable Product Evaluation
        </p>

        <form onSubmit={calculateEcoScore}>

          <label>Category</label>
          <input
            name="category"
            value={formData.category}
            onChange={handleChange}
            placeholder="e.g. Kitchen"
            required
          />

          <label>Material</label>
          <input
            name="material"
            value={formData.material}
            onChange={handleChange}
            placeholder="e.g. Bamboo"
            required
          />

          <label>Weight (grams)</label>
          <input
            type="number"
            name="weight_g"
            value={formData.weight_g}
            onChange={handleChange}
            placeholder="e.g. 300"
            required
          />

          <label>Packaging</label>
          <select
            name="packaging"
            value={formData.packaging}
            onChange={handleChange}
            required
          >
            <option value="">Select packaging</option>
            <option value="Minimal Packaging">Minimal Packaging</option>
            <option value="Compostable">Compostable</option>
            <option value="Recycled Cardboard">Recycled Cardboard</option>
            <option value="Paper">Paper</option>
            <option value="Cardboard">Cardboard</option>
            <option value="Glass">Glass</option>
            <option value="Plastic">Plastic</option>
          </select>

          <label>Recyclable</label>
          <select
            name="recyclable"
            value={formData.recyclable}
            onChange={handleChange}
            required
          >
            <option value="">Select</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>

          <label>Reusable</label>
          <select
            name="reusable"
            value={formData.reusable}
            onChange={handleChange}
            required
          >
            <option value="">Select</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>

          <label>Durability (years)</label>
          <input
            type="number"
            step="0.5"
            name="durability_years"
            value={formData.durability_years}
            onChange={handleChange}
            placeholder="e.g. 8"
            required
          />

          <label>Certification</label>
          <select
            name="certification"
            value={formData.certification}
            onChange={handleChange}
            required
          >
            <option value="">Select certification</option>
            <option value="FSC">FSC</option>
            <option value="GOTS">GOTS</option>
            <option value="USDA Organic">USDA Organic</option>
            <option value="Fair Trade">Fair Trade</option>
            <option value="OEKO-TEX">OEKO-TEX</option>
            <option value="B Corp">B Corp</option>
            <option value="Energy Star">Energy Star</option>
            <option value="None">None</option>
          </select>

          <button type="submit" disabled={loading}>
            {loading ? "Calculating..." : "🌱 Calculate Eco Score"}
          </button>

        </form>

        {result && (
          <div className="result">

            {result.error ? (
              <p className="error">{result.error}</p>
            ) : (
              <>
                <h2>Eco Score</h2>

                <div className="score">
                  {result.eco_score}/100
                </div>

                <h3>{result.level}</h3>
              </>
            )}

          </div>
        )}

      </div>
    </div>
  );
}

export default App;