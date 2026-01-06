document.addEventListener("DOMContentLoaded", () => {
  const chatForm = document.getElementById("chatForm");
  const userInput = document.getElementById("userInput");
  const chatBox = document.getElementById("chatbox");

  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    // Add user message
    appendMessage("user", message);
    userInput.value = "";

    try {
      const response = await fetch("/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `msg=${encodeURIComponent(message)}`,
      });

      const data = await response.json();

      // Add bot message
      appendMessage("bot", data.response);
    } catch (error) {
      console.error("Error:", error);
      appendMessage("bot", "Sorry, something went wrong. Please try again.");
    }
  });

  function appendMessage(sender, text) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", `${sender}-message`);

    const contentDiv = document.createElement("div");
    contentDiv.classList.add("message-content");
    contentDiv.textContent = text;

    const timeDiv = document.createElement("div");
    timeDiv.classList.add("timestamp");
    const now = new Date();
    timeDiv.textContent = now.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    });

    messageDiv.appendChild(contentDiv);
    messageDiv.appendChild(timeDiv);

    chatBox.appendChild(messageDiv);

    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});
