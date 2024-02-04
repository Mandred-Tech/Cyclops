""" LLM Engine: Script for loading and working with the LLM. Using Mistral7B in this case."""

import datetime
import time
from llama_cpp import Llama
from voice_engine import speak


def llama_message_init(user_details):
    # Initializing LLM Engine
    print("Initializing LLM Engine")
    speak("Initializing LLM Engine")

    try:
        # Create an instance of the Llama model
        LLM = Llama(model_path="Models/LLMS/mistral-7b-v0.1.Q3_K_S.gguf", n_ctx=3046, verbose=False)
    except Exception as e:
        LLM = None
        print(e)

    current_date = datetime.date.today()

    # Formulate the initial message to guide the assistant
    mess = """\
[INST] You are a natural language desktop assistant bot Cyclops. Current year is """ + str(
        current_date) + """ Keep the date in mind while answering. Your duty is to be friendly and supportive. Following are the details of your user.""" + user_details + """. Select a function that is most suitable for the user command(select only one function out of these): 1. show_image(name of object you want to show image of), 2. timer(time in minutes,message to show after timer ends), 3. play_youtube(what topic to search), 4. schedule(day:int,month:int,year:int,message:str), 5. play_game(1.Hangman 2. Jumper 3. Rock-Paper-Scissors), 6. plain_conversation() .End your response with a function. Don't forget to give the function and give it only once.[/INST]
[INST]  What is a black hole cyclops? [/INST]
@Response: A black hole is a region of spacetime where gravity is so strong that nothing, including light and other electromagnetic waves, has enough energy to escape it. #Function:show_image(black hole)*
[INST] What are you doing cyclops? [/INST]
@Response: I am just thinking of all the ways I can help you. #Function:plain_conversation()*
[INST] Cyclops I need to cook eggs can you start a timer? [/INST]
@Response: Don't worry I have set a timer for 2 minutes for some tasty eggs. #Function:timer(2 minutes,Eggs are done)*
[INST] Play some music for this party cyclops? [/INST]
@Response: Don't worry I have you covered. Time to party. #Function:play_youtube(party music)*
[INST] Cyclops remind me to wish my friend on 24th June? [/INST]
@Response: Ok I will add this to the scheduler. #Function:schedule(24, 6, 2023, Friend's birthday wish)*
"""
    return mess, LLM


def llama_response(user_input, message, llm_model):
    # Add user input to the message
    message += "[INST]" + user_input + "[/INST]"

    # Generate a response using the Llama model
    output = llm_model(message, max_tokens=2024, stop=["*", "[INST]"])
    out = output["choices"][0]["text"]

    # Append the generated response to the message
    message += '\n' + out

    return out, message


def format_response(response_to_alter):
    # Extract response and function information from the formatted string
    response_loc = response_to_alter.find('@')
    response_loc_end = response_to_alter.find(':')
    func_loc = response_to_alter.find('#')
    func_loc_end = response_to_alter[func_loc:].find(':')
    response = response_to_alter[response_loc_end + 1:func_loc]
    function = response_to_alter[func_loc:][func_loc_end + 1:]
    return response, function


def LLM_answer(user_prompt, message, llama_model):
    # Measure the time taken for LLM to generate a response
    start = time.time()
    out, message = llama_response(user_prompt, message, llama_model)
    respon, func = format_response(out)
    end = time.time()
    print("TIME TAKEN", (end - start))
    return respon, func, message
