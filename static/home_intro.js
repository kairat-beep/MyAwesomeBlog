window.onload = function () {
  function show_second_prompt() {
    new Typed("#prompt2-input", {
      strings: ["./a.out"],
      typeSpeed: 80,
      onComplete: (self) => {
        setTimeout(() => {
          $("#prompt2-response").toggleClass("invisible");
          self.cursor.innerHTML = "";
        }, 500);
      }
    });
  }
  var typed = new Typed("#prompt1-input", {
    strings: ["make all"],
    typeSpeed: 80,
    onComplete: (self) => {
      setTimeout(() => {
        $("#prompt1-response").toggleClass("invisible");
        $("#prompt2").toggleClass("invisible");
        self.cursor.innerHTML = "";
        show_second_prompt();
      }, 400);
    }
  });
};

