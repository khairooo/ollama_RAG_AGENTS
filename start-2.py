import ollama


### response = ollama.list()

### print(response)

# Example of using a specific model
##====================
# CHAT EXAMPLE 
#==============================

#res = ollama.chat(
#    model = "llama3.2",
 #   messages = [{"role":"user","content":"Why the sky is blue?"},])

#print(res["message"]["content"])

##==================
# GENERATE EXAMPLE 
##============================

res2 = ollama.generate(
    model = "ollama3.2",
    prompt = "Why the Sky is blue",
    max_tokens = 200
)

print(ollama.show("ollama3.2", res2["id"]))