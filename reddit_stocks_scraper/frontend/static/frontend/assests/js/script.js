let i = 0;
let txt = 'Lorem ipsum typing effect!'; /* The text */
let speed = 60 * 90000000000000; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("type").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
typeWriter();