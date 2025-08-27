// form aur result element ko grab karo
const form = document.getElementById("fraudForm");
const result = document.getElementById("result");

// form submit hone pe ye chalega
form.addEventListener("submit", function(event) {
    event.preventDefault(); // page refresh hone se rokta hai

    // input values lo
    const amount = document.getElementById("amount").value;
    const type = document.getElementById("type").value;
    const age = document.getElementById("age").value;

    // abhi dummy logic: sirf example ke liye
    let prediction;
    if (amount > 10000 && type === "online") {
        prediction = "⚠️ Fraud Detected!";
        result.style.color = "red";
    } else {
        prediction = "✅ Transaction is Legit.";
        result.style.color = "green";
    }

    // result show karo
    result.textContent = prediction;
});
