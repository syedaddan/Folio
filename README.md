# ✨ Folio

---

<div align="center">
	<img src="/assets/folio.gif" height="300">
</div>

<br>

<div align="center">
   <img src="/assets/made-with-python.svg">
   <img src="/assets/built-with-love.svg">
   <br>
   <img src="/assets/WIP.svg"><img src="/assets/contribute.svg"><img src="/assets/license.svg">
</div>

---

Welcome to **Folio**,
the portfolio of **Syed Addan**, a ***Machine Learning Engineer*** who loves blending creativity with cutting-edge technology. 🚀

---

## 🎉 What's Special About Folio?

Imagine a portfolio that ***talks***. With Folio, you can ask the Voice AI anything about Syed’s work, skills, or projects—and it will answer truthfully, just like having a friendly conversation.

Here’s why Folio stands out:

- **A Conversational Portfolio**: No need to *read walls of text*. Simply ask, and the Voice AI will do the rest!
- **Smart Search**: Whether you're curious about his resume or LinkedIn, Folio finds the right answers from the right place.
- **Smooth & Interactive**: Hover over buttons to preview resources or dive deeper by clicking. It’s simple, fun, and modern!

### 🌟 Why Folio?

Because it proves Syed doesn't just understand technology—he makes it work in delightful, practical ways. If you’d like to connect:

- [LinkedIn](https://linkedin.com/in/syedaddan)
- [Discord](https://discordapp.com/users/557548825154420737)
- [Email](mailto:syedaddan@gmail.com)

---

## 🧑‍💻 For the Eclectic Species called the Developers

If you’re still scrolling, you’ve unlocked a little treasure: the "how" behind Folio. 🛠️

### 💻 The Tech Behind the Magic

Folio is built to impress both technically and visually:

#### **Frontend**

Built with [**Next.js**](https://nextjs.org/), customized from LiveKit's WebRTC boilerplate. Features include:

- A clean, user-friendly interface.
- Smooth animations and hover previews for resources.
- Integration with the Voice AI for conversational interaction.

#### **Backend**

Folio is powered by **two servers**:

1. **Application Server**:
   - Handles application logic and manages the context documents for answering user queries.
   - Services include:
     - **LLM (Language Model)**: For generating conversational responses. Used: ***llama-3.1-8b-instant*** from **groq**.
     - **STT (Speech-to-Text)**: For processing user audio input. Used: ***nova-2-conversationalai*** from **deepgram**.
     - **TTS (Text-to-Speech)**: For generating voice responses. Used: ***eleven_turbo_v2_5*** from **elevenlabs**.
     - **VAD (Voice Activity Detection)**: For detecting user speech. Used: ***silero-vad*** from **silero**.
     - **Turn Detection**: To manage conversational flow. Used: ***turn_detector*** from **livekit**.
     - **RAG (Retrieval-Augmented Generation)**: For accurate, context-driven answers. Used: *still in development*.
     - **Web Searching**: To fetch external information dynamically. Used: ***web search*** from **exa.ai**.
     - **Function Calls**: For executing specific actions based on user queries. Used: ***inbuilt function calls*** from **livekit**.
   - **Hosting**: Currently deployed on **Microsoft Azure**, but will migrate once free credits expire.

2. **LiveKit Server**:
   - Leverages WebRTC for real-time audio and video communication.
   - Hosted on **LiveKit's cloud**, ensuring low-latency communication.
   - Integrated into the application using the **LiveKit Python SDK**.

### 🔥 Features to Expect

- **AI Pipeline**: Speech-to-text, natural language processing, and text-to-speech combine for an engaging Voice AI experience.
- **Search Intelligence**: Contextual search uses LLMs to find relevant info from Syed's resume or LinkedIn.
- **Animations**: Dynamic previews and transitions keep the experience fresh and engaging.

### 🚀 Want to Build Something Similar?

If Folio inspired you to create something like it, here's a guide:

1. **Set Up Servers**:
   - Use Python for your application server and deploy a LiveKit server for real-time audio/video.

2. **Integrate AI Models**:
   - Choose models for STT, TTS, and LLM. Open-source models like Whisper, FastSpeech, and GPT-based ones are great starts.

3. **Build the Client**:
   - Start with LiveKit's Next.js boilerplate, customize for smooth animations, previews, and navigation.

4. **Deploy the Application**:
   - Containerize with Docker and host on a cloud provider (e.g., Azure, AWS, DigitalOcean).

5. **Iterate and Innovate**:
   - Continuously improve your pipeline and client for a better user experience.

---

## 🥚 Easter Egg

If you've scrolled this far, you're in the secret club. Remember, every line of code is a little step toward magic. 🚀

---

Folio is more than a portfolio—it’s Syed Addan's story, told in the most engaging way possible.
Whether you’re here to hire or learn, welcome aboard! 🌟
