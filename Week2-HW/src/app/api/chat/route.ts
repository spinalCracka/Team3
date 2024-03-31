import OpenAI from 'openai';
import { OpenAIStream, StreamingTextResponse } from 'ai';

// Create an OpenAI API client (that's edge friendly!)
const openai = new OpenAI({
	apiKey: process.env.OPENAI_API_KEY,
	//for local model testing only, remove if want to test via cloud api:
	baseURL: `http://127.0.0.1:5000/v1`,
});

// IMPORTANT! Set the runtime to edge
export const runtime = 'edge';

export async function POST(req: Request) {
	const { messages, temperature } = await req.json();

	console.log("temperature passed from client to  server side:"+ Number(temperature))
	// Ask OpenAI for a streaming chat completion given the prompt
	const response = await openai.chat.completions.create({
		model: 'gpt-3.5-turbo',
		stream: true,
		//messages,
		messages: [
			{
				role: "system", 
				content: "You are a professional comedian who can create jokes for the user based on the joke parameters the user sends. He will send you the topic of the joke, the tone the joke should be in, and the type of joke it should be (like a knock-knock joke, or a joke involving a pun, or a joke involving a story)."
			},
			...messages
		],
		temperature: Number(temperature)
	});

	// Convert the response into a friendly text-stream
	const stream = OpenAIStream(response);
	// Respond with the stream
	return new StreamingTextResponse(stream);
}
