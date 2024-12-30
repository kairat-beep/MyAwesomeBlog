window.onload = function () {
  function show_second_prompt() {
    new Typed("#type2", {
      strings: ["./a.out"],
      typeSpeed: 80,
      onComplete: (self) => {
        setTimeout(() => {
          $("#type2_response").toggleClass("d-none");
          self.cursor.innerHTML = "";
        }, 500);
      }
    });
  }
  var typed = new Typed("#type1", {
    strings: ["make all"],
    typeSpeed: 80,
    onComplete: (self) => {
      setTimeout(() => {
        $("#type1_response").toggleClass("d-none");
        $("#prompt2").toggleClass("d-none");
        self.cursor.innerHTML = "";
        show_second_prompt();
      }, 400);
    }
  });
};

