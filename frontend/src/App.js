import React, { useState } from "react";

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
      <h2>Student Grade Calculator</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Student Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        {/* {grades.map((grade, i) => )} */}



        
      </form>
    </div>
  );
}

export default App;
