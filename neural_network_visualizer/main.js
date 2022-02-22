import p5 from 'p5'
import './style.css'

let network = {
   layers: [{
      layer: []
   }]
}

function readData() {
   let nn = document.getElementById("net").value;
   console.log(JSON.parse(nn.replaceAll("'", '"')))
   network = JSON.parse(nn.replaceAll("'", '"'))
}

const spacingx = 80;
const spacingy = 50;
const size = 25;
let yoffset = 100;
let xoffset = 0;

const sketch = (s) => {
   s.setup = () => {
      s.createCanvas(1920, 800);
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
            s.circle((j * spacingx) + yoffset, (i * spacingy) + offset / 2, size);

         }
      }

   }

   function keyPressed() {
      if (s.keyCode == s.RIGHT_ARROW) {
         yoffset += 50
      }
      if (s.keyCode == s.LEFT_ARROW) {
         yoffset -= 50
      }
      if (s.keyCode == s.UP_ARROW) {
         xoffset -= 50
         console.log("bruhh")
      }
      if (s.keyCode == s.DOWN_ARROW) {
         xoffset += 50
         console.log("bruhh")
      }
   }

   s.keyPressed = keyPressed;
}

document.getElementById("btn").addEventListener('click', readData);

new p5(sketch)
