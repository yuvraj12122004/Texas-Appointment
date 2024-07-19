


<template>
  <section class="layout_container m-0 py-3">
    <div class="container">
      <div class="row">
        <div class="col-lg-4">
          <div class="audio_section p-3">
            <img src="/src/assets/plsulogo.svg" alt="LAPD" class="LAPD_logo">
            <div class="LAPD_name">
              <h3>Texas <br> Medical <br>
              Center</h3>
            </div>
            <img src="/src/assets/js/mic.svg" alt="LAPD" class="Mic">
            
            <div class="row">
              <div class="col-lg-12"> 
                <div class="text-center">
                  <div class="audio_icon my-5 pt-5">
                    <font-awesome-icon icon="fa-solid fa-microphone" />
                  </div>

                  <button type="button" @click="startListening" :disabled="isRecording" class="btn start_btn mb-4">Start Recording</button>
                  <!-- <button type="button" @click="stopRecording" :disabled="!isRecording" class="btn start_btn mb-4">Stop Recording</button> -->

                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-8">
          <div class="chat_section p-3">
            <div class="row mb-5">
              <div class="col-lg-12">
                <div class="chat_section_header">
                  <a>
                    <img class="exc me-4" src="/src/assets/images/exc_icon.svg" alt="Alert">
                  </a>
                  <a>
                    <img class="exc me-4" src="/src/assets/images/delete_icon.svg" alt="Delete">
                  </a>
                  
                  <div class="search_box">
                    <input type="text" class="form-control" placeholder="Search" aria-describedby="emailHelp" />
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" class="search-icon" />
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12">
                <div class="chat_box">
                  <div class="row">

                    <div class="col-lg-12">
                      <div class="lapd_chat d-flex align-items-start justify-content-end mb-4">
                        <div class="chat_text_div d-flex flex-column align-items-end">
                          <p>Hello, thank you for calling Texas Medical Center. How can I help you today?</p>
                        </div>
                        <div class="img-box">
                          <img src="/src/assets/images/lapd_chat.png" alt="LAPD">
                        </div>
                      </div>
                    </div>










                    <div class="col-lg-12" v-for="(items,index) in chatJson" :key="index">
                     



                        <div class="user_chat d-flex align-items-star mb-4">
                                  <div class="img-box">
                                    <img src="/src/assets/images/user-chat.png" alt="User">
                                  </div>  
                                
                                  <div class="chat_text_div" v-if="items.transcription">
                                    <p>Language detected: {{items.detectedlanguage}} </p>
                                    <p> <b>{{items.detectedlanguage}} : </b>{{items.transcription}} </p>
                                  <p> <b>English : </b>{{items.translatedtext}}</p>
                                  </div>

                                  
                        </div>



       
                          <div v-if="items.openai" class="lapd_chat d-flex align-items-start justify-content-end mb-4">
                                <div class="chat_text_div d-flex flex-column align-items-end">
                                  <!-- <p v-if="items.openairesponse[0]">{{items.openairesponse[0]}}</p> -->
                                  <p v-if="items.openai">{{items.openai}}
                                    <br>
                                    <div class="float-end sound_box" v-if="items.convertedtext">
                                      <span style="margin-right: 10px;">
                                        <font-awesome-icon icon="fa-solid fa-play"  @click="playAudio(items.convertedtext,items.detectedlanguage)" />
                                      </span>
                                      <span style="margin-right: 10px;">
                                        <font-awesome-icon icon="fa-solid fa-pause" @click="pauseAudio(items.convertedtext)"/>
                                      </span>
                                      <span>
                                        <font-awesome-icon icon="fa-solid fa-rotate-right" @click="stopAudio(items.convertedtext)" />
                                      </span>
                                    </div>
                                  </p> 
                                

                                </div>
                                <div class="img-box">
                                  <img src="/src/assets/images/lapd_chat.png" alt="LAPD">
                                </div>  
                          </div>
         
                          






                          
                     
                      <!-- <div class="user_chat d-flex align-items-star mb-4">
                                  <div class="img-box">
                                    <img src="/src/assets/images/user-chat.png" alt="User">
                                  </div>  
                                
                                  <div class="chat_text_div" v-if="transcription">
                                    <p>Language detected: {{detectedlanguage}} </p>
                                    <p> <b>{{detectedlanguage}} : </b>{{transcription}} </p>
                                  <p> <b>English : </b>{{translatedtext}}</p>
                                  </div>

                                  <div class="chat_text_div" v-if="processing">
                                    <p> Processing.... </p>
                                    </div>
                      </div>



                 
                      <div v-if="openai" class="lapd_chat d-flex align-items-start justify-content-end mb-4">
                              <div class="chat_text_div d-flex flex-column align-items-end">
                                <p v-if="openairesponse[0]">{{openairesponse[0]}}</p>
                                <p v-if="openairesponse[1]">{{openairesponse[1]}}
                                  <br>
                                  <div class="float-end sound_box" v-if="convertedtext">
                                    <span style="margin-right: 10px;">
                                      <font-awesome-icon icon="fa-solid fa-play"  @click="playAudio(convertedtext,detectedlanguage)" />
                                    </span>
                                    <span style="margin-right: 10px;">
                                      <font-awesome-icon icon="fa-solid fa-pause" @click="pauseAudio(convertedtext)"/>
                                    </span>
                                    <span>
                                      <font-awesome-icon icon="fa-solid fa-rotate-right" @click="stopAudio(convertedtext)" />
                                    </span>
                                  </div>
                                </p> 
                              

                              </div>
                              <div class="img-box">
                                <img src="/src/assets/images/lapd_chat.png" alt="LAPD">
                              </div>  
                      </div>
                    -->




                    </div>




                      
                    <div class="user_chat d-flex align-items-star mb-4" v-if="processing">
                      <div class="img-box">
                        <img src="/src/assets/images/user-chat.png" alt="User">
                      </div>  
                    
                      <div class="chat_text_div" >
                        Processing...
                      </div>

                      
                 </div>


                    
                  </div>
                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<style scoped>

</style>


<script>


import { COMMON_API_HTTP } from './api/axiosConfig';



export default {
  data() {
    return {
      isRecording: false,
      recordingStop: true,
      mediaRecorder: null,
      audioChunks: [],
      audioBlob: null,
      transcription: '',
      translatedtext:'',
      openai:'',
      detectedlanguage:'',
      processing:false,
      convertedtext:'',
      isPaused: false,
      speechSynthesisUtterance: null,
      play:true,
      pause:false,
      play2:false,
      chatJson:[],
      recognition: null,
      silenceTimeout: null,
      audioStream: null
    };
  },
  created: function () {
    // this.chatJson.push({
    //   openai: "Welcome to 911 emergency, how can i help you?",
    //   convertedtext: "Welcome to 911 emergency, how can i help you?",
    //   openairesponse: ["Welcome to 911 emergency, how can i help you?"]
    // });
    // console.log(this.chatJson);
    this.stopAudio()
    this.playAudio("Hello, Thank you for calling the Texas Medical Center. How can I help you today?","en","Hello, Thank you for calling the Texas Medical Center. How can I help you today?");
  },


 
  methods: {
    clearFields() {
      this.transcription = '';
      this.translatedtext = '';
      this.openai = '';
      this.detectedlanguage = '';
      this.processing = false;
      this.convertedtext = '';
      this.speechSynthesisUtterance = null;
      this.chatJson = [];
    },
    async startListening() {
      try {
        this.isRecording = true;
        this.recordingStop = false;
        this.audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        this.recognition.continuous = true;
        this.recognition.interimResults = false;
 
        this.recognition.onresult = (event) => {
          clearTimeout(this.silenceTimeout);
          this.silenceTimeout = setTimeout(() => {
            this.processing = true
            this.isRecording = true;
            this.recordingStop = true;
            this.stopRecording();
          }, 1000); // Stop after 1 seconds of silence
        };
 
        this.recognition.onend = () => {
          if (this.isRecording) {
            this.startRecording(); // Restart recording if still in recording mode
          }
        };
 
        this.recognition.start();
        this.startRecording();
 
      } catch (err) {
        console.error('Error accessing media devices.', err);
      }
    },
    startRecording() {
      this.isRecording = true;
      // this.recordingStop = false;
      this.mediaRecorder = new MediaRecorder(this.audioStream);
      this.mediaRecorder.start();
 
      this.mediaRecorder.ondataavailable = (event) => {
        this.audioChunks.push(event.data);
      };
 
      this.mediaRecorder.onstop = () => {
        this.audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        this.audioChunks = [];
 
        this.uploadRecording();
      };
 
    },
    stopRecording() {
      if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
        this.mediaRecorder.stop();
 
      }
    },
    stopListening() {
      if (this.recognition) {
        this.recognition.stop();
      }
      this.stopRecording();
    },
    async uploadRecording() {
      if (this.chatJson.length > 0) {
        this.chathistoryjsonString = JSON.stringify(this.chatJson);
      } else {
        this.chathistoryjsonString = JSON.stringify("");
      }
 
      if (!this.audioBlob) return;
 
      const formData = new FormData();
      formData.append('file', this.audioBlob, 'audio.wav');
      formData.append('chathistory', this.chathistoryjsonString);
 
      try {
        const response = await COMMON_API_HTTP.post('/transcribe/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.processing = false;
        console.log(response);
 
        this.transcription = response.data.transcription;
        this.translatedtext = response.data.translatedtext;
        this.openai = response.data.openai;
        this.detectedlanguage = response.data.detectedlanguage;
        this.convertedtext = response.data.convertedtext;
 
        console.log(this.openai);
        this.openairesponse = this.openai.split('\n\n');
        console.log(this.openairesponse);
 
        this.chatJson.push({
          transcription: this.transcription,
          translatedtext: this.translatedtext,
          openai: this.openai,
          detectedlanguage: this.detectedlanguage,
          convertedtext: this.convertedtext,
          openairesponse: this.openairesponse,
        });
        this.isRecording = false;
        if (this.convertedtext.includes('We have redirected your call to')) {
          this.isRecording = false;
        }
        console.log(this.chatJson);
        await this.playAudio(this.openairesponse, this.detectedlanguage, this.convertedtext);
        // this.startListening();
      } catch (error) {
        this.processing = false;
        console.error('Error uploading audio file.', error);
      }
    },
    async playAudio(text, detectedlanguage, AiEnglishResponse) {
      try {
        this.stopListening()
        console.log("play audio : " + text);
        if (!text) {
          console.log('Please enter some text');
          return;
        }
 
        if (this.isPaused && this.speechSynthesisUtterance) {
          window.speechSynthesis.resume();
          this.isPaused = false;
          return;
        }
 
        this.speechSynthesisUtterance = new SpeechSynthesisUtterance(text);

        if (AiEnglishResponse.includes('We have redirected your call to')) {
            console.log("Reached line 381")
        }
 
        // Retrieve the list of available voices
        let voices = window.speechSynthesis.getVoices();
 
        while (voices.length === 0) {
          voices = window.speechSynthesis.getVoices();
          await new Promise(resolve => setTimeout(resolve,1000));
        }
 
        //Find a female voice
        const ziraVoice = voices.find(voice => voice.name === 'Microsoft Zira - English (United States)');

    if (ziraVoice) {
    this.speechSynthesisUtterance.voice = ziraVoice;
  }   else {
    console.log('Microsoft Zira voice not found, using default voice');
}




        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const mediaStreamDestination = audioContext.createMediaStreamDestination();
        const mediaRecorder = new MediaRecorder(mediaStreamDestination.stream);
        let audioChunks = [];
 
        mediaRecorder.ondataavailable = (event) => {
          audioChunks.push(event.data);
        };
 
        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
          this.audioUrl = URL.createObjectURL(audioBlob);
        };
 
        if (AiEnglishResponse.includes('We have redirected your call to')) {
          console.log(this.speechSynthesisUtterance)
          console.log("Reached line 418")
        }



        mediaRecorder.start();

        if (AiEnglishResponse.includes('We have redirected your call to')) {
            console.log("Reached line 426")
            console.log(this.speechSynthesisUtterance)
        }


        window.speechSynthesis.speak(this.speechSynthesisUtterance);

        
        if (AiEnglishResponse.includes('We have redirected your call to')) {
            console.log("Reached line 434")
        }


 
        this.speechSynthesisUtterance.onend = () => {
          // mediaRecorder.stop();
          // this.isRecording = false;
          this.recordingStop = true;
          if (!AiEnglishResponse.includes('We have redirected your call to')) {
            this.startListening();
          }
        };
 
      } catch (error) {
        console.log(error);
      }
    },

    pauseAudio() {
      if (window.speechSynthesis.speaking && !this.isPaused) {
        window.speechSynthesis.pause();
        this.isPaused = true;
      } else if (this.isPaused) {
        window.speechSynthesis.resume();
        this.isPaused = false;
      }
      this.startListening()
    },
    stopAudio() {
      window.speechSynthesis.cancel();
      if (this.mediaRecorder && this.mediaRecorder.state === 'recording') {
        this.mediaRecorder.stop();
        this.startListening()
 
      }
      this.isPaused = false;
 
    }
  }
 


};
</script>

<style scoped>
button {
  margin: 5px;
}
</style>
