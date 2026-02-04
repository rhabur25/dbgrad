import gradio as gr

def f(x, y):
    return x + y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            app_input = gr.Number(label = "Type a number")
            app_input2 = gr.Number(label = "Type another number")
        with gr.Column():
            app_output = gr.Number(label = "This is the sum of the two numbers")

    app_input.change(fn=f, inputs=[app_input, app_input2], outputs=[app_output])

iface.launch()