const form = document.getElementById("form");
const errorForm = document.getElementById("errorMessage");

function is_password_correct(psswrd) {}

if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username-input").value;
    const password1 = document.getElementById("password-input").value;
    const password2 = document.getElementById("confirm-password-input").value;

    if (password1 === password2 && password1 != "") {
      const response = await fetch("/api/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password: password1 }),
      });

      const result = await response.json();
      console.log(result);
      if (result.status == "success") {
        window.location.href = "/login";
      } else {
        errorForm.textContent = "Erreur lors de la création du compte.";
      }
    } else {
      errorForm.textContent = "Les mot de passes ne se correspondent pas.";
    }
  });
}
