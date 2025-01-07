# Folio: A Portfolio that **Speaks** for Itself, *literally*

Welcome to **Folio**,
the portfolio of **Syed Addan**, a ***Machine Learning Engineer*** who loves blending creativity with cutting-edge technology. 🚀

---

What's Special About Folio? I am glad you asked! 🎉

## For the Normal Folks 🧑‍🤝‍🧑

Imagine a portfolio that ***talks***. With Folio, you can ask the Voice AI anything about Syed’s work, skills, or projects—and it will answer truthfully, just like having a friendly conversation.

Here’s why Folio stands out:

- **A Conversational Portfolio**: No need to *read walls of text*. Simply ask, and the Voice AI will do the rest!
- **Smart Search**: Whether you're curious about his resume or LinkedIn, Folio finds the right answers from the right place.
- **Smooth & Interactive**: Hover over buttons to preview resources or dive deeper by clicking. It's simple, fun, and modern!

### **Why the need for Folio?**

Because it’s proof that Syed doesn’t just understand technology—he makes it work in delightful, practical ways.

If you’d like to connect:

- [LinkedIn](https://linkedin.com/in/syedaddan)
- [Discord](https://discordapp.com/users/557548825154420737)
- [Email](mailto:syedaddan@gmail.com)

---

## For the Abnormal Species called Developers 🧑‍💻

If you’re still scrolling, you’ve unlocked a little treasure: the "how" behind Folio. 🛠️

### The Tech Behind the Magic

Folio is built to impress both technically and visually:

#### **Frontend**

The client is developed in [**Next.js**](https://nextjs.org/) using a boilerplate template provided by LiveKit for creating WebRTC-enabled applications. I customized this client to align with the goals of Folio, adding features like:

- A clean, user-friendly interface.
- Smooth animations and hover previews for resources.
- Integration with the Voice AI to enable conversational interaction.

#### **Backend**

Folio is powered by **two servers**:

1. **Application Server**:
   - This is where all the magic happens. It handles the application logic and manages the context documents for answering user queries.
   - It includes a **pipeline** defining services and models for:
     - **LLM (Language Model)**: For generating conversational responses. Used: ***llama-3.1-8b-instant*** from **groq**.
     - **STT (Speech-to-Text)**: To process user audio input. Used: ***nova-2-conversationalai*** from **deepgram**.
     - **TTS (Text-to-Speech)**: To generate voice responses. Used: ***eleven_turbo_v2_5*** from **elevenlabs**.
     - **VAD (Voice Activity Detection)**: For detecting when a user is speaking. Used: ***silero-vad*** from **silero**.
     - **Turn Detection**: To manage conversational flow. Used: ***turn_detector*** from **livekit**.
     - **RAG (Retrieval-Augmented Generation)**: For accurate, context-driven answers. Used: *still in development*.
     - **Web Searching**: To fetch external information dynamically. Used: ***web search*** from **exa.ai**.
     - **Function Calls**: To execute specific actions based on user queries. Used: ***inbuilt function calls*** from **livekit**.
   - **Hosting**: Deployed on **Microsoft Azure** (for now), with plans to migrate after free credits run out.

2. **LiveKit Server**:
   - Built by **LiveKit**, this server leverages their WebRTC framework to handle real-time audio and video pipelines.
   - This server is hosted on **LiveKit's own cloud**, ensuring low-latency communication and high-quality audio/video streams.
   - It’s optimized for low-latency communication, making it perfect for a smooth conversational experience.
   - My application server integrates with LiveKit's environment using the **LiveKit Python SDK**.

### Expect These Features in Folio

- **AI Pipeline**: Speech-to-text, natural language processing, and text-to-speech combine for an engaging Voice AI experience.
- **Search Intelligence**: Contextual search leverages LLMs to find relevant info from Syed's resume or LinkedIn.
- **Animations**: Dynamic previews and transitions keep the experience fresh and engaging.

### Want to Build Something Similar?

If you’re inspired by Folio and want to create something like it, here’s a step-by-step guide:  

1. **Set Up the Servers**:  
   - Use Python for your application server to define the pipeline and handle business logic.  
   - Deploy a LiveKit server for managing real-time audio/video streams.  

2. **Integrate AI Models**:  
   - Choose models/services for STT, TTS, and LLM. Open-source options like Whisper, FastSpeech, and GPT-based models are a good starting point.  
   - Use a RAG framework to ensure accurate, context-aware responses.  

3. **Build the Client**:  
   - Start with LiveKit's Next.js boilerplate and customize it to match your vision.  
   - Add features like animations, previews, and smooth navigation.  

4. **Deploy the Application**:  
   - Containerize your servers using Docker for easy deployment.  
   - Host on a cloud provider (e.g., Azure, AWS, or DigitalOcean) for scalability.  

5. **Iterate and Innovate**:  
   - Continuously refine your pipeline and client to improve performance and user experience.

## Easter Egg 🥚

If you’ve scrolled this far, you’re officially in the secret club. Remember, every line of code is a little step toward magic. 🚀

---

Folio is more than a portfolio—it’s Syed Addan's story, told in the most engaging way possible.
Whether you’re here to hire or to learn, welcome aboard! 🌟
