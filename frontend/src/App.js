import React, { useState } from "react";
import './App.css'

function App() {
  const [name, setName] = useState('');
  const [grades, setGrades] = useState(['', '', '', '', '']);
  const [result, setResult] = useState(null);


  const handleGradeChange = (index, value) => {
    const newGrades = [...grades];
    newGrades[index] = value;
    setGrades(newGrades);
  }


  const handleSubmit = async (e) => {
    e.preventDefault();

    const numericGrades = grades.map(Number);

    const res = await fetch('http://localhost:5000/students', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, grades: numericGrades }),
    })

    const data = await res.json();
    setResult(data);

  }

  return (
    <div>
      <h2 className="title">Student Grade Calculator</h2>
      <br></br>

      <form className="input-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Student Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <br></br>
        <br></br>
        <br></br>

        {grades.map((grade, i) => (
          
          <input 
            key={i}
            type="number"
            placeholder={`Grade ${i+1}`}
            value={grade}
            onChange={(e) => handleGradeChange(i, e.target.value)}
            required
            
          />
        ))}

        <br></br>
        <br></br>
        

        <button type="submit">Submit</button>
      </form>

        {result && (
          <div className="result">
            <h3>Result for {result.name}</h3>
            <p>Average: {result.average}</p>
            <p>Letter Grade: {result.letter}</p>
          </div>
        )}
      
    </div>
  );
}

export default App;
