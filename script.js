async function analyzeWaste() {

    const input = document.getElementById("wasteInput").value.trim();

    if (input === "") {
        alert("Please enter a waste item.");
        return;
    }

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                waste: input
            })
        });

        const data = await response.json();

        console.log("Server Response:", data);

        document.getElementById("category").textContent =
            data.category || "Not available";

        document.getElementById("action").textContent =
            data.action || "Not available";

        document.getElementById("recycling").textContent =
            data.recycling || "Not available";

        document.getElementById("safety").textContent =
            data.safety || "Not available";

        document.getElementById("result").style.display = "block";

    } catch (error) {

        console.error("Error:", error);

        alert("Something went wrong. Check the Flask terminal.");

    }
}