const mic = document.querySelector('.mic')
const recordingStatus = document.querySelector('.recording-status')
const samantha = window.speechSynthesis.getVoices().filter(voice => voice.name === 'Samantha')[0]

let isRecording = false;

mic.addEventListener('click', listenForSpeech)

function clearChatInput() {
  chatInput.value = ''
}

function sendTextChatMessage() {
  let newChat = chatInput.value
  postChatMessage(newChat)
}

function postChatMessage(response) {
  console.log("post chat function");
  res_list = document.getElementById("chat-responses"); //chat-responses should be the class of the mic button in the html.

  element_val = `
   You Said: ${response}
  `
  res_list.append(element_val);
  var respon_json = {
    "text": response
  }
  $.ajax({
    type: "POST",
    contentType: "application/json;charset=utf-8",
    url: "http://localhost:5000/print/name",
    traditional: "true",
    data: JSON.stringify(respon_json),
    dataType: "json",
    success: function (response) {
      speakResponse(response.response);
      //displayResponse(response.response);
    }
  });
}

function displayResponse(response) {
  let newChat = document.createElement('li')
  newChat.innerText = `wheeler : ${response}`
  chatMessages = document.getElementById("chat-input");
  res_list.append(newChat)
}

function speakResponse(response) {
  let utterance = new SpeechSynthesisUtterance(response);
  utterance.voice = samantha
  window.speechSynthesis.speak(utterance)
  displayResponse(response)
}

function listenForSpeech() {
  console.log(isRecording)
  if (isRecording) {
    isRecording = false
    recordingStatus.innerText = 'Speak Your Query'
    return 0;
  }
  isRecording = true
  recordingStatus.innerText = 'Listening To You'
  var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
  var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent
  var recognition = new SpeechRecognition()

  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;
  recognition.start()

  recognition.onspeechstart = function () {
    console.log('Speech has been detected');
  }

  recognition.onresult = function (event) {
    let last = event.results.length - 1;
    let speech = event.results[last][0].transcript;

    postChatMessage(speech)

    console.log('Result received: ' + speech + '.');
    console.log('Confidence: ' + event.results[0][0].confidence);
  }

  recognition.onspeechend = function () {
    recordingStatus.innerText = 'speak your querry'
    console.log('Speech has stopped being detected');
  }

  recognition.onerror = function (event) {
    console.log('Error occurred in recognition: ' + event.error);
  }
}

document.querySelector('.chat-bot-button').addEventListener('click', function () {
  console.log('clicked')
  document.querySelector('.chat-bot-modal').classList.toggle('open')
})