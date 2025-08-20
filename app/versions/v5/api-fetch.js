const fastapiUrl = "https://pydatanova-api.onrender.com";
const flaskUrl = "https://pydatanova-api.onrender.com";
// const fastapiUrl = "http://localhost:8000";
// const flaskUrl = "http://localhost:5001";

// Helper to fetch and display response
async function fetchAndDisplay(url, outputId) {
    const outputEl = document.getElementById(outputId);
    try {
        const response = await fetch(url);
        const data = await response.json();
        outputEl.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputEl.textContent = `Error: ${err.message}`;
    }
}

// FastAPI buttons
document.getElementById("btn-fastapi-root").addEventListener("click", () => {
    fetchAndDisplay(`${fastapiUrl}/root`, "fastapi-output");
});

document.getElementById("btn-fastapi-mock").addEventListener("click", () => {
    fetchAndDisplay(`${fastapiUrl}/mock-data`, "fastapi-output");
});

// Flask buttons
document.getElementById("btn-flask-root").addEventListener("click", () => {
    fetchAndDisplay(`${flaskUrl}/root`, "flask-output");
});

document.getElementById("btn-flask-mock").addEventListener("click", () => {
    fetchAndDisplay(`${flaskUrl}/mock-data`, "flask-output");
});
