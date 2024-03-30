"use client";

import { useChat } from "ai/react";
import { useEffect, useRef, useState } from "react";

export default function Chat() {

  const [topicOfJoke, setTopicOfJoke] = useState('work'); 
  const [toneOfJoke, setToneOfJoke] = useState('witty'); 
  const [kindOfJoke, setKindOfJoke] = useState('pun'); 
  const [jokeTemperature, setJokeTemperature] = useState('0.50'); 

  const {
    messages,
    input,
    handleInputChange,
    handleSubmit,
    isLoading,
    append,
  } = useChat({
    body: { temperature: jokeTemperature }
  });

  const messagesContainerRef = useRef<HTMLDivElement>(null);


  useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="flex flex-col w-full h-screen max-w-md py-24 mx-auto stretch">
      <div className="overflow-auto mb-8 w-full" ref={messagesContainerRef}>
        {messages.map((m) => (
          <div
            key={m.id}
            className={`whitespace-pre-wrap ${
              m.role === "user"
                ? "bg-green-700 p-3 m-2 rounded-lg"
                : "bg-slate-700 p-3 m-2 rounded-lg"
            }`}
          >
            {m.role === "user" ? "User: " : "AI: "}
            {m.content}
          </div>
        ))}

        {isLoading && (
          <div className="flex justify-end pr-4">
            <span className="animate-bounce">...</span>
          </div>
        )}
      </div>
      <div className="fixed bottom-0 w-full max-w-md">
        <div className="flex flex-col justify-center mb-2 items-center">

        <select
          value={topicOfJoke} // ...force the select's value to match the state variable...
          onChange={e => setTopicOfJoke(e.target.value)} // ... and update the state variable on any change!
        >
          <option value="work">work</option>
          <option value="people">people</option>
          <option value="animals">animals</option>
          <option value="food">food</option>
          <option value="television">television</option>
        </select>
        <select
          value={toneOfJoke} // ...force the select's value to match the state variable...
          onChange={e => setToneOfJoke(e.target.value)} // ... and update the state variable on any change!
        >
          <option value="witty">witty</option>
          <option value="sarcastic">sarcastic</option>
          <option value="silly">silly</option>
          <option value="dark">dark</option>
          <option value="goofy">goofy</option>
        </select>
        <select
          value={kindOfJoke} // ...force the select's value to match the state variable...
          onChange={e => setKindOfJoke(e.target.value)} // ... and update the state variable on any change!
        >
          <option value="knock-knock">knock-knock</option>
          <option value="pun">pun</option>
          <option value="story">story</option>
        </select>
        <input type="number" value={jokeTemperature}         
          onChange={e => setJokeTemperature(e.target.value)} 
          min="0" max="1" step=".05"/>

          
          <button
            className="bg-blue-500 disabled:bg-grey-500 p-2 text-white rounded shadow-xl"
            disabled={isLoading}
            onClick={() => {
              console.log (topicOfJoke);
              console.log(kindOfJoke);
              console.log(toneOfJoke);
              console.log(jokeTemperature);
              append({ 
                role: "user", 
                content: `Give me a joke about ${topicOfJoke}. The type of the joke should be a ${kindOfJoke}. It should have a tone of ${toneOfJoke}` 
               ,temperature: 0.90
              });
              }
            }
          >
            Get me a joke with the above parameters  
          </button>
          Info: {isLoading ? 'true' : 'false'}<br/>
          UI fields: {topicOfJoke}, <br/>{toneOfJoke}, <br/>{kindOfJoke}, <br/>{jokeTemperature}
        </div>
        {/*
        <form onSubmit={handleSubmit} className="flex justify-center">
          <input
            className="w-[95%] p-2 mb-8 border border-gray-300 rounded shadow-xl text-black"
            disabled={isLoading}
            value={input}
            placeholder="Say something..."
            onChange={handleInputChange}
          />
        </form>
        */}
      </div>
    </div>
  );
}