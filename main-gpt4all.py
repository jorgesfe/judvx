import eel
import threading
from gpt4all import GPT4All

model = GPT4All("llama-2-7b-chat.ggmlv3.q4_0.bin")

message: str = ''
response: str = ''
chat_session = []
thinks = []


def generate_message(chat_message):
    global response
    global model
    global chat_session
    global message
    response = ''
    with model.chat_session(system_prompt="[INST]<<SYS>>The assistant acts like JudVx, who is an artificial intelligence;"
                                          "Never act like the user;"
                                          "JudVx always wants to help the user in any problem;<</SYS>>[/INST]",
                            prompt_template="[INST]{0}[/INST]"):
        if len(chat_session) > 0:
            model.current_chat_session = chat_session
        output = model.generate(chat_message, max_tokens=1000, n_batch=128, temp=0.8, streaming=True)
        for value in output:
            response = response + value
        response = response + '[HAPPY_ENDING]'
        print("Chat session at the end: ", model.current_chat_session)


@eel.expose
def send_message(chat_message):
    global message
    message = chat_message
    generate_thread = threading.Thread(target=generate_message, args=[chat_message])
    generate_thread.start()


@eel.expose
def read_message():
    global response
    return response

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('web', allowed_extensions=['.js', '.html'])

eel.start('index.html')             # Start (this blocks and enters loop)