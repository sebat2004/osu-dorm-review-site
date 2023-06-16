require('dotenv').config();
import { OpenAI } from "./src/openai/OpenAI.js";

function displaySummary() {
  console.log("Hello world")
  let button = document.getElementById('gpt-button');
  let gptOutput = document.getElementById('gpt-output');
  button.style.display = 'none';
  gptOutput.style.display = 'flex';
  typeWriter();
  return null
}

function getSummary(reviews)
  // Creating a new instance of the OpenAI class and passing in the OPENAI_KEY environment variable
  const openAI = new OpenAI(process.env.OPEN_AI_API_KEY);
  const model = 'text-curie-001';
  const prompt = `After given reviews of a hall at Oregon State University, summarize the reviews given in three sentences or less. ${reviews}`
  // Use the generateText method to generate text from the OpenAI API and passing the generated prompt, the model and max token value
  await openAI.generateText(prompt, model, 70)
      .then(text => {
          // Logging the generated text to the console
          return text
      })
      .catch(error => {
          return "An error occurred with the AI's response."
      });
  
function typeWriter() {
  const outputTag = document.getElementById("output");
  let text = getSummary(hallID);
  let i = 0;
  let speed = 30; // 30 ms
  const intervalId = setInterval (function() {
      outputTag.innerHTML += text[i];
      i++;
      if (i === text.length) {
          clearInterval(intervalId);
      }
  }, speed);
  return null
}

