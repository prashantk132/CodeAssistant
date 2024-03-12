import requests
import json
import gradio as gr

# backend
url="http://localhost:11434/api/generate"


headers={

    'Content-Type':'application/json'

}
history=[]
def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)
    data={
        "model":"codeguru",
        "prompt":final_prompt,
        "stream":False  # if it is true then it will give lot of unnecessary values
    }
    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


# frontend
interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter Your Prompt"),
    outputs="text"
)
interface.launch()