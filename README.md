# llm-serving-with-vastai
This repository contains some code and notes on how to serve example LLM model with vast.ai/runpod.ai for some number of customers and testing throughput

# Overview
1. What do we need?
   + A GPU server
   + Software to run an api
   + Software to call the api (optionally supporting functions)
2. End-to-end example
3. Final notes and resources


## Server and API Setup
There are a few options for choosing a server and choosing software to run an API

### Choosing a server
The services I checked are:

Runpod
+ Easiest setup
+ Lowest price GPU is ~ per hour
+ A100 80GB is ~ per hour
+ Supports one click templates

Vast.AI
+ 15 min setup
+ Has some low price GPUs
+ A100 80GB is
+ Supports one click templates

AWS or Azure
+ Difficuil to get access to GPUs
+ expensive per hour

### Choosing API software

### Tips on GPU selection
GPUs are specified by:
+ Memory size (VRAM)
+ Computation speed (FLOPs)
+ Memory speed (GB/s) - specifically the speed to read from the GPU's main memory into the computation unit. This value is typically not shown on runpod or vast.ai dashboards.

Generaly, the higher any of these values, the more expensive to rent the GPUs.

#### Picking a GPU based on VRAM

    
### End-to-end example
We do the following in this section:
1. Setup an account on Vast.AI
2. Create SSH key pair
3. Create an GPU instance from the template to serve Mistral vLLM quantized version.
4. Test the throughput by simulating concurrent requests
5. Serving a function calling model

#### 1. Setup an account on Vast.AI
Vast.ai setup requires account and credit card setup. It also requires you to setup an rsa key pair in order to securely connect to your instance. 

![](https://github.com/llm-serving-with-vastai/imgs/setup1.png)



