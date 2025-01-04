$(document).ready(function () {
  function getBotResponse() {
    var selectedModel = $("#select-model").val();
    var rawText = $("#textInput").val();
    var formattedRawText = rawText.replace(/\n/g, "<br>");
    var userHtml =
      '<p class="userText"><span>' + formattedRawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    updateTextareaHeight();
    document
      .querySelector("#chatbox")
      .lastChild.scrollIntoView({ behavior: "smooth" });
    updateTextPlaceholder("Under Processing ...", true);
    $.ajax({
      url: "/getChatBotResponse",
      type: "put",
      dataType: "json",
      contentType: "application/json",
      data: JSON.stringify({
        model: selectedModel,
        prompt: rawText,
      }),
      success: function (data) {
        var formattedData = data.replace(/\n/g, "<br>");
        var botHtml =
          '<p class="botText"><span>' + formattedData + "</span></p>";
        $("#chatbox").append(botHtml);
        updateTextareaHeight();
        document
          .querySelector("#chatbox")
          .lastChild.scrollIntoView({ behavior: "smooth" });
        updateTextPlaceholder("Type your message", false);
      },
      error: function () {
        console.log("error", data);
        alert("error ChatGPT Gatekeeper...");
      },
    });
  }
  function resetChatModel() {
    var selectedModel = $("#select-model").val();
    $.ajax({
      url: "/resetChatModel",
      type: "put",
      dataType: "json",
      contentType: "application/json",
      data: JSON.stringify({
        model: selectedModel,
      }),
      success: function (data) {
        console.log("success", data);
      },
      error: function () {
        console.log("error", data);
        alert("error ChatGPT Gatekeeper...");
      },
    });
  }
  function updateTextPlaceholder(new_placeholder, disable_placeholder) {
    var textarea = document.getElementById("textInput");
    textarea.placeholder = new_placeholder;
    textarea.disabled = disable_placeholder;
    if (!disable_placeholder) {
      textarea.classList.remove("wait-animation");
      textarea.focus();
    } else {
      textarea.classList.add("wait-animation");
    }
  }
  function updateTextareaHeight() {
    var textarea = $("#textInput");
    textarea.height(0); // Reset the height to auto
    var newHeight = textarea.prop("scrollHeight");
    textarea.height(newHeight);
  }
  function eraseChat() {
    $("#chatbox").empty();
    resetChatModel();
  }
  $("#textInput").on("input", function () {
    updateTextareaHeight();
  });
  $("#textInput").keydown(function (event) {
    if (event.key === "Enter") {
      if (event.shiftKey) {
        event.preventDefault();
        let textarea = document.getElementById("textInput");
        textarea.value += "\n";
        updateTextareaHeight();
      } else {
        event.preventDefault();
        getBotResponse();
      }
    }
  });
  $("#buttonInput").click(function () {
    getBotResponse();
  });
  $("#deleteChatButton").click(function () {
    eraseChat();
  });
  $("#select-model").change(function () {
    eraseChat();
  });
});
