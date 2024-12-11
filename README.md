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
In order to sign you need to go to vast.ai website, then choose one of two options: on-demand instances or interruptable instances. Next you will see what is presented below:

![setup1](https://github.com/user-attachments/assets/c6bc7b40-5875-43e6-a7e4-453fd72bc9df)

You need to click top right blue button "SIGN IN" and use your e-mail or google/github account to create a user. Next what you need to do is to top up your credentials. To try it out I recommend to ad as little as $5.

When this is done, you are ready for the next step.

#### 2. Create SSH key pair
SSH (Secure Shell) is a protocol for securely connecting to remote servers or devices, and SSH keys enable password-less authentication for enhanced security. On Linux one can use the command `ssh-keygen -t rsa` to generate an SSH key pair (public and private keys) utilizing the RSA algorithm (`-t rsa` specifies the type of key to generate- here, it selects the RSA algorithm).

**What Happens During Execution**:
+ Command Execution: When you run the command, the system prompts you to specify a file location to save the generated keys (by default, it saves them in `~/.ssh/`).
+ Passphrase (Optional): You can set a passphrase to secure the private key further. If you skip this step, the private key will have no additional encryption.
+ Output: Two files are created:
   + Private Key: (e.g., `id_rsa`) This file contains the private key and should remain confidential.
   + Public Key: (e.g., `id_rsa.pub`) This file contains the public key and is shared with remote servers for authentication purposes.
 
**Practical Usage**:
+ The public key (e.g., `id_rsa.pub`) is copied to the server in the `~/.ssh/authorized_keys` file, enabling authentication.
+ The private key (e.g., `id_rsa`) remains on your local machine and is used to authenticate connections.

[Screencast from 11.12.2024 11:48:56.webm](https://github.com/user-attachments/assets/8362417b-0753-4657-9e3a-9959597e69d9)



