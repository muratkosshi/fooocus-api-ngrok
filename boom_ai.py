import gradio as gr
import gradio
import requests

def send_request(data, url):
    response = requests.post(url, json=data)
    return response.json()

def api_interface(url):
    return gr.Interface(
        send_request,
        [gradio.inputs.Textbox(label="JSON"), gradio.inputs.Textbox(label="API URL")],
        "json",
        title="API Interface",
        description="Enter JSON data to send to the API",
        examples=[
            [{"example_key": "example_value"}],
            [{"another_key": "another_value"}]
        ],
        args={
            "url": gradio.inputs.Textbox(label="http://127.0.0.1:8888/v1/generation/text-to-image")
        }
    )

if __name__ == "__main__":
    api_interface("http://localhost:8888").launch()
