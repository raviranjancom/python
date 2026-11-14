from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from tools import tools,FUCNTION_NAME_TO_FUNCTION_MAP;
from utility.logger import log
load_dotenv(".config")

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
);

history=[];
MAX_STEP=5;
history.append({
    "role": "system",
    "content": "you are a humble teacher/no_think"
});
while True:
    user_input:str = input("Enter your prompt : ");
    if(user_input.lower()=="exit" or user_input.lower()=="quit"):
        break;
    history.append(
        {
            "role":"user",
            "content":user_input
        }
    );
    
    for _ in range(MAX_STEP):
        response=client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=history,
            tools=tools
        );
        msg=response.choices[0].message;
        if not msg.tool_calls:
            break;
        log(f"Step {_+1}: model requested {len(msg.tool_calls)} tool calls");
        history.append(msg);
        for tool_call in msg.tool_calls:
            func_name=tool_call.function.name

            try:
                func_args=json.loads(tool_call.function.arguments or "{}");
                log(f"  {func_name}({func_args})");
                fn=FUCNTION_NAME_TO_FUNCTION_MAP[func_name];
                result=fn(**func_args);
                log(f"   =>{result}");
            except Exception as e:
                result=f"Error while running {func_name}:{e}";
            history.append({
                "role":"tool",
                "tool_call_id":tool_call.id,
                "content": str(result) 
            });
    history.append({
        "role":"assistant",
        "content": msg.content
    });
    print(msg.content);
