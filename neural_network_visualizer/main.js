import p5 from 'p5'
import './style.css'

let network = {
   layers: [{
      layer: []
   }]
}

function clear() {
   document.getElementById("net").value = "";
}

function readData() {
   let nn = document.getElementById("net").value;
   console.log(JSON.parse(nn.replaceAll("'", '"')))
   network = JSON.parse(nn.replaceAll("'", '"'))
}

let spacingx = 80;
let spacingy = 50;
let size = 25;
let yoffset = 100;
let xoffset = 0;
let strokeWeight = 1;

const sketch = (s) => {
   s.setup = () => {
      s.createCanvas(s.windowWidth, s.windowHeight);
      s.background([0x2b, 0x2a, 0x33])
   }

   s.draw = () => {
      s.clear()


      for (let j = 1; j < network.layers.length; j++) {
         let offset = s.height - (network.layers[j].layer.length * spacingy);
         for (let i = 0; i < network.layers[j].layer.length; i++) {
            for (let k = 0; k < network.layers[j - 1].layer.length; k++) {
               if (network.layers[j].layer[i].weights[k] > 0) {
                  s.stroke([0, network.layers[j].layer[i].weights[k] * 256, 0])
               }
               else {
                  s.stroke([0, 0, Math.abs(network.layers[j].layer[i].weights[k]) * 256])
               }
               let offset2 = s.height - (network.layers[j - 1].layer.length * spacingy);
               s.line(
                  (j * spacingx) + yoffset,
                  (i * spacingy) + offset / 2 + xoffset,
                  ((j - 1) * spacingx) + yoffset,
                  (k * spacingy) + offset2 / 2 + xoffset
               )
               s.stroke(0)
            }
         }
      }

      // Draw nodes
      for (let j = 0; j < network.layers.length; j++) {

         let offset = s.height - (network.layers[j].layer.length * spacingy);

         for (let i = 0; i < network.layers[j].layer.length; i++) {

            s.fill([0, -network.layers[j].layer[i].value * 256, network.layers[j].layer[i].value * 256])
            s.circle((j * spacingx) + yoffset, (i * spacingy) + offset / 2 + xoffset, size);

         }
      }

   }

   s.keyPressed = function () {
      if (s.keyCode == s.RIGHT_ARROW) {
         yoffset += 50
      }
      if (s.keyCode == s.LEFT_ARROW) {
         yoffset -= 50
      }
      if (s.keyCode == s.UP_ARROW) {
         xoffset -= 50
      }
      if (s.keyCode == s.DOWN_ARROW) {
         xoffset += 50
      }
      if (s.keyCode == s.SHIFT) {
         strokeWeight += 1;
         s.strokeWeight(strokeWeight)
      }
      if (s.keyCode == s.CONTROL) {
         strokeWeight -= 1;
         s.strokeWeight(strokeWeight)
      }
   }

   s.mouseDragged = function () {
      const xDelta = s.mouseX - s.pmouseX;
      const yDelta = s.mouseY - s.pmouseY;

      xoffset += yDelta;
      yoffset += xDelta;
   }

   s.mouseWheel = (fxn) => {
      if (fxn.delta < 0) {
         spacingx *= 1.1;
         spacingy *= 1.1;
         size *= 1.1;
         //yoffset *= 0.9
      }
      else {
         spacingx *= 0.9;
         spacingy *= 0.9;
         //yoffset *= 1.1
         size *= 0.9;
      }
   }
}

document.getElementById("btn").addEventListener('click', readData);
document.getElementById("clear").addEventListener('click', clear)

new p5(sketch)
