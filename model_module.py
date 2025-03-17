
# Import necessary libraries
import torch

# Load the model and tokenizer
model = torch.load('model.pt')
tokenizer = torch.load('tokenizer.pt')

def process_input(user_input, max_new_tokens=300):
    """Process user input through the model and return the result."""
    messages = [{"role": "user", "content": user_input}]
    
    # Apply chat template and generate response
    input_tensor = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
    outputs = model.generate(input_tensor, max_new_tokens=max_new_tokens, pad_token_id=tokenizer.eos_token_id)
    result = tokenizer.decode(outputs[0][input_tensor.shape[1]:], skip_special_tokens=True)
    
    return result
