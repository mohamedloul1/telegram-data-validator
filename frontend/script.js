document.addEventListener("DOMContentLoaded", function () {
    const tg = window.Telegram.WebApp;
    tg.expand(); 

    const userInfo = document.getElementById("user-info");
    const validateBtn = document.getElementById("validate-btn");

    console.log("[LOG] Telegram WebApp loaded:", tg);

    if (tg.initDataUnsafe.user) {
        userInfo.textContent = `Hello, ${tg.initDataUnsafe.user.first_name}!`;
        console.log("[LOG] User information:", tg.initDataUnsafe.user);
    } else {
        userInfo.textContent = "No user data available.";
        console.log("[LOG] No user information available.");
    }

    validateBtn.addEventListener("click", function () {
        console.log("[LOG] Validation button clicked.");
        console.log("[LOG] Sending initData:", tg.initData);

        fetch("https://declared-jersey-nv-france.trycloudflare.com/validate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ initData: tg.initData })
        })
        .then(response => response.json())
        .then(data => {
            console.log("[LOG] Received response:", data);
            alert(data.valid ? "✅ Data valid!" : "❌ Invalid data!");
        })
        .catch(error => {
            console.error("[ERROR] Validation error:", error);
        });
    });
});
