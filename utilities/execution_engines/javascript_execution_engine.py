"""
project: lollms_webui
file: shell_execution_engine.py 
author: ParisNeo
description: 
    This is a utility for executing python code

"""
from lollms_webui import LOLLMSWebUI
from ascii_colors import get_trace_exception, trace_exception
import time
import subprocess
import json

lollmsElfServer:LOLLMSWebUI = LOLLMSWebUI.get_instance()          

def build_javascript_output(code, ifram_name="unnamed"):
    """
    This function creates an HTML5 iframe with the given HTML content and iframe name.

    Args:
    html (str): The HTML content to be displayed in the iframe.
    ifram_name (str, optional): The name of the iframe. Defaults to "unnamed".

    Returns:
    str: The HTML string for the iframe.
    """
    # Start the timer.
    start_time = time.time()    
    rendered =  "\n".join([
        '<div style="width: 100%; margin: 0 auto;">',
        f'<iframe id="{ifram_name}" srcdoc="',
        '<script>',
        code,
        '</script>',
        '" style="width: 100%; height: 600px; border: none;"></iframe>',
        '</div>'
        ]
    )
    execution_time = time.time() - start_time
    return {"output": rendered, "execution_time": execution_time}

def execute_javascript(code, discussion_id, message_id):
    return build_javascript_output(code)