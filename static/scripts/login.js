const form = document.querySelector("form");
const errorMessage = document.getElementById("errorMessage");
if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username-input").value;
    const password = document.getElementById("password-input").value;

    if (username == "" || password == "") {
      errorMessage.textContent = "You must fill in all the fields.";
      errorMessage.style.display = "block";
      return;
    }

    const response = await fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",

      },
      body: JSON.stringify({ username, password }),
    });

    const result = await response.json();
    console.log(result);
    if (result.status == "success") {
      localStorage.setItem("authToken", result.token);
      localStorage.setItem("isLoggedIn", "true");
      window.location.href = "/doc";
    } else if (result.message == "Missing data") {
      errorMessage.textContent = "Missing data";
      errorMessage.style.display = "block";
    } else if (result.message == "Icorrect username or password") {
      errorMessage.textContent = "Incorrect username or password";
      errorMessage.style.display = "block";
      password.value = "";
    } else if (result.message == "Internal server error") {
      errorMessage.textContent = "Internal server error";
      errorMessage.style.display = "block";
    } else {
      console.log(result);
    }
  });
}
