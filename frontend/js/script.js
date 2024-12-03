
document.getElementById("calculateButton").addEventListener("click", function() {
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    const weight = document.getElementById("weight").value;
    const height = document.getElementById("height").value;
    const activity = document.getElementById("activity").value;
    const goal = document.getElementById("goal").value;

    // Placeholder for API integration
    fetch("http://localhost:5000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ age, gender, weight, height, activity, goal }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("calories").textContent = `Calories: ${data.calories} kcal`;
        document.getElementById("macros").textContent = `Macros: Protein ${data.protein}g, Carbs ${data.carbs}g, Fat ${data.fat}g`;
    })
    .catch(err => console.error(err));
});
