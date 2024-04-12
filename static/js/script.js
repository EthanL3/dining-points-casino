function spinWheel() {
  var wheel = document.getElementById("wheel");
  var degree = Math.floor(Math.random() * 360) + 1440; // Ensure at least 4 rotations
  wheel.style.transform = "rotate(" + degree + "deg)";
}
