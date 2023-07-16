import streamlit as st
import boto3
import json

global region
global ENDPOINT

region = "us-east-2"


# Create a Boto3 client for sagemaker
sagemaker_client = boto3.session.Session().client("sagemaker-runtime", region_name = region)

# define the SageMaker Model Endpoint
ENDPOINT = "huggingface-pytorch-tgi-inference-2023-07-16-14-08-59-732"




def generate_response(prompt):
    
    # set up model parameters
    parameters = {
    "do_sample": True,
    "top_p": 0.7,
    "temperature": 0.3,
    "top_k": 50,
    "max_new_tokens": 512,
    "repetition_penalty": 1.03
    }
    
    # create the payload
    payload = {
        "inputs": prompt,
        "parameters": parameters
    }
    
    try:
        # send the request to the sagemaker endpoint
        output = sagemaker_client.invoke_endpoint(
            EndpointName=ENDPOINT, 
            ContentType="application/json", 
            Body= json.dumps(payload))
    
        # parse the results
        response = json.loads(output["Body"].read().decode("utf-8"))
        return response[0]["generated_text"]
    
    except Exception as e:
        response = "Error: {}".format(str(e))
        return response
                            

        
# define the streamlit app
def main():
    # set up the streamlit app
    st.title("Chat")
    st.write("Enter your question or prompt and click 'Generate' to get a response")
    
    # get user prompt
    prompt = st.text_area("Enter your question or prompt")
    
    # generate and display the article
    if st.button("Generate"):
        if prompt:
            response = generate_response(prompt)
            st.subheader("Generated Response")
            st.write(response)
        else:
            st.warning("Please enter your question or prompt")
          
    
    
# run the streamlit app
if __name__ == "__main__":
    main()
    
     